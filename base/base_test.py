import pytest

from clients.api_сlient import APIClient


class BaseTest:
    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        """Настройка перед выполнением тестов."""
        self.auth_token = self.get_auth_token()
        self.api_client = APIClient(auth_header=self.auth_token)

    def get_auth_token(self):
        """Метод для получения токена авторизации (можно переопределить)."""
        return "your_auth_token"  # Это можно заменить запросом на авторизацию

    def send_post_request(self, endpoint, data):
        """Вспомогательный метод для отправки POST запроса."""
        return self.api_client.post(endpoint, data=data)

    def send_get_request(self, endpoint, params=None):
        """Вспомогательный метод для отправки GET запроса."""
        return self.api_client.get(endpoint, params=params)
