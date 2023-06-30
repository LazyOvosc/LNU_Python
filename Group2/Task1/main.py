from sympy import divisors

final_array = []


def length_input():
    number_of_numbers = int(input("Enter number of friendly numbers: "))
    return number_of_numbers


def friendly_array_creating(number_of_numbers):
    i = 2

    while len(final_array) < number_of_numbers:
        first_divisors = divisors(i)
        first_divisors = first_divisors[:len(first_divisors) - 1]
        sum1 = sum(first_divisors)
        second_divisors = divisors(sum1)
        second_divisors = second_divisors[:len(second_divisors) - 1]
        if sum(second_divisors) == i and i != sum1:
            if len(final_array) != 0:
                if final_array[len(final_array) - 1][0] != sum1:
                    final_array.append([i, sum1])
            else:
                final_array.append([i, sum1])

        i += 1

    return final_array


def help_print():
    print('1) start')
    print('2) help')
    print('3) exit')


def input_logic(value):
    match value:
        case 'start':
            length = length_input()
            array = friendly_array_creating(length)
            print(array)
            return True
        case 'help':
            help_print()
            return True
        case 'exit':
            return False
        case _:
            print('Wring input!!!')
            return True


def program():
    program_continue = True
    help_print()
    while program_continue:
        value = input("Enter your choice: ")
        program_continue = input_logic(value)


program()
