from Matrix import Matrix

m = Matrix()


def matrix_input(matrix: Matrix):
    return_matrix = []
    for i in range(matrix.length):
        temp_matrix = [int(el) for el in input(f'Enter {i+1} row: ').split()]
        return_matrix.append(temp_matrix)

    return return_matrix


def help_print():
    print('1) keyboard input')
    print('2) print')
    print('3) add')
    print('4) subtract')
    print('5) multiply')
    print('6) divide')
    print('7) transpose')
    print('8) inverse')
    print('9) solve')
    print('10) eig')
    print('11) vectors')
    print('12) norm')
    print('13) iter')
    print('14) spiral iter')
    print('15) help')
    print('16) exit')
    return True

def keyboard_input():
    m.keyboard_input()
    return True


def matrix_print():
    print(m)
    return True


def add():
    matrix = matrix_input(m)
    print(m.add(matrix))
    return True


def subtract():
    matrix = matrix_input(m)
    print(m.subtract(matrix))
    return True


def multiply():
    matrix = matrix_input(m)
    print(m.multiply(matrix))
    return True


def divide():
    matrix = matrix_input(m)
    print(m.divide(matrix))
    return True


def inverse():
    print(m.inverse())
    return True


def transpose():
    print(m.transpose())
    return True


def eig():
    print(m.eig())
    return True


def norm():
    print(m.norm())
    return True


def vectors():
    print(m.vectors())
    return True


def solve():
    equals = [int(el) for el in input('Enter equals: ').split()]
    print(m.solve(equals))
    return True


def iteration():
    it = iter(m)
    for it in m:
        print(it, end=' ')
    print()
    return True


def spiral_iter():
    for i in m.spiral_iter():
        print(i, end=' ')
    print()
    return True


def exit_():
    return False


actions = {'keyboard input': keyboard_input, 'print': matrix_print, 'add': add, 'subtract': subtract,
           'multiply': multiply, 'divide': divide, 'inverse': inverse, 'transpose': transpose,
           'eig': eig, 'norm': norm, 'vectors': vectors, 'solve': solve, 'iter': iteration,
           'spiral iter': spiral_iter, 'help': help_print, 'exit': exit_}


def input_logic(value: str):
    if value not in actions.keys():
        print('Wrong input!!!')
        return True
    return_value = actions[value]()
    return return_value


def program():
    program_continue = True
    help_print()

    while program_continue:
        value = input('Enter what to do: ')
        program_continue = input_logic(value)


program()
