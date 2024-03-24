def print_data(list_vacancy, top_n, from_range, to_range):
    count_vacancy = 0
    for vacancy in list_vacancy:
        # print(type(vacancy))
        if count_vacancy < top_n:
            if vacancy.get_salary() == 0:
                count_vacancy += 1
                print(
                    f'{count_vacancy}. '
                    f'Вакансия: {vacancy.get_name()}\nТребование: {vacancy.get_requirement()}\n{vacancy.get_responsibility()}'
                    f'Опыт: {vacancy.get_experience()}\n'
                    f'Зарплата: Отсутствует. Необходимо уточнить о размере зарплаты \nСсылка на вакансию: {vacancy.get_url()}\n\n')
            else:
                if vacancy.get_salary()['from'] is None:

                    if vacancy.get_salary()['to'] is None:
                        count_vacancy += 1
                        print(
                            f'{count_vacancy}. '
                            f'Вакансия: {vacancy.get_name()}\nТребование: {vacancy.get_requirement()}\n{vacancy.get_responsibility()}'
                            f'Опыт: {vacancy.get_experience()}\n'
                            f'Зарплата: от Отсутствует. Необходимо уточнить о размере зарплаты\n'
                            f'Ссылка на вакансию: {vacancy.get_url()}\n\n')
                    else:
                        if to_range >= int(vacancy.get_salary()['to']):
                            count_vacancy += 1
                            print(
                                f'{count_vacancy}. '
                                f'Вакансия: {vacancy.get_name()}\nТребование: {vacancy.get_requirement()}\n{vacancy.get_responsibility()}'
                                f'Опыт: {vacancy.get_experience()}\n'
                                f'Зарплата:  до {vacancy.get_salary()['to']} {vacancy.get_salary()['currency']}\n'
                                f'Ссылка на вакансию: {vacancy.get_url()}\n\n')
                        else:
                            continue
                            # print('Диапазон такой не найден')
                else:
                    if vacancy.get_salary()['to'] is None:
                        if to_range >= int(vacancy.get_salary()['from']):
                            count_vacancy += 1
                            print(
                                f'{count_vacancy}. '
                                f'Вакансия: {vacancy.get_name()}\nТребование: {vacancy.get_requirement()}\n{vacancy.get_responsibility()}'
                                f'Опыт: {vacancy.get_experience()}\n'
                                f'Зарплата: от {vacancy.get_salary()['from']} {vacancy.get_salary()['currency']}\n'
                                f'Ссылка на вакансию: {vacancy.get_url()}\n\n')
                        else:
                            continue
                            # print('Диапазон такой не найден')
                    else:
                        if int(vacancy.get_salary()['from']) in range(from_range, to_range) or int(
                                vacancy.get_salary()['to']) in range(from_range, to_range):
                            count_vacancy += 1
                            print(
                                f'{count_vacancy}. '
                                f'Вакансия: {vacancy.get_name()}\nТребование: {vacancy.get_requirement()}\n{vacancy.get_responsibility()}'
                                f'Опыт: {vacancy.get_experience()}\n'
                                f'Зарплата: от {vacancy.get_salary()['from']} до {vacancy.get_salary()['to']} {vacancy.get_salary()['currency']}\n'
                                f'Ссылка на вакансию: {vacancy.get_url()}\n\n')
                        else:
                            continue
                            # print('Диапазон такой не найден')
        else:
            print('Отбор закончен')
            break
