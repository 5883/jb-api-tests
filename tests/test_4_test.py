# from enum import verify
#
# import requests
#
# from configs import base_url
#
#
# class TestClass:
#     # Установите базовый URL
#
#
#     def test_run(self):
#
#         base_url = "https://business-stream-0.jusan.kz:8460/api/v1/dictionaries/general?pageSize=300&type=PHONE_COUNTRY_CODES&sortBy=name"
#
#         # Определите заголовки
#         headers = {
#             "Authorization": "Basic d2ViYXBwOnJqWkk5TWZRT2Y=",  # Замените на ваш токен
#             "Content-Type": "application/json",  # Укажите тип контента
#             "Accept": "application/json",  # Укажите принимаемый тип данных
#             # Добавьте другие заголовки по мере необходимости
#         }
#         # Отправьте GET запрос
#         response = requests.get(base_url, headers=headers, , verify=False)
#
#         # Проверьте статус код ответа
#         if response.status_code == 200:
#             print("Запрос успешен:", response.json())
#         else:
#             print(f"Ошибка: {response.status_code}, Ответ: {response.text}")