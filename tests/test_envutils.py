import os
import pytest
from ezboilerplate.utils import envUtils


def test_is_in_dev_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "DEV")
    from importlib import reload
    reload(envUtils)  # ricarico il modulo per rileggere ENVIRONMENT
    assert envUtils.is_in_dev_env() is True
    assert envUtils.is_in_prod_env() is False


def test_is_in_prod_env(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "PRODUCTION")
    from importlib import reload
    reload(envUtils)
    assert envUtils.is_in_prod_env() is True
    assert envUtils.is_in_dev_env() is False


def test_default_env_is_dev(monkeypatch):
    monkeypatch.delenv("ENVIRONMENT", raising=False)
    from importlib import reload
    reload(envUtils)
    assert envUtils.is_in_dev_env() is True