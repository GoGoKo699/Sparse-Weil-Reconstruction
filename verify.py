#!/usr/bin/env python3
"""Verify the preserved import and replay its two exact research reports."""
import argparse
import hashlib
import json
from pathlib import Path
import subprocess
import sys


def main():
    if not __debug__ or sys.flags.optimize:
        raise SystemExit('Do not use -O or -OO for research verification.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--integrity-only', action='store_true',
                        help='Check imported bytes without running experiments.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    manifest = json.loads((root / 'provenance/import-manifest.json').read_text())
    for entry in manifest['files']:
        path = root / entry['path']
        raw = path.read_bytes()
        blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
        if (len(raw) != entry['size_bytes'] or
                hashlib.sha256(raw).hexdigest() != entry['sha256'] or
                blob != entry['git_blob']):
            raise SystemExit('Preserved import mismatch: ' + entry['path'])
    print(f"Import integrity: {len(manifest['files'])} preserved files passed.", flush=True)
    if args.integrity_only:
        return
    for name in ('all_field_reconstruction_v1', 'reconstruction_audit_v1'):
        script = root / 'experiments' / name / 'verify.py'
        subprocess.run([sys.executable, str(script)], cwd=root, check=True)
    print('Both exact research reports reproduced. Input promises remain external.')


if __name__ == '__main__':
    main()
