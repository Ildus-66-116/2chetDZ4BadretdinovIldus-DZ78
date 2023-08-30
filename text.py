menu = ['Главное меню',
        'Открыть файл',
        'Сохранить файл',
        'Показать контакты',
        'Создать контакт',
        'Найти контакт',
        'Изменить контакт',
        'Удалить контакт',
        'Выход']
input_menu = 'Выберете пункт меню: '

input_menu_error = f'Ввести нужно ЧИСЛО (от 1 до {len(menu)-1})'

load_successful = 'Телефонная книга загружена успешно!'
save_successful = 'Телефонная книга сохранена успешно!'

empty_book_error = 'Телефонная книга пуста или не открыта'

input_contact = ['Введите ФИО нового контакт: ',
                 'Введите номер телефона: ',
                 'Введите комментарий: ']

operation = ['создан', 'изменен', 'удален']

def new_contact(name: str, action: str) -> str:
    return f'Контакт {name} успешно {action}!'