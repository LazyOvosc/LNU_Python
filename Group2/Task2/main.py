import numpy as np
from colorama import Fore


def help_print():
    print("1) Draw matrix")
    print("2) Help")
    print("2) Exit")


def input_logic(input_value):
    match input_value:
        case "Draw matrix":
            n = input_number()
            diagonal = diagonal_making(n)
            array = array_creating(n, diagonal)
            print(array)
            return True
        case "Help":
            help_print()
            return True
        case "Exit":
            return False
        case _:
            print(Fore.RED + "Wrong input!!!" + Fore.RESET)
            return True


def input_number():
    n = int(input("Enter size of matrix: "))

    while n % 2 != 0:
        print(Fore.RED + "Wrong input!!! Number must be equal!!!" + Fore.RESET)
        n = int(input("Enter size of matrix: "))

    return n


def diagonal_making(n):
    diagonal = []
    for i in range(n):
        diagonal.append(n - i)

    return diagonal


def array_creating(n, diagonal):
    array = np.zeros((n, n), dtype=int)

    np.fill_diagonal(array, diagonal)
    diagonal.reverse()
    np.fill_diagonal(np.fliplr(array), diagonal)

    return array


def program():
    program_continue = True
    help_print()
    while program_continue:
        value = input("Enter your choice: ")
        program_continue = input_logic(value)


program()
