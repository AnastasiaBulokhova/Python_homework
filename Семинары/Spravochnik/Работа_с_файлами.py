

from logger import *

Contact = 'Семинары\\Spravochnik\\Contact.txt'

def interface():
    while True:
        print('Выберете действие:\
            \n 1 - Добавить контакт \
            \n 2 - Вывести все контакты \
            \n 3 - Найти контакт \
            \n 0- Выйти')

        command = int(input())
        match command:
            case 0:
                break
            case 1:
                add_contact(Contact)
            case 2:
                print_contact(Contact)
            case 3:
                find_contact(Contact)
            case _:
                print('Неверная команда')

if __name__ == '__main__':
    interface()

