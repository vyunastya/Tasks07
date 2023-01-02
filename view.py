# Запрос информации и вывод информации на экран
def get_name_file():
    name_file = input('Введите полное название файла: ')
    return name_file


def get_find_contact():
    check = input('Нужен поиск данных (да/нет)? ').lower()
    if check == 'да':
        while True:
            field_to_find = input('Введите параметр поиска (Имя, Фамилия, Номер телефона): ')
            field_to_find = field_to_find.lower()
            match field_to_find:
                case 'имя':
                    number_field = 0
                    break
                case 'фамилия':
                    number_field = 1
                    break
                case 'номер телефона':
                    number_field = 2
                    break
                case _1:
                    print('Введена некорректная информация!')
        data_to_find = input('Введите данные для поиска: ').capitalize()
        return (number_field, data_to_find)
    elif check == 'нет':
        return (-1,)
    else:
        print('Не корректный формат ответа')
        return (-2,)


def get_add_contact():
    check = input('Нужно добавление данных (да/нет)? ').lower()
    if check == 'да':
        return 1
    elif check == 'нет':
        return 0
    else:
        print('Не корректный формат ответа')
        return -1


def get_change_contact():
    check = input('Нужно изменение данных (да/нет)? ').lower()
    if check == 'да':
        return 1
    elif check == 'нет':
        return 0
    else:
        print('Не корректный формат ответа')
        return -1

def get_del_contact():
    check = input('Нужно удалить данные (да/нет)? ').lower()
    if check == 'да':
        return 1
    elif check == 'нет':
        return 0
    else:
        print('Не корректный формат ответа')
        return -1