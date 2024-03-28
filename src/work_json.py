import json
from src.work_vacancy import Vacancy
from abc import ABC, abstractmethod


class WorkJsonAbstract(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def __init__(self):
        pass


class WorkJson(WorkJsonAbstract):

    def __init__(self, file_json: list):
        self.file_json = file_json

    def save_json(self):
        """Выборка нужных полей и сохранение данных в файл"""
        list_vacancy = []
        for i in self.file_json:
            pars = {'name': i['name'], 'salary': i['salary'], 'experience': i['experience']['name'],
                    'responsibility': i['snippet']['responsibility'],
                    'requirement': i['snippet']['requirement'],
                    'url': i['alternate_url']}
            list_vacancy.append(pars)
        with open('data/data.json', 'w', encoding='UTF-8') as file:
            json.dump(list_vacancy, file, ensure_ascii=False)

    @staticmethod
    def get_vacancy(file) -> list:
        """Создание списка объектов вакансий из скаченных данных"""
        with open(file, encoding='UTF-8') as file:
            data = json.load(file)
            list_data = []
            for vacancy in data:
                list_data.append(Vacancy(**vacancy))
        return list_data

    def delete_vacancy(self, obj):
        """Удаление данных из файла"""
        self.file_json.remove(obj)
        with open('data/data.json', 'w', encoding='UTF-8') as file:
            json.dump(self.file_json, file, ensure_ascii=False)
