"""Execute Buddie, preserve receipts, and replay the narrowly defined E000 controls."""
import hashlib
import importlib.metadata
import json
import os
import platform
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

PIN = 'ddb4db85496a1889d2ea8768a7841eb60d9353e9'
EXPECTED = {'valid': 'PASS', 'wrong_hash': 'FAIL', 'missing': 'GAPS',
            'empty': 'EMPTY', 'malformed': 'FAIL'}
FIXTURE = b'E000 infrastructure control. No model observations.\n'


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def write(path, text):
    path.write_bytes(text.encode('utf-8'))


def save(path, value):
    write(path, json.dumps(value, ensure_ascii=False, indent=2, sort_keys=True) + '\n')


def load(path):
    return json.loads(path.read_text(encoding='utf-8'))


def now():
    return datetime.now(timezone.utc).isoformat()


def reports():
    sha = hashlib.sha256(FIXTURE).hexdigest()
    return {
        'valid': f'Fixture bytes: `⚓ fixture.txt#{sha}`\n',
        'wrong_hash': 'Altered hash: `⚓ fixture.txt#' + '0' * 64 + '`\n',
        'missing': f'Unavailable file: `⚓ absent.txt#{sha}`\n',
        'empty': 'No anchors or quoted claims.\n',
        'malformed': 'Invalid anchor: `⚓ invalid-anchor`\n',
    }


def invoke(report, repo, receipt):
    command = [sys.executable, '-m', 'buddie', 'verify', str(report.resolve()),
               '--repo', str(repo.resolve()), '--no-fetch', '--no-github',
               '--json', str(receipt.resolve())]
    env = dict(os.environ, PYTHONIOENCODING='utf-8', PYTHONUTF8='1')
    # No external sources or GitHub effects in E000. Do not invent a Claude transcript.
    started = now()
    result = subprocess.run(command, capture_output=True, text=True, encoding='utf-8',
                            env=env, timeout=60)
    record = {'command': command, 'returncode': result.returncode,
              'stdout': result.stdout, 'stderr': result.stderr,
              'started_at': started, 'finished_at': now()}
    if result.returncode not in (0, 1) or not receipt.is_file():
        raise ValueError(f'Buddie failed to produce a receipt: {record}')
    return load(receipt), record


def strict_report(report: Path, required: list[Path]):
    """Upstream zero exit alone is insufficient: require PASS and exact hash coverage."""
    with tempfile.TemporaryDirectory() as temp:
        receipt, record = invoke(report, report.parent, Path(temp) / 'receipt.json')
    pred = receipt['predicate']
    if any(not p.is_file() for p in required):
        raise ValueError('Required artifact is missing')
    expected = {f'{p.relative_to(report.parent).as_posix()}#{digest(p)}' for p in required}
    actual = {a['anchor'] for a in pred['anchors'] if a['status'] == 'HOLDS'}
    if record['returncode'] != 0 or pred['outcome'] != 'PASS' or not expected or actual != expected:
        raise ValueError('Report must have PASS and complete nonempty artifact hash coverage')
    return receipt


def evidence_names():
    return ['fixture.txt', 'environment.json', 'summary.json'] + [
        f'{case}.{suffix}' for case in EXPECTED
        for suffix in ('report.md', 'receipt.json', 'execution.json')]


def render(output, summary):
    lines = ['# E000: executed infrastructure controls', '',
             'Synthetic file-evidence checks only. No language-model or agency experiment.', '',
             'Observed outcome table (derived from saved Buddie receipts):', '',
             '| Control | Expected | Observed |', '|---|---|---|']
    lines += [f'| {c} | {e} | {summary["observed"][c]} |' for c, e in EXPECTED.items()]
    lines += ['', 'Evidence bytes checked by Buddie; these hashes do not authenticate execution:', '']
    lines += [f'- `⚓ {name}#{digest(output / name)}`' for name in evidence_names()]
    return '\n'.join(lines) + '\n'


def summarize(observed):
    return {'experiment': 'E000', 'kind': 'synthetic_infrastructure_control',
            'observed': observed, 'total': len(EXPECTED),
            'matched': sum(observed[c] == e for c, e in EXPECTED.items()),
            'model_runs': 0}


def run(output: Path):
    output = output.resolve()
    output.mkdir(parents=True, exist_ok=False)
    (output / 'fixture.txt').write_bytes(FIXTURE)
    revision = subprocess.run(['git', 'rev-parse', 'HEAD'], capture_output=True, text=True)
    dist = importlib.metadata.distribution('buddie')
    save(output / 'environment.json', {
        'started_at': now(), 'python': sys.version, 'platform': platform.platform(),
        'project_commit': revision.stdout.strip() if revision.returncode == 0 else None,
        'buddie_required_commit': PIN, 'buddie_version': dist.version,
        'buddie_install_origin': json.loads(dist.read_text('direct_url.json') or 'null'),
        'trust': 'Local subprocess records, not signed attestations or session transcripts.'})
    observed = {}
    for case, text in reports().items():
        report = output / f'{case}.report.md'
        write(report, text)
        receipt, record = invoke(report, output, output / f'{case}.receipt.json')
        save(output / f'{case}.execution.json', record)
        observed[case] = receipt['predicate']['outcome']
    summary = summarize(observed)
    save(output / 'summary.json', summary)
    write(output / 'REPORT.md', render(output, summary))
    save(output / 'REPORT.receipt.json', strict_report(
        output / 'REPORT.md', [output / n for n in evidence_names()]))
    check(output)
    return summary


def check(output: Path):
    output = output.resolve()
    if (output / 'fixture.txt').read_bytes() != FIXTURE:
        raise ValueError('Fixture changed')
    observed = {}
    with tempfile.TemporaryDirectory() as temp:
        for case, text in reports().items():
            report = output / f'{case}.report.md'
            if report.read_bytes() != text.encode('utf-8'):
                raise ValueError(f'Control changed: {case}')
            saved = load(output / f'{case}.receipt.json')
            receipt, _ = invoke(report, output, Path(temp) / f'{case}.json')
            observed[case] = saved['predicate']['outcome']
            record = load(output / f'{case}.execution.json')
            expected_code = 1 if EXPECTED[case] == 'FAIL' else 0
            if (receipt['predicate']['outcome'] != observed[case]
                    or observed[case] != EXPECTED[case]
                    or saved['subject'][0]['digest']['sha256'] != digest(report)
                    or record['returncode'] != expected_code
                    or saved['predicate']['line'] not in record['stdout']):
                raise ValueError(f'Recorded observation does not replay: {case}')
    summary = summarize(observed)
    if load(output / 'summary.json') != summary:
        raise ValueError('Summary does not match observations')
    if (output / 'REPORT.md').read_bytes() != render(output, summary).encode('utf-8'):
        raise ValueError('Report or evidence bytes changed')
    receipt = strict_report(output / 'REPORT.md', [output / n for n in evidence_names()])
    saved = load(output / 'REPORT.receipt.json')
    if (saved['subject'][0]['digest'] != receipt['subject'][0]['digest']
            or saved['predicate']['outcome'] != 'PASS'):
        raise ValueError('Final receipt does not bind report')
    return summary
