# Телефонный справочник 

# имя     телефон     комментарий


# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход

# file = open('phonebook.txt', 'w', encoding='UTF-8')
# file.close

def add_note():
    surname = input('Введите фамилию:')
    name = input('Введите имя:')
    patronymic = input('Ввыедите отчество:')
    phonenumber = input('Введите номер:')
    while not phonenumber.isdigit():
        phonenumber = input('Введите номер:')
    coment = input('Введите комментарий:')
    str = f'{surname} {name} {patronymic} {phonenumber} {coment}\n'
    with open('phonebook.txt', 'a', encoding='UTF-8') as data:
        data.write(str)

def find_note(stroka):
    with open('phonebook.txt', 'r', encoding='UTF-8') as data:
        for line in data:
            if stroka.lower() in line.lower().split():
                print(line)



while True:
    com = input('1 Выводить все контакты на экран\n2 Добавить контакт\n3 Удалить контакт\n4 Изменить контакт\n5 Найти контакт\n6 Выход\n Введите номер из меню: ')
    if com == '6':
        break
    if com == '2':
        add_note()
    if com == '1':
        find_note('')
    if com == '5':
        stroka = input('Введите запрос:')
        find_note(stroka)
