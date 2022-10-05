import os
from setuptools import setup
from mypyc.build import mypycify

DO_COMPILE = os.environ.get("PYTHON_MYPY_COMPILE", None)

# NOTE: Place any modules you wish compiled here
if DO_COMPILE is not None:
    setup(
        ext_modules=mypycify([
            "src/log_color/formatters.py",
            "src/log_color/lib.py",
        ])
    )
else:
    setup()
