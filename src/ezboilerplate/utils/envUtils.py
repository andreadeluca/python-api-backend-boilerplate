import os

PROD_STR_TUPLE = ('PROD', 'PRODUCTION')
DEV_STR_TUPLE = ('DEV', 'DEVELOPMENT')
LOC_STR_TUPLE = ('LOC', 'LOCAL')
STG_STR_TUPLE = ('STG', 'STAGING', 'STAGE', 'TEST')
ENVIRONMENT = os.getenv("ENVIRONMENT", "development").upper()
ALL_ENV = PROD_STR_TUPLE + DEV_STR_TUPLE + LOC_STR_TUPLE + STG_STR_TUPLE

if ENVIRONMENT is None or ENVIRONMENT not in ALL_ENV:
    raise ValueError('ENVIRONMENT not valid. Please specify a valid environment in .env file.')


def is_in_prod_env():
    return ENVIRONMENT in PROD_STR_TUPLE


def is_in_dev_env():
    return ENVIRONMENT in DEV_STR_TUPLE
