import model
import text
import view

def start():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:
                model.open_file()
                view.print_message(text.load_successful)
            case 2:
                model.save_file()
                view.print_message(text.save_successful)
            case 3:
                view.show_book(model.phone_book, text.empty_book_error)
            case 4:
                new_contact = view.input_contact(text.input_contact)
                model.add_contact(new_contact)
                view.print_message(text.new_contact(new_contact[0], text.operation[0]))
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break