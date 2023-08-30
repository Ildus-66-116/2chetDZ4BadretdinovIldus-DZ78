import text

def main_menu():
    for i, item in enumerate(text.menu):
        if i == 0:
            print(item)
        else:
            print(f'\t{i}. {item}')
    while True:
        choice = input(text.input_menu)
        if choice.isdigit and 0 < int(choice) < len(text.menu):
            return int(choice)
        else:
            print(text.input_menu_error)

def print_message(msg):
    print('\n' + '='*len(msg))
    print(msg)
    print('='*len(msg) + '\n')

def show_book(book: dict[int, list[str]], msg):
    if book:
        print('\n' + '*'* 87)
        for i, contact in book.items():
            print(f'{i:>3}. {contact[0]:<40} {contact[1]:<20} {contact[2]:<20}')
        print('*'* 87 + '\n')
    else:
        print_message(msg)