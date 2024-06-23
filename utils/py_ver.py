import sys

MIN_PYTHON = (3, 8)
if sys.version_info < MIN_PYTHON:
    sys.exit(f'minimum required python is {MIN_PYTHON}')
