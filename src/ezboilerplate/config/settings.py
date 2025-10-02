import os
from dotenv import load_dotenv

ENVIRONMENT = os.getenv("ENVIRONMENT", "development").upper()
PROD_STR_TUPLE = ('PROD','PRODUCTION')
DEV_STR_TUPLE = ('DEV','DEVELOPMENT')
#TODO DATABASE MANAGER QUA DENTRO? FORSE Sì
#TODO CHECK DELLE VARIABILI CRITICHE ALTRIMENTI COL CAZZO CHE PARTE

#The configuration will always be loaded from local .env if environment is dev
if ENVIRONMENT in DEV_STR_TUPLE:
    load_dotenv(dotenv_path=".env",override=True)

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
