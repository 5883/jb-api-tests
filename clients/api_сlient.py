import requests
from utils.logger import Logger

from configs import base_url


class APIClient:
    _access_token = None
    __base_url = base_url
    headers = {
        "Client-Type": "web",
        "Content-type": "application/json"
    }

    def __init__(self, access_token):
        self._access_token = access_token
        self.session = requests.Session()

    def _updated_headers(self):
        updated_headers = self.headers.copy()
        updated_headers["Authorization"] = f"Bearer {self._access_token}"
        return updated_headers

    def request(self, method, endpoint, data=None, json=None, params=None, status_code=None):
        """Общий метод для отправки запросов."""
        url = f"{self.__base_url}{endpoint}"
        response = self.session.request(
            method=method,
            url=url,
            headers=self._updated_headers(),
            data=data,
            json=json,
            params=params,
            verify=False
        )
        Logger.log_request_response(response)
        if response.status_code != status_code:
            response.raise_for_status()
        return response.json()


    def get(self, endpoint, status_code=None):
        """Метод для GET-запросов."""
        return self.request("GET", endpoint, status_code=status_code)

    def post(self, endpoint, data=None, json=None, params=None, status_code=None):
        """Метод для POST-запросов."""
        return self.request("POST", endpoint, data=data, json=json, params=params, status_code=status_code)

    def put(self, endpoint, data=None, json=None, params=None, status_code=None):
        """Метод для PUT-запросов."""
        return self.request("PUT", endpoint, data=data, json=json, params=params, status_code=status_code)

    def patch(self, endpoint, data=None, json=None, params=None, status_code=None):
        """Метод для PATCH-запросов."""
        return self.request("PATCH", endpoint, data=data, json=json, params=params, status_code=status_code)

    def delete(self, endpoint, data=None, json=None, params=None, status_code=None):
        """Метод для DELETE-запросов."""
        return  self.request("DELETE", endpoint,  data=data, json=json, params=params, status_code=status_code)
