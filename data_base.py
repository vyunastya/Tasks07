# Работа с данными: функции на импорт и экспорт данных
def get_data(file):
    with open(f'{file}', 'r') as data:
        count = 1
        my_dict = {}
        for line in data:
            my_dict[f'entry_{count}'] = line.split()
            count += 1
    return my_dict


def export_data(my_dict):
    with open('result.txt', 'w') as data:
        for key, values in my_dict.items():
            # print(values)
            data.write(' '.join(values))
            data.write('\n')