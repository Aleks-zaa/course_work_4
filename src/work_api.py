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
