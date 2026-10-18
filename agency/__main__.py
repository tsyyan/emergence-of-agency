import argparse
import json
from pathlib import Path

from agency.controls import run, check


def main():
    parser = argparse.ArgumentParser(description='E000 infrastructure controls; no model experiment')
    sub = parser.add_subparsers(dest='action', required=True)
    sub.add_parser('run').add_argument('--output', required=True, type=Path)
    sub.add_parser('check').add_argument('directory', type=Path)
    args = parser.parse_args()
    try:
        result = run(args.output) if args.action == 'run' else check(args.directory)
    except (ValueError, OSError, KeyError) as error:
        parser.exit(1, f'Check failed: {error}\n')
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
