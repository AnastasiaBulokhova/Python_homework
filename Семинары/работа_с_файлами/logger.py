def print_contact(file_name): # функция для вывода всех контактов
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            for line in all_cont:
                print(line.strip(), end = '\n\n')
        else:
            print('Список контактов пустой')

def connect_with_user(): # спрашивает у юзера информац
    print('Введите имя, фамилию и телефон (например: Иванов Иван 89132456377): ')
    cont_info = input()
    return cont_info

def add_contact(file_name): # добавить контакт
    with open(file_name, 'r', encoding='utf8') as file:
        all_cont = file.readlines()
    new_cont = connect_with_user()
    all_cont.append('\n' + new_cont)
    with open(file_name, 'w', encoding='utf8') as file:
        file.writelines(all_cont)


def find_contact(file_name): # поиск контакта
        with open(file_name, 'r', encoding='utf8') as file:
            all_cont = file.readlines()

        print('Выберите критерий для поиска: \
            \n1 - Фамилия \
            \n2 - Имя \
            \n3 - Телефон')

        comm = int(input())
        print('Введите строку для поиска: ')
        data = input()
        print('Найденные контакты')
        for cont in all_cont:
            cont_as_list = print(list(cont.strip().split()))
            if cont_as_list[comm - 1] == data:
                print(*cont_as_list)
                all_cont.remove(cont)


def delite_contact(file_name): # удаление контакта
    with open(file_name, 'w', encoding='utf8') as file:
        all_cont = file.readlines()
        if len(all_cont) != 0:
            print('Все контакты: ')
            for line in all_cont:
                print(line.strip(), end = '\n\n')
        else:
            print('Список контактов пустой')

    print('Укажите, какой контакт вы бы хотели удалить: ')
    data = input()
    for cont in all_cont:
        cont_as_list = print(list(cont.strip().split()))
        if cont_as_list == data:
            print('Контакт удален')
            all_cont.replace(cont_as_list, ' ')
        with open(file_name, 'w', encoding='utf8') as file:
            file.writelines(all_cont)
