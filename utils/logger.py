import logging
import json
from venv import logger


class Logger:
    """Класс для логирования запросов"""
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)

    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[logging.StreamHandler()]  # Убедитесь, что вывод направляется в консоль
    )

    @staticmethod
    def log_info(message):
        logging.info(message)

    @staticmethod
    def log_error(message):
        logging.error(message)

    @staticmethod
    def log_json_response(json_object):
        try:
            formatted_json = json.dumps(json_object, indent=4, ensure_ascii=False)
            logger.info("Ответ JSON: %s", formatted_json)
        except ValueError as e:
            logger.error("Ошибка при декодировании JSON: %s", e)

    @staticmethod
    def log_request_response(response):
        """Логи"""
        request = response.request
        logger.info(f"Метод: {request.method}")
        logger.info(f"URL: {request.url}")
        logger.info(f"Заголовки запроса: {request.headers}")
        if request.body:
            try:
                body = json.loads(request.body)
                logger.info(f"Тело запроса: {json.dumps(body, indent=4, ensure_ascii=False)}")
            except ValueError:
                logger.info(f"Тело запроса (не JSON): {request.body}")

        # Логируем данные ответа
        logger.info(f"Статус-код ответа: {response.status_code}")
        logger.info(f"Заголовки ответа: {response.headers}")
        try:
            logger.info(f"Тело ответа: {json.dumps(response.json(), indent=4, ensure_ascii=False)}")
        except ValueError:
            logger.info(f"Тело ответа (не JSON): {response.text}")
