import argparse
import os
import re
import json
import importlib
import ensurepip

try:
    requests = importlib.import_module('requests')
except ImportError:
    ensurepip.bootstrap(upgrade=True)
    import subprocess

    subprocess.check_call(["pip3", "install", "requests"])
    requests = importlib.import_module('requests')

parser = argparse.ArgumentParser(
    description='Скрипт для подготовки XML-файлов JUnit для Zephyr Scale и загрузки в API Zephyr')
parser.add_argument('-f', '--filename', required=True,
                    help='Имя XML-файла, который будет создан и загружен в Zephyr Scale')
parser.add_argument('-p', '--project', required=True, help='Ключ проекта в Jira (например, JBVED)')
parser.add_argument('-c', '--testcycle', required=True, help='Наименование тестового цикла')
parser.add_argument('-t', '--token', required=True,
                    help='Для авторизации используется токен API Zephyr')
parser.add_argument('-a', '--auto', default='FALSE',
                    help='Автоматически создавать тест кейсы, если они не существуют (по умолчанию FALSE)')
args = parser.parse_args()

xmlDir = os.getcwd()

print(f'Поиск файла {xmlDir}')
xmlFiles = []
for filename in os.listdir(xmlDir):
    if filename.endswith('.xml'):
        print(f'Найден файл: {filename}')
        xmlFiles.append(os.path.join(xmlDir, filename))

if not xmlFiles:
    print("Файл не загружен")
    exit(1)

apiUrl = f'https://api.zephyrscale.smartbear.com/v2/automations/executions/junit?projectKey={args.project}&autoCreateTestCases=true'

headers = {'Authorization': f'Bearer {args.token}'}

print('Загрузка в Zephyr')
for xmlFile in xmlFiles:
    with open(xmlFile, 'rb') as file:
        requestBody = {
            "testCycle": (None, json.dumps({'name': f'{args.testcycle}'}), "application/json"),
            "file": (os.path.basename(xmlFile), file, "application/xml")
        }

        response = requests.post(apiUrl, headers=headers, files=requestBody)

        if response.status_code == requests.codes.ok:
            print(f'Загрузка {xmlFile} прошла успешно')
            print(response.text)
        else:
            print(f'Загрузка не удалась {xmlFile} со статусом {response.status_code}')
            print(response.text)
            exit(1)
