import json
import logging
import jsonschema
import os
from jsonschema import validate

import pydash


class JsonUtils:
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    @staticmethod
    def get_value_by_path(json_object, path):
        return pydash.get(json_object, path)

    @staticmethod
    def validate_json_schema(response_json, schema_path):
        """Метод для валидации JSON ответа по схеме"""
        ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
        PROJECT_ROOT = os.path.dirname(ROOT_DIR)
        schema_path = os.path.join(PROJECT_ROOT, 'schemas', schema_path)
        with open(f'{schema_path}', 'r') as schema_file:
            schema = json.load(schema_file)
        try:
            validate(instance=response_json, schema=schema)
            print("JSON соответствует схеме.")
        except jsonschema.exceptions.ValidationError as err:
            print(f"Ошибка валидации: {err.message}")
            raise

    @staticmethod
    def string_to_list(input_string):
        return [input_string]
