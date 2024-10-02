from __future__ import annotations

from contextlib import contextmanager
import importlib.util
import logging
import logging.config
import os
import sys
from pathlib import Path
import platform
import secrets
import socket
import typing as t

log: logging.Logger = logging.getLogger("nox")

import nox

sys.path.append(os.path.abspath("nox_extra"))

## Set nox options
if importlib.util.find_spec("uv"):
    nox.options.default_venv_backend = "uv|virtualenv"
else:
    nox.options.default_venv_backend = "virtualenv"
nox.options.reuse_existing_virtualenvs = True
nox.options.error_on_external_run = False
nox.options.error_on_missing_interpreters = False
# nox.options.report = True


try:
    ## Import extra nox modules from a "nox_extra/" directory.
    import nox_utils

    nox_utils.setup_nox_logging()

    log.info(
        "nox_extra module detected, enhancements from nox_extra.nox_utils are now available."
    )
except ImportError:
    log.error("Unable to import nox_utils.")

try:
    ## Import pytest sessions
    import nox_pytest_sessions
except ImportError:
    log.error("Unable to import pytest sessions.")

## Define versions to test
PY_VERSIONS: list[str] = nox_utils.PY_VERSIONS
## Get tuple of Python ver ('maj', 'min', 'mic')
PY_VER_TUPLE: tuple[str, str, str] = nox_utils.PY_VER_TUPLE
## Dynamically set Python version
DEFAULT_PYTHON: str = nox_utils.DEFAULT_PYTHON

DEFAULT_LINT_PATHS: list[str] = nox_utils.DEFAULT_LINT_PATHS
## Set directory for requirements.txt file output
REQUIREMENTS_OUTPUT_DIR: Path = nox_utils.REQUIREMENTS_OUTPUT_DIR

nox_utils.append_lint_paths(extra_paths=["nox_extra"], lint_paths=DEFAULT_LINT_PATHS)
