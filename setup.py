import os
from setuptools import setup

DO_COMPILE = bool(os.environ.get("MYPYC_PYTHON_COMPILE", False))

# NOTE: Place any modules you wish compiled here
if DO_COMPILE:
    from mypyc.build import mypycify
    setup(
        ext_modules=mypycify([
            'src/log_color/lib.py',
            'src/log_color/formatters.py',
        ])
    )
else:
    setup()
