from clients.api_сlient import Client
from utils.assert_utils import *


class RegistrationService:
    def __init__(self, client: Client):
        self.client = client

    def register_user(self, user_data):
        response = self.client.post("/register", data=user_data)
        AssertUtils.assert_status_code(response, 201)
