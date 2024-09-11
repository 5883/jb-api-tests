import json
import logging
from venv import logger

import pydash


class JsonUtils:

    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_value_by_path(json_object, path):
        return pydash.get(json_object, path)
