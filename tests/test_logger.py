import logging
import pytest
from ezboilerplate.utils import envUtils
from ezboilerplate.config import loggerWrapper

def test_logger_in_dev(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "DEV")
    from importlib import reload
    reload(envUtils)

    logger = loggerWrapper.get_logger("test.module")
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.DEBUG


def test_logger_in_prod(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "PRODUCTION")
    from importlib import reload
    reload(envUtils)

    logger = loggerWrapper.get_logger("test.module.prod")
    assert isinstance(logger, logging.Logger)
    assert logger.level == logging.INFO


def test_logger_cache(monkeypatch):
    monkeypatch.setenv("ENVIRONMENT", "DEV")
    from importlib import reload
    reload(envUtils)

    logger1 = loggerWrapper.get_logger("same.module")
    logger2 = loggerWrapper.get_logger("same.module")
    assert logger1 is logger2  # deve restituire lo stesso oggetto
