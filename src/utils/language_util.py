import glob
import json
from pathlib import Path
from core.logger import logger
from core.config import settings
import os

language_dict = {}
default_lang = settings.DEFAULT_LANGUAGE
languages_array = []

def language_init():
    """Loads language JSON files and builds the language dictionary."""
    
    BASE_DIR = Path("./src/languages/*.json")

    for filename in glob.glob(str(BASE_DIR)):
        lang_code = filename.split('/')[-1].split('.')[0]
        with open(filename, 'r') as f:
            language_dict[lang_code] = json.load(f)

def get_message(language=default_lang, key=None, bot_id=None):
    """Retrieves a message from the language dictionary, handling fallbacks."""

    message = None
    try:
        if bot_id:
            message = language_dict[language].get(key, {}).get(bot_id)
        if not message:
            message = language_dict[language].get(key)
        if message:
            return json.loads(json.dumps(message))
    except KeyError:
        logger.warn(f"❌ Object doesn't exist for {language}.{key}")
        logger.info(f"Getting default language (en) message for key: {key}")
        if bot_id:
            message = language_dict[default_lang].get(key, {}).get(bot_id)
        if not message:
            message = language_dict[default_lang].get(key)
        if message:
            return json.loads(json.dumps(message))
    return None

def get_languages():
    """Returns the global languages array."""
    languages = settings.SUPPORTED_LANGUAGES.split(",")
    return list(filter(lambda x: x.get("code") in languages , settings.LANGUAGES))