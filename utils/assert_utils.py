# assert_utils.py
import jsonschema
import json


class AssertUtils:

    @staticmethod
    def assert_json_schema(data, schema):
        """Проверка соответствия данных JSON схеме."""
        jsonschema.validate(instance=data, schema=schema)

    @staticmethod
    def assert_json_equal(actual_json, expected_json):
        """Сравнение двух JSON объектов."""
        assert json.dumps(actual_json, sort_keys=True) == json.dumps(expected_json, sort_keys=True), \
            f"JSON несоответствует:\nОжидаемый: {expected_json}\nАктуальный: {actual_json}"

    @staticmethod
    def assert_status_code(response, expected_status_code):
        """Проверка статуса ответа."""
        assert response.status_code == expected_status_code, \
            f"Ожидаемый статус код {expected_status_code}, получен {response.status_code}"
