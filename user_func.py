# Все функции:

# цикл на добавление
# цикл на изменение
# цикл на удаление
#
def find_contact(find_tuple, find_dict):
    flag = False
    for key, values in find_dict.items():
        if values[find_tuple[0]] == find_tuple[1]:
            print(*values)
            flag = True
    if not flag:
        print('Контакт не найден')

def add_contact(add_dict,i):
    add_dict[f'add_{i}']=list(input('Добавление контакта: ').split())
    return add_dict

def change_contact(original_dict):
    flag = False
    contact_for_change = input('Введите имя и фамилию контакта, который надо изменить: ').split()
    for key, values in original_dict.items():
        if values[0] == contact_for_change[0] and values[1] == contact_for_change[1]:
            while True:
                try:
                    number = int(input('Что надо изменить: имя (1), фамилию (2) или номер (3). Выберите цифру: ')) - 1
                    if 0<=number<=2:
                        break
                    else:
                        print('Неверное значение')
                except:
                    print('Неверное значение')
            new_data = input('Введите новое значение: ')
            original_dict[key][number] = new_data
            flag = True
    if not flag:
        print('Контакт не найден')
    return original_dict

def del_contact(original_dict):
    contact_for_change = input('Введите имя и фамилию контакта, который надо удалить: ').split()
    for key, values in original_dict.items():
        if values[0] == contact_for_change[0] and values[1] == contact_for_change[1]:
            original_dict.pop(key)
            break
    else:
        print('Контакт не найден')
    return original_dict