#!/usr/bin/env python3
"""Pin the first-g successor and reproduce its exact controls in fresh storage."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys
import tempfile


def main():
    if not __debug__ or sys.flags.optimize:
        raise SystemExit('Do not use -O or -OO for research verification.')
    here = Path(__file__).resolve().parent
    manifest = json.loads((here / 'MANIFEST.json').read_text())
    for name, digest in manifest['sha256'].items():
        if hashlib.sha256((here / name).read_bytes()).hexdigest() != digest:
            raise SystemExit('Hash mismatch: ' + name)
    dependency = here.parent / 'all_field_reconstruction_v1' / 'reconstruct.py'
    raw = dependency.read_bytes()
    blob = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest()
    if (hashlib.sha256(raw).hexdigest() != manifest['dependency']['sha256'] or
            blob != manifest['dependency']['git_blob']):
        raise SystemExit('Pinned logarithm dependency changed')
    with tempfile.TemporaryDirectory(prefix='first-g-reconstruction-') as directory:
        root = Path(directory)
        experiment = root / 'first_g_reconstruction_v1'
        experiment.mkdir()
        (root / 'all_field_reconstruction_v1').mkdir()
        for name in ('reconstruct.py', 'experiment.py'):
            shutil.copyfile(here / name, experiment / name)
        shutil.copyfile(dependency, root / 'all_field_reconstruction_v1' / 'reconstruct.py')
        result = subprocess.run([sys.executable, str(experiment / 'experiment.py')],
                                capture_output=True, check=True, timeout=120)
        if result.stdout != (here / 'REPORT.json').read_bytes():
            raise SystemExit('Exact report differs; inspect instead of overwriting.')
    report = json.loads(result.stdout)
    print('First-g reconstruction: source hashes, pinned logarithms, and exact report passed.')
    print(json.dumps(dict(
        supplied_polynomial_controls=len(report['controls']),
        recovered_coefficients=sum(row['recovered_coefficients'] for row in report['controls']),
        independent_companion_determinants=report['independent_companion_determinants'],
        allowed_log_displacement_runs=report['allowed_log_displacement_runs'],
        malformed_input_rejections=report['malformed_input_rejections']), sort_keys=True))
    print('Promised-input reconstruction; no count authentication or curve realization is certified.')


if __name__ == '__main__':
    main()
