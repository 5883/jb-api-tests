import faker

class PaymentServiceData:

    @staticmethod
    def mshi_payments_data(amount):
        return {
            "category": "DOMESTIC",
            "type": "SOCIAL",
            "details": {
                "associatedField": {
                    "parameters": {
                        "signatureNoCommission": False,
                        "paymentPurpose": "назначение OSMS API tests"
                    }
                },
                "valueDate": None,
                "knp": {
                    "code": "012",
                    "name": "Обязательные социальные отчисления"
                },
                "description": "api-test-description Обязательные социальные отчисления",
                "payerIban": "KZ38998BTB0000793638",
                "paymentAmount": {
                    "amount": amount,
                    "currency": "KZT"
                },
                "commission": {
                    "amount": 0,
                    "currency": "KZT"
                },
                "urgent": False,
                "documentId": "604",
                "factualSender": {
                    "name": "",
                    "iinOrBin": ""
                }
            },
            "paymentEmployees": [
                {
                    "amount": {
                        "currency": "KZT",
                        "amount": amount
                    },
                    "birthDate": "1991-07-31",
                    "firstname": "Батыр",
                    "iin": "910731302080",
                    "lastname": "Ханболат",
                    "middlename": "",
                    "period": "2024-08-11"
                }
            ]
        }

    @staticmethod
    def delete_payment_request_by_payment_id(payment_id):
        return payment_id


