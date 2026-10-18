import json
import shutil
import subprocess
import tempfile
import unittest
from pathlib import Path

from agency.controls import run, check, strict_report


class ControlsTest(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.out = Path(self.temp.name) / 'bundle'

    def test_real_controls_and_replay(self):
        run(self.out)
        metrics = json.loads((self.out / 'summary.json').read_text())
        self.assertEqual(metrics['observed'], {
            'valid': 'PASS', 'wrong_hash': 'FAIL', 'missing': 'GAPS',
            'empty': 'EMPTY', 'malformed': 'FAIL'})
        self.assertEqual(metrics['matched'], 5)
        check(self.out)

    def test_never_overwrites(self):
        self.out.mkdir()
        with self.assertRaises(FileExistsError):
            run(self.out)

    def test_bundle_replays_after_relocation(self):
        run(self.out)
        relocated = self.out.parent / 'relocated'
        shutil.copytree(self.out, relocated)
        check(relocated)

    def test_changed_report_prose_rejected(self):
        run(self.out)
        p = self.out / 'REPORT.md'
        p.write_bytes(p.read_bytes() + b'Invented conclusion.\n')
        with self.assertRaises(ValueError):
            check(self.out)

    def test_changed_final_receipt_rejected(self):
        run(self.out)
        p = self.out / 'REPORT.receipt.json'
        data = json.loads(p.read_text())
        data['subject'][0]['digest']['sha256'] = '0' * 64
        p.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            check(self.out)

    def test_changed_final_receipt_anchor_verdict_rejected(self):
        run(self.out)
        p = self.out / 'REPORT.receipt.json'
        data = json.loads(p.read_text())
        data['predicate']['anchors'][0]['status'] = 'BROKEN'
        p.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            check(self.out)

    def test_changed_fixture_rejected(self):
        run(self.out)
        (self.out / 'fixture.txt').write_text('altered\n')
        with self.assertRaises(ValueError):
            check(self.out)

    def test_evidence_bytes_survive_git_checkout(self):
        root = self.out.parent / 'repo'
        bundle = root / 'results' / 'E000'
        run(bundle)
        attributes = Path(__file__).resolve().parents[1] / '.gitattributes'
        shutil.copyfile(attributes, root / '.gitattributes')
        raw = root / 'results' / 'byte-fidelity.txt'
        raw.write_bytes(b'original\r\nbytes\r\n')
        for args in (['init', str(root)], ['-C', str(root), 'add', '.']):
            subprocess.run(['git', *args], check=True, capture_output=True)
        exported = self.out.parent / 'exported'
        exported.mkdir()
        subprocess.run(['git', '-C', str(root), 'checkout-index', '--all',
                        '--prefix=' + exported.as_posix() + '/'], check=True, capture_output=True)
        for path in (root / 'results').rglob('*'):
            if path.is_file():
                self.assertEqual(path.read_bytes(), (exported / path.relative_to(root)).read_bytes())
        check(exported / 'results' / 'E000')

    def test_changed_metrics_rejected(self):
        run(self.out)
        p = self.out / 'summary.json'
        data = json.loads(p.read_text())
        data['matched'] = 999
        p.write_text(json.dumps(data))
        with self.assertRaises(ValueError):
            check(self.out)

    def test_missing_receipt_rejected(self):
        run(self.out)
        (self.out / 'valid.receipt.json').unlink()
        with self.assertRaises((ValueError, FileNotFoundError)):
            check(self.out)

    def test_strict_empty_rejected(self):
        self.out.mkdir()
        p = self.out / 'report.md'
        p.write_text('No checked evidence.\n')
        with self.assertRaises(ValueError):
            strict_report(p, [])

    def test_strict_gap_rejected(self):
        self.out.mkdir()
        p = self.out / 'report.md'
        p.write_text('`⚓ absent.txt#' + '0' * 64 + '`\n', encoding='utf-8')
        with self.assertRaises(ValueError):
            strict_report(p, [self.out / 'absent.txt'])

    def test_strict_uncovered_file_rejected(self):
        run(self.out)
        (self.out / 'not-covered.txt').write_bytes(b'additional evidence\n')
        with self.assertRaises(ValueError):
            strict_report(self.out / 'REPORT.md', [self.out / 'not-covered.txt'])


if __name__ == '__main__':
    unittest.main()
