#!/usr/bin/python3
"""
#
# Test if all of the requirements are up to date
#
"""

import os
import subprocess
import sys

pip_bin = 'env/bin/pip3'
if len(sys.argv) > 1:
    pip_bin = sys.argv[1]
project_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pip_dir = (subprocess.check_output([pip_bin, '-V']).decode()
           .split('\n')[0].split(' from')[-1].split()[0])

# check if the venv reported by pip is under the project directory
if not pip_dir.startswith(project_dir):
    # not running a venv, so it isn't out of date...
    sys.exit(0)

def _check_file(file_name):
    want = {}
    with open(file_name) as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('-') and not line.startswith('#'):
                req = line.split('/')[-1].split('#')[0].replace('.git', '').replace('==', '@').split('@')
                if 'egg=' in line:
                    # the egg name can be different than the repo name
                    req = line.split('egg=')[1].split('&')[0], req[1]
                want[req[0].lower().replace('_', '-')] = req[1].strip('v').strip()
    
    have = {
        k.lower(): v for k, v in [
            line.split('==') for
            line in subprocess.check_output([pip_bin, 'freeze']).decode().split('\n')
            if not line.startswith('-') and line]
    }
    
    result = [f'{req} -->  want:{want[req]}  have:{have.get(req)}'
              for req in want if have.get(req) != want[req]]
    
    if result:
        # if we have any mismatched packages, then report them
        print('ERROR: venv out of date:')
        for line in result:
            print(f'  {line}')
        print('TRY:')
        print('  make prepare-venv')
        sys.exit(1)


_check_file('requirements.dev')
_check_file('requirements.prod')
