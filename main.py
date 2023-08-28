# Телефонный справочник 

# имя     телефон     комментарий


# выводить все контакты на экран
# добавить контакт
# удалить контакт
# изменить контакт
# найти контакт
# открыть или сохранить
# выход


# def add_note():
#     surname = input('Введите фамилию:')
#     name = input('Введите имя:')
#     patronymic = input('Ввыедите отчество:')
#     phonenumber = input('Введите номер:')
#     coment = input('Введите комментарий:')
#     str = f'{surname} {name} {patronymic} {phonenumber} {coment}\n'
#     with open('phonebook.txt', 'a', encoding='UTF-8') as data:
#         data.write(str)

# def find_note(str):
#     with open('phonebook.txt', 'r', encoding='UTF-8') as data:
#         for line in data:
#             if str.lower() in line.lower().split():
#                 print(line)

# def delete_note(str):
#     lst = []
#     with open('phonebook.txt', 'r', encoding='UTF-8') as data:
#         lst = data.readlines()
#         for line in range(len(lst)):
#             if str.lower() in lst[line].lower().split():
#                 lst[line] = ''
#     with open('phonebook.txt', 'w', encoding='UTF-8') as data:
#         for i in lst:
#             data.write(i)

# def edit_note(str):
#     delete_note(str)
#     add_note()

# def read_all():
#     with open('phonebook.txt', 'r', encoding='UTF-8') as data:
#         for line in data:
#             print(line[:-1])

# com = ''
# while com != '6':
#     com = input('1 Выводить все контакты на экран\n2 Добавить контакт\n3 Удалить контакт\n4 Изменить контакт\n5 Найти контакт\n6 Выход\n Введите номер из меню: ')
#     if com == '2':
#         add_note()
#     if com == '1':
#         read_all()
#     if com == '5':
#         str = input('Введите запрос:')
#         find_note(str)
#     if com == '3':
#         str = input('Введите запрос:')
#         delete_note(str)
#     if com == '4':
#         str = input('Введите запрос:')
#         edit_note(str)

# Модульный вариант:
