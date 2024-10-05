import requests

import configs
from configs import base_url, phone_number, iin, password


class AuthService:
    _access_token = None
    _id = None
    _code = None
    _signature = None
    _headers = None
    _body = None
    _data = None
    _json = None
    _response = None
    _url = None

    def _create_client_token(self):
        self._headers = {
            "Content-type": "application/x-www-form-urlencoded",
            "Authorization": "Basic d2ViYXBwOnJqWkk5TWZRT2Y="
        }
        self._data = {
            "grant_type": "client_credentials"
        }

        self._response = requests.post(f'{base_url}/api/v1/oauth/token', headers=self._headers, data=self._data,
                                       cert=(configs.cert, configs.key), verify=False)
        self._json = self._response.json()
        self._access_token = self._json.get("access_token")

    def _send_sms(self):
        self._headers = {
            "Client-Type": "web",
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self._access_token}"
        }

        self._body = {
            "actionIds": [iin],
            "phone": phone_number
        }

        self._response = requests.post(f'{base_url}/api/v1/auth/phone/token', headers=self._headers,
                                       cert=(configs.cert, configs.key), json=self._body, verify=False)
        self._json = self._response.json()
        self._id = self._json.get("id")
        self._signature = self._json.get("signature")
        self._code = self._json.get("code")

    def _verify_sms_values(self):
        self._url = f'{base_url}/api/v1/auth/phone/token/{self._id}'
        self._headers = {
            "SMSAuthorization": self._signature,
            "Authorization": f"Bearer {self._access_token}",
            "Client-Type": "web",
            "Content-Type": "application/json"
        }
        self._body = {
            "actionIds": [iin],
            "code": self._code,
            "id": self._id,
            "phone": phone_number,
        }

        self._response = requests.put(
            self._url,
            headers=self._headers,
            json=self._body,
            cert=(configs.cert, configs.key),
            verify=False
        )

        self._json = self._response.json()
        self._signature = self._json.get("signature")

    def _create_device_token(self):
        self._url = f'{base_url}/api/v1/auth/device/token'
        self._headers = {
            "PhoneAuthorization": self._signature,
            "Authorization": f"Bearer {self._access_token}",
            "Client-Type": "web",
            "Content-Type": "application/json"
        }

        self._body = {"phone": phone_number}

        self._response = requests.post(self._url, headers=self._headers, json=self._body,
                                       cert=(configs.cert, configs.key), verify=False)
        self._json = self._response.json()
        self._signature = self._json.get("signature")

    def login(self):
        self._create_client_token()
        self._send_sms()
        self._verify_sms_values()
        self._create_device_token()

        self._url = f'{base_url}/api/v1/oauth/token'

        self._headers = {
            "DeviceAuthorization": self._signature,
            "Authorization": f"Basic d2ViYXBwOnJqWkk5TWZRT2Y=",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        self._data = {
            "username": phone_number,
            "password": password
        }

        params = {"grant_type": "password"}

        self._response = requests.post(self._url, headers=self._headers, data=self._data, params=params,
                                       cert=(configs.cert, configs.key), verify=False)
        return self._response.json()
