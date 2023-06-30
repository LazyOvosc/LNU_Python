import Logic


def program():
    program_continue = True
    Logic.help_print()
    while program_continue:
        value = input("Enter your choice: ")
        program_continue = Logic.input_logic(value)


program()

