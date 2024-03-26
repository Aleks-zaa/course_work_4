import json
import requests
from abc import ABC, abstractmethod


class ApiAbstract(ABC):
    """Абстрактный класс получения данных с HH"""

    @abstractmethod
    def get_res_hh(self):
        pass


class HeadHunter(ApiAbstract):

    def __init__(self, url: str, key_word: str):
        self.__url = url
        self.key_word = key_word
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': self.key_word, 'page': 0, "per_page": 100}
        self.data = []

    def get_res_hh(self):
        """Получение данных с HH"""
        while self.params.get('page') != 20:
            response = requests.get(self.__url, headers=self.headers, params=self.params)
            data = response.json()['items']
            self.data.extend(data)
            self.params['page'] += 1
            return data


class GetFileAbstract(ABC):
    """Абстрактный класс"""

    @abstractmethod
    def get_vacancy(self):
        pass


class GetVacancy(GetFileAbstract):
    """Абстрактный класс работы с файлом"""

    def __init__(self, file_name: str):
        self.file_json = file_name

    def get_vacancy(self) -> list:
        """Создание списка объектов вакансий из скаченных данных"""
        with open(self.file_json) as file:
            data = json.load(file)
            list_data = []
            for vacancy in data:
                list_data.append(Vacancy(**vacancy))
        return list_data


class JSONSaver:

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
            json.dump(list_vacancy, file)

    def delete_vacancy(self, obj):
        """Удаление данных из файла"""
        self.file_json.remove(obj)
        with open('data/data.json', 'w', encoding='UTF-8') as file:
            json.dump(self.file_json, file)


class Vacancy:
    """Класс вакансии"""
    __slots__ = ('name', 'salary', 'experience', 'responsibility', 'requirement', 'url')

    def __init__(self, name: str, salary: dict, experience: str, responsibility: str, requirement: str, url: str):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.responsibility = responsibility
        self.requirement = requirement
        self.url = url

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.experience}, {self.requirement}, {self.responsibility}'

    def get_requirement(self) -> str:
        """Проверка на заполнение и избавление от <highlighttext>"""
        if self.requirement is None:
            return 'требования не указаны'
        else:
            req_beg = self.requirement.replace('<highlighttext>', '')
            req_end = req_beg.replace('</highlighttext>', '')
            return req_end

    def get_responsibility(self) -> str:
        """Проверка на заполнение и избавление от <highlighttext>"""
        if self.responsibility is None:
            return 'требования не указаны'
        else:
            req_beg = self.responsibility.replace('<highlighttext>', '')
            req_end = req_beg.replace('</highlighttext>', '')
            return req_end

    def get_name(self) -> str:
        """Возвращаем имя"""
        return self.name

    def get_experience(self) -> str:
        """Проверка на наличие или отсутствие, возвращаем то, что заполнено автором или 'По договоренности' """
        if self.experience == 'Нет опыта':
            return 'По договоренности'
        return self.experience

    def get_salary(self) -> dict:
        """Проверка на наличие или отсутствие, если нет, то 0 или возвращаем зп"""
        if self.salary is None:
            return 0
        return self.salary

    def get_url(self) -> str:
        """Возвращаем ссылку"""
        return self.url
