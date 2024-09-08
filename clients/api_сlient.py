import requests

class APIClient:
    BASE_URL = "https://api.example.com"

    def __init__(self, auth_header=None):
        self.session = requests.Session()
        self.auth_header = auth_header

    def create_request_specification(self):
        """Создание спецификации запроса с заголовками."""
        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }
        if self.auth_header:
            headers["Authorization"] = f"Bearer {self.auth_header}"
        return headers

    def post(self, endpoint, data=None):
        """Отправка POST запроса с заголовками."""
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.create_request_specification()
        return self.session.post(url, json=data, headers=headers)

    def get(self, endpoint, params=None):
        """Отправка GET запроса с заголовками."""
        url = f"{self.BASE_URL}{endpoint}"
        headers = self.create_request_specification()
        return self.session.get(url, params=params, headers=headers)
