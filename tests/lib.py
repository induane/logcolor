from __future__ import annotations

import logging
import os
from contextlib import contextmanager
from io import StringIO

from log_color.colors import ColorStr


@contextmanager
def temp_env(**kwargs):
    """
    Temporarily set environment variables inside the context, restoring on exit.

    Pass variables as keyword args. Use None to remove a variable inside the context.
    """
    old = {}
    for k, v in kwargs.items():
        old[k] = os.environ.get(k)
        if v is None:
            os.environ.pop(k, None)
        else:
            os.environ[k] = v
    try:
        # Clear cached detection so ColorStr picks up the environment change
        ColorStr.color_supported.cache_clear()
        yield
    finally:
        for k, ov in old.items():
            if ov is None:
                os.environ.pop(k, None)
            else:
                os.environ[k] = ov
        ColorStr.color_supported.cache_clear()


@contextmanager
def temp_logger(formatter: logging.Formatter, level=logging.INFO, fmt: str = "%(levelname)s: %(message)s"):
    """
    Create a temporary logger with a StreamHandler and a ColorFormatter, restore prior handlers on exit.

    Yields a tuple of (logger, stream) so tests can emit and inspect logged output.
    """
    stream = StringIO()
    name = f"temp-logger-{formatter.__name__}"
    handler = logging.StreamHandler(stream)
    handler.setFormatter(formatter(fmt))
    log = logging.getLogger(name)
    old_handlers = list(log.handlers)
    try:
        for h in old_handlers:
            log.removeHandler(h)
        log.setLevel(level)
        log.addHandler(handler)
        yield log, stream
    finally:
        # Remove our handler(s)
        for h in list(log.handlers):
            log.removeHandler(h)
        # Restore prior handlers
        for h in old_handlers:
            log.addHandler(h)
