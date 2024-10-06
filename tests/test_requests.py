from unittest import skipIf
import pytest
import configs
from base.base_test import BaseTest
from utils.assert_utils import AssertUtils
from utils.json_utils import JsonUtils
from data.payment_data import PaymentServiceData


@pytest.mark.usefixtures('setup')
class TestAccount(BaseTest):

    @skipIf(configs.bin == "040640004843", reason="скипул тест потому что данный тест относится к компания типа ИП") # для примера, если есть необходимость скипнуть тест по какому-то признаку
    def test_get_request(self):
        self.responseBody = self.api_client.get(f'/api/v1/companies/{self.companyID}/accounts')
        JsonUtils.validate_json_schema(self.responseBody, "get_account_response_schema.json")

    @pytest.mark.parametrize("amount", [1, 2, 3]) # пример параметризированных тестов, данный тест запустится 3 раза со значениями amount: 1, 2, 3
    def test_post_request(self, amount):
        self.responseBody = self.api_client.post(
            endpoint=f'/api/v1/companies/{self.companyID}/payments',
            json=PaymentServiceData.mshi_payments_data(amount)
        )
        JsonUtils.validate_json_schema(self.responseBody, "create_domestic_payment_response.json")
        self.payment_id = JsonUtils.get_value_by_path(self.responseBody, 'id')

    def test_delete_request(self):
        self.responseBody = self.api_client.delete(
            endpoint=f'/api/v1/companies/{self.companyID}/payments',
            json=JsonUtils.string_to_list(self.payment_id),
            status_code=200
        )
        AssertUtils.assert_json_equal(self.responseBody, JsonUtils.string_to_list(self.payment_id))
