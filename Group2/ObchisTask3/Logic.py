from sympy import divisors
from LinkedList import LinkedList
from IterClass import IterClass
import Generator

l = LinkedList()
iterat = IterClass()
generat = Generator.generator()

def length_input():
    number_of_numbers = int(input("Enter number of friendly numbers: "))
    return number_of_numbers


def friendly_array_creating(number_of_numbers):
    i = 2
    final_list = LinkedList()

    while final_list.length < number_of_numbers:
        first_divisors = divisors(i)
        first_divisors = first_divisors[:len(first_divisors)-1]
        sum1 = sum(first_divisors)
        second_divisors = divisors(sum1)
        second_divisors = second_divisors[:len(second_divisors)-1]
        if sum(second_divisors) == i and i != sum1:
            if final_list.length != 0:
                if final_list.find_at(final_list.length-1).value[0] != sum1:
                    final_list.append([i, sum1])
            else:
                final_list.append([i, sum1])

        i += 1

    return final_list


def help_print():
    print('1) start')
    print('2) help')
    print('3) list work')
    print('4) iterator')
    print('5) generator')
    print('6) exit')


def list_help_print():
    print('1) keyboard input')
    print('2) find at')
    print('3) remove at')
    print('4) add at')
    print('5) length')
    print('6) append')
    print('7) delete list')
    print('8) print')
    print('9) help')
    print('10) exit')


def list_input_logic(value: str):
    match value:
        case 'keyboard input':
            values = [int(el) for el in input('Enter values: ').split(' ')]
            l.keyboard_input(values)
            return True
        case 'find at':
            pos = int(input('Enter position: '))
            print(l.find_at(pos))
            return True
        case 'remove at':
            pos = int(input('Enter position: '))
            l.remove_at(pos)
            return True
        case 'add at':
            pos = int(input('Enter position: '))
            value = int(input('Enter value: '))
            l.add_at(pos, value)
            return True
        case 'length':
            print(f'Length of the list is: {l.length}')
            return True
        case 'append':
            value = int(input('Enter value: '))
            l.append(value)
            return True
        case 'delete list':
            l.delete_list()
            print('List is successfully deleted!')
            return True
        case 'print':
            print(l)
            return True
        case 'help':
            list_help_print()
            return True
        case 'exit':
            return False
        case _:
            print('Wrong input!!!')
            return True


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
        case 'list work':
            list_continue = True
            list_help_print()
            while list_continue:
                list_action = input("Enter your choice: ")
                list_continue = list_input_logic(list_action)
            return True
        case 'iterator':
            length = int(input('Enter number of numbers to generate: '))
            for i in range(length):
                print(next(iterat), end=' ')
            print()
            return True
        case 'generator':
            length = int(input('Enter number of numbers to generate: '))
            for i in range(length):
                print(next(generat), end=' ')
            print()
            return True
        case 'exit':
            return False
        case _:
            print('Wring input!!!')
            return True
