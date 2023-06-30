from List import List
from List import read_file, iterator
from colorama import Fore

work_list = List()

def help_print():
    print(Fore.CYAN + '1) strategy 1(iterator)')
    print('2) strategy 2(file reading)')
    print('3) generate list')
    print('4) pop')
    print('5) delete range')
    print('6) find at position')
    print('7) print')
    print('8) exit' + Fore.RESET)


def iterator_strategy():
    global work_list
    work_list = List(strategy=iterator)


def file_strategy():
    global work_list
    work_list = List(strategy=read_file)


def pop():
    pos = input('Enter position: ')
    if not pos.isdigit() or not pos.isdigit():
        print(Fore.RED + 'Must be integers!!!' + Fore.RESET)
        return
    work_list.pop(pos)


def list_print():
    print(work_list)


def delete_range():
    start = input('Enter start pos: ')
    end = input('Enter end pos: ')
    if not start.isdigit() or not end.isdigit():
        print(Fore.RED + 'Must be integers!!!' + Fore.RESET)
        return
    work_list.delete_range(start, end)


def generate_list():
    work_list.do_strategy()


def find_at():
    pos = input('Enter position of element to find: ')
    if not pos.isdigit() or not pos.isdigit():
        print(Fore.RED + 'Must be integers!!!' + Fore.RESET)
        return
    el = work_list.find_at(int(pos))
    print(el) if not None else print('', end='')


user_input_dict = {'1': iterator_strategy, '2': file_strategy, '3': generate_list, '4': pop, '5': delete_range,
                   '6': find_at, '7': list_print, '8': exit}

help_print()
while True:
    to_do = input('Enter what to do: ')
    if to_do not in user_input_dict:
        print('Wrong value')
        continue
    try:
        user_input_dict[to_do]()
    except TypeError:
        print(Fore.RED + 'Enter your strategy first!!!' + Fore.RESET)
    except FileNotFoundError:
        print(Fore.RED + 'File not found!!!' + Fore.RESET)
