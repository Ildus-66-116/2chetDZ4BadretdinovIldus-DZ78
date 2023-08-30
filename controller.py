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
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                break