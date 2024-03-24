import json
import requests
from abc import ABC, abstractmethod


class ApiAbstract(ABC):

    @abstractmethod
    def get_res_hh(self):
        pass


class HeadHunter(ApiAbstract):

    def __init__(self, url, key_word):
        self.url = url
        self.key_word = key_word
        self.headers = {'User-Agent': 'HH-User-Agent'}
        self.params = {'text': self.key_word, 'page': 0, "per_page": 100}
        self.data = []

    def get_res_hh(self):
        while self.params.get('page') != 20:
            response = requests.get(self.url, headers=self.headers, params=self.params)
            data = response.json()['items']
            self.data.extend(data)
            self.params['page'] += 1
            # print(f'222222 {data}')
            return data

    # def get_res_hh(self):
    #     res = requests.get(self.url, params={'text': self.key_word, "per_page": self.top_n})
    #     data = res.json()
    #     if len(data['items']) == 0:
    #         print("Нет вакансий")
    #     return data


class GetVacancy:

    def __init__(self, file_name):
        self.file_json = file_name

    def get_vacancy(self):
        with open(self.file_json) as file:
            data = json.load(file)
            list_data = []
            for vacancy in data:
                list_data.append(Vacancy(**vacancy))
        # print(list_data)
        return list_data


class JSONSaver:

    def __init__(self, file_json):
        self.file_json = file_json

    def save_json(self):
        list_vacancy = []
        for i in self.file_json:  # ['items']:
            pars = {'name': i['name'], 'salary': i['salary'], 'experience': i['experience']['name'],
                    'responsibility': i['snippet']['responsibility'],
                    'requirement': i['snippet']['requirement'],
                    'url': i['alternate_url']}
            list_vacancy.append(pars)
        with open('data.json', 'w', encoding='UTF-8') as file:
            json.dump(list_vacancy, file)


class Vacancy:

    def __init__(self, name, salary, experience, responsibility, requirement, url):
        self.name = name
        self.salary = salary
        self.experience = experience
        self.responsibility = responsibility
        self.requirement = requirement
        self.url = url

    def __str__(self):
        return f'{self.name}, {self.salary}, {self.experience}, {self.requirement}, {self.responsibility}'

    def get_requirement(self):
        if self.requirement is None:
            return f'требования не указаны'
        else:
            req_beg = self.requirement.replace('<highlighttext>', '')
            req_end = req_beg.replace('</highlighttext>', '')
            return req_end

    def get_responsibility(self):
        if self.responsibility is None:
            return f'требования не указаны'
        else:
            req_beg = self.responsibility.replace('<highlighttext>', '')
            req_end = req_beg.replace('</highlighttext>', '')
            return req_end

    def get_name(self):
        return self.name

    def get_experience(self):
        if self.experience == 'Нет опыта':
            return 'По договоренности'
        return self.experience

    def get_salary(self):
        if self.salary is None:
            return 0
        return self.salary

    def get_url(self):
        return self.url
