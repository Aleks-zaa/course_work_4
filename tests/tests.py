import pytest
from src.classes import Vacancy, GetVacancy, HeadHunter, JSONSaver


@pytest.fixture
def test_hh():
    return HeadHunter('https://hh.ru/vacancy/94781222', 'Бухгалтер')


@pytest.fixture
def test_get_class_vacancy():
    return GetVacancy('test_data.json')


@pytest.fixture
def test_json_save():
    return JSONSaver('test_data.json')


@pytest.fixture
def test_vacancy():
    return Vacancy('Бухгалтер', 10000, 'От 3 до 6 лет', 'общение с клиентами',
                   'навыки работы в программе 1С',
                   'https://hh.ru/vacancy/94781222')


@pytest.fixture
def test_list_vacancy():
    pass


def test_init_hh(test_hh):
    assert test_hh.key_word == 'Бухгалтер'


def test_init_get_vacancy(test_get_class_vacancy):
    assert test_get_class_vacancy.file_json == 'test_data.json'


def test_init_json_save(test_json_save):
    assert test_json_save.file_json == 'test_data.json'


def test_init_vacancy(test_vacancy):
    assert test_vacancy.name == 'Бухгалтер'
    assert test_vacancy.salary == 10000
    assert test_vacancy.experience == 'От 3 до 6 лет'
    assert test_vacancy.responsibility == 'общение с клиентами'
    assert test_vacancy.requirement == 'навыки работы в программе 1С'
    assert test_vacancy.url == 'https://hh.ru/vacancy/94781222'


def test_get_requirement():
    sorted_vacancies = GetVacancy('test_data.json')
    vacancy = sorted_vacancies.get_vacancy()[0]
    assert vacancy.get_requirement() == (f'Знание бухгалтерского и налогового учета. Опыт работ от 3-х лет. '
                                         f'Сертификаты проф бухгалтера и другие будут преимуществом.')


def test_get_responsibility():
    sorted_vacancies = GetVacancy('test_data.json')
    vacancy = sorted_vacancies.get_vacancy()[0]
    assert vacancy.get_responsibility() == (f'Осуществлять хозяйственные операции '
                                            f'(реализация услуг, расчеты с поставщиками, движение денежных'
                                            f' средств и др). '
                                            f'Выполнять работу по ведению бухгалтерского учета обязательств...')


def test_get_name():
    sorted_vacancies = GetVacancy('test_data.json')
    vacancy = sorted_vacancies.get_vacancy()[0]
    assert vacancy.get_name() == 'Бухгалтер'


def test_get_experience():
    sorted_vacancies = GetVacancy('test_data.json')
    vacancy = sorted_vacancies.get_vacancy()[0]
    assert vacancy.get_experience() == 'От 3 до 6 лет'


def test_get_salary():
    sorted_vacancies = GetVacancy('test_data.json')
    vacancy = sorted_vacancies.get_vacancy()[0]
    assert vacancy.get_salary() == {'currency': 'KZT', 'from': 400000, 'gross': False, 'to': 500000}


def test_get_url():
    sorted_vacancies = GetVacancy('test_data.json')
    vacancy = sorted_vacancies.get_vacancy()[0]
    assert vacancy.get_url() == 'https://hh.ru/vacancy/94286367'


def test_get_vacancy():
    sorted_vacancies = GetVacancy('test_data.json')
    a = sorted_vacancies.get_vacancy()[0]
    assert str(a) == ("Бухгалтер, {'from': 400000, 'to': 500000, 'currency': 'KZT', 'gross': "
                      'False}, От 3 до 6 лет, Знание бухгалтерского и налогового учета. Опыт работ '
                      'от 3-х лет. Сертификаты проф <highlighttext>бухгалтера</highlighttext> и '
                      'другие будут преимуществом., Осуществлять хозяйственные операции (реализация '
                      'услуг, расчеты с поставщиками, движение денежных средств и др). Выполнять '
                      'работу по ведению бухгалтерского учета обязательств...')
