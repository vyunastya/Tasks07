from data_base import get_data, export_data
from view import get_name_file, get_find_contact, get_add_contact, get_change_contact, get_del_contact
from user_func import find_contact, add_contact, change_contact, del_contact

def notebook():
    while True:
        try:
            notebook_dict = get_data(get_name_file())
            break
        except:
            print('Неверное название файла')
    print(notebook_dict)

    find_tuple = get_find_contact()
    while find_tuple != (-1,):
        while find_tuple == (-2,):
            find_tuple = get_find_contact()
        if find_tuple == (-1,):
            break
        find_contact(find_tuple, notebook_dict)
        find_tuple = get_find_contact()
    print(notebook_dict)

    check_add = get_add_contact()
    count=0
    while check_add != 0:
        while check_add == -1:
            check_add = get_add_contact()
        if check_add == 0:
            break
        notebook_dict = add_contact(notebook_dict,count)
        count+=1
        check_add = get_add_contact()

    print(notebook_dict)

    check_change = get_change_contact()
    while check_change != 0:
        while check_change == -1:
            check_change = get_change_contact()
        if check_change == 0:
            break
        notebook_dict = change_contact(notebook_dict)
        check_change = get_change_contact()

    print(notebook_dict)
#

    check_del = get_del_contact()
    while check_del != 0:
        while check_del == -1:
            check_del = get_del_contact()
        if check_del == 0:
            break
        notebook_dict = del_contact(notebook_dict)
        check_del = get_del_contact()
    print(notebook_dict)

    export_data(notebook_dict)
