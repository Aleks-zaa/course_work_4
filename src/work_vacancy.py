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

    def __lt__(self, other):
        if isinstance(other, int):
            if self.salary.get('to') is None:
                return self.salary.get('from') < other
            elif self.salary.get('from') is None:
                return self.salary.get('to') < other
        raise ValueError

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

    # def like_salary(self, from_range, to_range):
    #     """Сравнение сумм зарплат"""
    #
    #     if to_range >= self.salary['to']:
    #         return 'to1'
    #     elif to_range >= self.salary['from']:
    #         return 'to2'
    #     elif (self.salary['from'] in range(from_range, to_range)
    #           or self.salary['to'] in range(from_range, to_range)):
    #         return 'all'


