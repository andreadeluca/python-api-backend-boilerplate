import logging
from logging import exception
from pathlib import Path
from dotenv import load_dotenv
import json

CONFIG_PATH = Path(__file__).parent / "config.json"


class Settings:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            try:
                logging.info("Loading settings from {}".format(CONFIG_PATH))
                with open(CONFIG_PATH, "r", encoding='UTF-8') as file:
                    result = json.load(file)
                    cls._instance = super().__new__()
                    cls.instance = result
            except (FileNotFoundError,json.JSONDecodeError) as e:
                logging.error("Config load error (%s): %s", type(e).__name__, e)
            raise
        return cls._instance