import pytest

from clients.api_сlient import APIClient
from utils.token_manager import TokenManager


class BaseTest:

    @pytest.fixture(scope="class", autouse=True)
    def setup(self):
        """Настройка перед выполнением тестов."""
        login = TokenManager.login_request("+77013132777", "ASDasd1234!")
        self.auth_token = TokenManager.get_client_access_token()
        self.api_client = APIClient(auth_header=self.auth_token)

    def send_post_request(self, endpoint, data):
        """Вспомогательный метод для отправки POST запроса."""
        return self.api_client.post(endpoint, data=data)

    def send_get_request(self, endpoint, params=None):
        """Вспомогательный метод для отправки GET запроса."""
        return self.api_client.get(endpoint, params=params)
