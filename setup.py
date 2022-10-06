import os
from setuptools import setup

DO_COMPILE = bool(os.environ.get("PYTHON_MYPY_COMPILE", None))

# NOTE: Place any modules you wish compiled here
if DO_COMPILE:
    from mypyc.build import mypycify
    setup(
        ext_modules=mypycify([
            "src/log_color/formatters.py",
            "src/log_color/lib.py",
        ])
    )
else:
    setup()
