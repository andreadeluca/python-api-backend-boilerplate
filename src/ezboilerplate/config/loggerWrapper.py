import logging
from ezboilerplate.utils import envUtils

_configured_loggers = set()


def get_logger(name: str):
    logger: logging.Logger = logging.getLogger(name)
    if name not in _configured_loggers:
        handler = logging.StreamHandler()
        if envUtils.is_in_dev_env():
            logger.setLevel(logging.DEBUG)
            #detailed text for dev env
            fmt = "%(levelname)s [%(name)s] %(message)s"
        else:
            logger.setLevel(logging.INFO)
            #minimal json for non-local env
            fmt = '{"ts":"%(asctime)s","level":"%(levelname)s","service":"%(name)s","msg":"%(message)s"}'
        formatter = logging.Formatter(fmt)
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        _configured_loggers.add(name)
    return logger
