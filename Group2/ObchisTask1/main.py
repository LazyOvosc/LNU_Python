import LogicAndUI


def program():
    program_continue = True
    LogicAndUI.help_print()
    while program_continue:
        value = input("Enter your choice: ")
        program_continue = LogicAndUI.input_logic(value)


program()