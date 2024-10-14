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
    def internal_pyament_data():
        return {
            "type": "EXTERNAL",
            "category": "DOMESTIC",
            "details": {
                "associatedField": {
                    "parameters": {
                        "permitRecord": None,
                        "signatureNoCommission": False,
                        "paymentPurpose": "projection invoice polite whenever deserunt paradigms technologies Gasoline Electric Coordinator correct"
                    }
                },
                "valueDate": None,
                "knp": {
                    "code": "342",
                    "name": "Переводы клиентом денег с одного своего текущего счета, открытого в банке, на другой свой текущий счет, открытый в данном банке"
                },
                "description": "projection invoice polite whenever deserunt paradigms technologies Gasoline Electric Coordinator correct. Включая НДС 12% — 0,96 ₸. Переводы клиентом денег с одного своего текущего счета, открытого в банке, на другой свой текущий счет, открытый в данном банке",
                "payerIban": "KZ50998CTB0000977960",
                "paymentAmount": {
                    "amount": 9,
                    "currency": "KZT"
                },
                "commission": {
                    "amount": None,
                    "currency": "KZT"
                },
                "vat": True,
                "urgent": False,
                "documentId": "340510232213353581",
                "fxContract": None,
                "fxContractId": None,
                "fxContractRecipientId": None,
                "factualSender": {
                    "name": "",
                    "iinOrBin": ""
                }
            },
            "paymentRecipient": {
                "iinOrBin": "040640004843",
                "name": "Внутренний платеж",
                "kbe": {
                    "name": "17",
                    "code": "17"
                },
                "recipientAccount": {
                    "iban": "KZ048562203104859037",
                    "bankName": "АО \"Банк ЦентрКредит\"",
                    "bic": "KCJBKZKX"
                },
                "factualRecipient": {
                    "name": "",
                    "iinOrBin": ""
                },
                "countryCode": None
            }
        }
