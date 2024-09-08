import pytest
from base.base_test import BaseTest
from data.user_data import UserData


class TestUserRegistration(BaseTest):

    def test_successful_registration(self):
        """Проверка успешной регистрации пользователя."""
        user_data = UserData.valid_user()
        response = self.send_post_request("/register", data=user_data)

        assert response.status_code == 201, "Expected status code 201, got {response.status_code}"
        response_data = response.json()
        assert response_data["message"] == "User registered successfully"
        assert "token" in response_data

    def test_registration_with_invalid_data(self):
        """Проверка регистрации с некорректными данными."""
        user_data = UserData.invalid_user()
        response = self.send_post_request("/register", data=user_data)

        assert response.status_code == 400, "Expected status code 400, got {response.status_code}"
        response_data = response.json()
        assert "error" in response_data
