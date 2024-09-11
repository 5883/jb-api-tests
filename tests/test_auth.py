import pytest

from base.base_test import BaseTest


@pytest.mark.usefixtures('setup')
class TestAccount(BaseTest):

    def test_account_by_company_id(self):
        response = self.api_client.get(f'/api/v1/companies/{self.companyID}/accounts', 200)
