# from src.classes import GetVacancy, JSONSaver, HeadHunter
from src.work_api import HeadHunter
from src.work_json import WorkJson

from src.utils import print_data


def main():
    search_query = input('Введите поисковый запрос: \n')
    salary_range = input("Введите диапазон зарплат через пробел: ")
    top_n = int(input("Введите количество вакансий для вывода в топ N: \n"))
    list_range = salary_range.split(' ')
    from_range = int(list_range[0])
    to_range = int(list_range[1])
    hh = HeadHunter('https://api.hh.ru/vacancies', search_query)
    data_hh = hh.get_res_hh()
    # print(data_hh)
    res_from_hh = WorkJson(data_hh)
    res_from_hh.save_json()
    # sorted_vacancies = GetVacancy('data/data.json')
    list_vacancy = res_from_hh.get_vacancy('data/data.json')
    print_data(list_vacancy, top_n, from_range, to_range)


if __name__ == '__main__':
    main()
