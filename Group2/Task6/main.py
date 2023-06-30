from Collection import Collection
from Collection import CareTaker
from Validators import Validators
from User import User

collection = Collection()
caretaker = CareTaker()


def help_print():
    print("1) search")
    print("2) sort")
    print("3) add user")
    print("4) delete user")
    print("5) edit user")
    print("6) print")
    print("7) help")
    print("8) save")
    print("9) load save")
    print("10) next save")
    print("11) prev save")
    print("12) saves")
    print("13) exit")


def input_logic(usr_input):
    global collection
    user_data_list = ['age', 'birth_date', 'driver_license', 'driver_license_date', 'email', 'gender', 'id',
                      'mobile_phone', 'name']

    match usr_input:
        case "search":
            symbols = input("Enter symbols to find: ")
            collection.search_duplicates(symbols)
            return True
        case "sort":
            print("Enter what bye what field do you want to sort from this list: ")
            print(user_data_list)
            option = input()
            if option not in user_data_list:
                print("Wrong option field")
                return True
            collection.sort(option)
            return True
        case "add user":  # TODO decorators
            user_data = []
            for i in range(len(user_data_list)):
                temp = input("Enter " + user_data_list[i] + ": ")
                if i == 3:
                    if not Validators.field_check(user_data_list[i], user_data[1], temp):
                        return True
                else:
                    if not Validators.field_check(user_data_list[i], temp):
                        return True

                user_data.append(temp)
            user = User(user_data[0], user_data[1], user_data[2], user_data[3], user_data[4], user_data[5],
                        user_data[6], user_data[7], user_data[8])

            collection.add_user(user)
            return True
        case "delete user":  # TODO decorators
            print("Enter user id: ")
            usr_id = input()
            if not Validators.only_numbers_check(usr_id):
                print("Invalid input!!!")
                return True
            collection.delete_user(usr_id)
            return True
        case "edit user":  # TODO decorators
            user_id = input("Enter user id: ")
            print("Enter what you want to edit from this list: ")
            print(user_data_list)
            to_edit = input()
            if to_edit not in user_data_list:
                print("Wrong edit field")
                return True
            edited_value = input("Enter new value: ")
            if to_edit == 'driver_license_date':
                if not Validators.field_check(to_edit, collection.date_by_id(user_id), edited_value):
                    return True
                collection.edit_user(user_id, to_edit, edited_value)
            else:
                if not Validators.field_check(to_edit, edited_value):
                    return True
                collection.edit_user(user_id, to_edit, edited_value)
            return True
        case "print":
            print(collection)
            return True
        case "help":
            help_print()
            return True
        case "save":
            caretaker.add(collection)
            return True
        case "load save":
            caretaker.restore(collection)
            return True
        case "next save":
            caretaker.redo(collection)
            return True
        case "prev save":
            caretaker.undo(collection)
            return True
        case "saves":
            print(caretaker)
            return True
        case "exit":
            return False
        case _:
            print("Wrong input!!!")
            print("Try again")
            return True


def program():
    collection.read_data_from_file()

    program_continue = True

    help_print()

    while program_continue:
        option = input("Enter your choice: ")
        program_continue = input_logic(option)

    print("Thanks for using my program!")


program()
