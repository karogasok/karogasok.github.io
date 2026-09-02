"""Shared fixtures and the emtsv availability gate."""

from __future__ import annotations

import pytest
import requests

from karogasok_temak.emtsv import DEFAULT_BASE_URL


def _emtsv_running() -> bool:
    """Whether an emtsv server answers on the default port."""
    try:
        requests.get(DEFAULT_BASE_URL, timeout=2)
    except requests.RequestException:
        return False
    return True


needs_emtsv = pytest.mark.skipif(
    not _emtsv_running(),
    reason="emtsv is not running; start it with `make emtsv-up`",
)
