from ArrayWithSearch import ArrayWithSearch


array = ArrayWithSearch()


def help_print():
    print('1) array by hand')
    print('2) random array')
    print('3) search')
    print('4) print array')
    print('5) help')
    print('6) exit')


def input_logic(value: str):
    match value:
        case 'array by hand':
            array.user_input()
            return True
        case 'random array':
            array.random_input()
            return True
        case 'search':
            array.binary_search()
            return True
        case 'print array':
            print(array)
            return True
        case 'help':
            help_print()
            return True
        case 'exit':
            return False
        case _:
            print('Wrong input!!!')
            return True


def program():
    program_continue = True
    help_print()
    while program_continue:
        value = input("Enter your choice: ")
        program_continue = input_logic(value)


program()
