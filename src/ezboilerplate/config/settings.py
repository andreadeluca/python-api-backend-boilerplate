import os

from dotenv import load_dotenv

import loggerWrapper as lw
from ezboilerplate.utils import envUtils

# TODO DATABASE MANAGER QUA DENTRO? FORSE Sì
# TODO CHECK DELLE VARIABILI CRITICHE ALTRIMENTI COL CAZZO CHE PARTE

_logger = lw.get_logger(__name__)

# The configuration will always be loaded from local .env if environment is dev
if envUtils.is_in_dev_env():
    try:
        load_dotenv(dotenv_path=".env", override=True)
    except IOError as e:
        _logger.error(e)
    except Exception as e:
        _logger.exception(e)


def retrieve_setting(settingstr: str, default=None, type=None):
    """

    :param default: Optional parameter, you can use it whether you would like
    to give a default value if the environment variable is not set.
    :type settingstr: str
    """
    value = os.environ.get(settingstr, default)

    if type is int:
        try:
            return int(value)
        except (TypeError, ValueError):
            return default
    elif type is bool:
        if value is None:
            return default
        return str(value).strip().lower() in ("1", "true", "yes", "on")
    else:
        return value


def retrieve_bool_setting(settingstr: str, default=None):
    return retrieve_setting(settingstr, default, bool)


def retrieve_int_setting(settingstr: str, default=None):
    return retrieve_setting(settingstr, default, int)
