import requests
import pprint
import json

DOMAIN = 'https://api.hh.ru/'
url_vacancies = f'{DOMAIN}vacancies'

# Создаем словарь с параметрами поиска
params = {
    'text': 'Развитие продаж (1 OR Активные продажи) AND (Управление продажами OR CRM)',
    'page': 1,
    'area': 1,  # Идентификатор региона (например, Москва)
    'per_page': 100,  # Количество вакансий на странице
}

# Отправляем запрос к API и получаем результаты поиска
result = requests.get(url_vacancies, params=params).json()

pprint.pprint(result)


with open('vacancies.json', 'w') as f:
    json.dump(result, f)
