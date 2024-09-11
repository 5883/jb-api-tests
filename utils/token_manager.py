import requests
import json
import os
import jsonschema
from assert_utils import AssertUtils

from configs import base_url
from utils.json_utils import JsonUtils


class TokenManager:
    BASE_URL = base_url
    HEADERS = {"Content-Type": "application/json", "Client-Type": "web"}

    code = None
    id = None
    signature = None

    @staticmethod
    def load_schema(schema_name):
        """Загрузка JSON-схемы из файла."""
        schema_path = os.path.join(os.path.dirname(__file__), 'schemas', schema_name)
        with open(schema_path, 'r') as schema_file:
            return json.load(schema_file)

    @staticmethod
    def get_client_access_token():
        url = f"{TokenManager.BASE_URL}/oauth/token"
        headers = {"Content-Type": "application/x-www-form-urlencoded",
                   "Authorization": "Basic d2ViYXBwOnJqWkk5TWZRT2Y="}
        data = {"grant_type": "client_credentials"}
        response = requests.post(url, headers=headers, verify=False, data=data)

        schema = TokenManager.load_schema("createClientTokenResponse.json")
        jsonschema.validate(response.json(), schema)

        response_data = response.json()
        assert response_data["token_type"] == "bearer"
        return response_data["access_token"]

    @staticmethod
    def get_sms_code(access_token, phone_number):
        url = f"{TokenManager.BASE_URL}/auth/phone/token"
        headers = {**TokenManager.HEADERS, "Authorization": f"Bearer {access_token}"}
        request_body = {
            "iin_list": TokenManager.iin_list,
            "phone_number": phone_number
        }

        response = requests.post(url, json=request_body, headers=headers)
        assert response.status_code == 200

        schema = TokenManager.load_schema("sendSmsResponse.json")
        jsonschema.validate(response.json(), schema)

        sms_code_response = response.json()
        assert sms_code_response["phone"] == phone_number
        assert sms_code_response["subject"] == phone_number

        TokenManager.code = sms_code_response["code"]
        TokenManager.id = sms_code_response["id"]
        TokenManager.signature = sms_code_response["signature"]

    @staticmethod
    def verify_sms_values(access_token, phone_number):
        url = f"{TokenManager.BASE_URL}/auth/phone/token/{TokenManager.id}"
        headers = {**TokenManager.HEADERS, "Authorization": f"Bearer {access_token}",
                   "SMSAuthorization": TokenManager.signature}
        request_body = {
            "id": TokenManager.id,
            "date": "2024-09-01",
            "type": "PHONE",
            "phone_number": phone_number,
            "signature": TokenManager.signature,
            "code": TokenManager.code
        }

        response = requests.put(url, json=request_body, headers=headers)
        assert response.status_code == 200

        schema = TokenManager.load_schema("verifySmsValuesResponse.json")
        jsonschema.validate(response.json(), schema)
        TokenManager.signature = response.json()["signature"]

    @staticmethod
    def create_device_token(access_token, phone_number):
        url = f"{TokenManager.BASE_URL}/auth/device/token"
        headers = {**TokenManager.HEADERS, "Authorization": f"Bearer {access_token}",
                   "PhoneAuthorization": TokenManager.signature}
        request_body = {"phone_number": phone_number}

        response = requests.post(url, json=request_body, headers=headers)
        AssertUtils.assert_status_code(response, 200)
        schema = TokenManager.load_schema("createDeviceTokenResponse.json")
        jsonschema.validate(response.json(), schema)

        TokenManager.signature = response.json()["signature"]
