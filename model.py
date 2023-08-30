PATH = 'phonebook.txt'
phone_book = {}

def open_file():
    global phone_book, PATH
    with open(PATH, 'r', encoding='UTF-8') as file:
        data = file.readlines()
    for i, contact in enumerate(data,1):
        contact = contact.strip().split(';')
        phone_book[i] = contact



def save_file():
    global phone_book, PATH
    data = []
    for contact in phone_book.values():
        contact = ';'.join(contact)
        data.append(contact)
    data = '\n'.join(data)
    with open(PATH, 'w', encoding='UTF-8') as file:
        file.write(data)


def add_contact(new_contact: list[str]):
    global phone_book
    c_id = max(phone_book) + 1
    phone_book[c_id] = new_contact