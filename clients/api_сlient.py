import requests

class Client:
    BASE_URL = "https://api.example.com"

    def __init__(self):
        self.session = requests.Session()

    def post(self, endpoint, data=None, headers=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.post(url, json=data, headers=headers)
        return response

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.BASE_URL}{endpoint}"
        response = self.session.get(url, params=params, headers=headers)
        return response
