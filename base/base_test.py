from socket import send_fds

import pytest
import pydash
from client.api_сlient import APIClient
from services.auth_service import AuthService
import configs
from utils.assert_utils import AssertUtils
from utils.json_utils import *

@pytest.mark.usefixtures("setup")
class BaseTest:
    access_token = None
    api_client = None
    companyID = None
    assert_utils = None
    response_body = None
    payment_id = None

    @pytest.fixture(scope='class', autouse=True)
    def setup(self, request):
        self.assert_utils = AssertUtils()
        auth_service = AuthService()
        login = auth_service.login()
        self.access_token = login.get("access_token")
        userAuthorities = JsonUtils.get_value_by_path(login, 'user.userAuthorities')
        userAuth = self.get_user_auth_by_bin(userAuthorities, configs.bin)

        if self.companyID is None and userAuth is not None:
            self.companyID = userAuth.get('companyId')

        if self.access_token:
            self.api_client = APIClient(self.access_token)
        else:
            raise Exception("Отсутствует access_token. APIClient не может быть инициализирован.")

        request.cls.auth_service = auth_service
        request.cls.access_token = self.access_token
        request.cls.api_client = self.api_client
        request.cls.companyID = self.companyID
        request.cls.assert_utils = self.assert_utils

    def get_access_token(self):
        return self.access_token

    @staticmethod
    def get_user_auth_by_bin(user_authorities, bin):
        """Ищем userAuthority по BIN компании"""
        for user_authority in user_authorities:
            company = user_authority.get('company', {})
            if company.get('bin') == bin:
                return user_authority
        return None
