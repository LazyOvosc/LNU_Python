letter_dict = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
field = [[' ' for x in range(8)] for y in range(8)]
queen = 'q'
rook = 'r'
knight = 'k'
queen_position = []
rook_position = []
knight_position = []


def field_print():
    for i in range(len(field)):
        print(field[i])


def figure_positions():
    global queen_position, rook_position, knight_position
    figure_position = input("Enter figure positions: ")
    queen_position = (8-int(figure_position[1]), letter_dict[figure_position[0]])
    rook_position = (8-int(figure_position[4]), letter_dict[figure_position[3]])
    knight_position = (8-int(figure_position[7]), letter_dict[figure_position[6]])
    field[queen_position[0]][queen_position[1]] = 'q'
    field[rook_position[0]][rook_position[1]] = 'r'
    field[knight_position[0]][knight_position[1]] = 'k'


def queen_diagonal(i: int, queen_beats: list):
    if queen_position[0] + i < 8 and queen_position[1] + i < 8:
        queen_beats.append((queen_position[0] + i, queen_position[1] + i))
    if queen_position[0] + i < 8 and queen_position[1] - i > -1:
        queen_beats.append((queen_position[0] + i, queen_position[1] - i))
    if queen_position[0] - i > -1 and queen_position[1] + i < 8:
        queen_beats.append((queen_position[0] - i, queen_position[1] + i))
    if queen_position[0] - i > -1 and queen_position[1] - i > -1:
        queen_beats.append((queen_position[0] - i, queen_position[1] - i))

    return queen_beats


def remove_positions(list_of_fields: list):
    if queen_position in list_of_fields:
        list_of_fields.remove(queen_position)
    if rook_position in list_of_fields:
        list_of_fields.remove(rook_position)
    if knight_position in list_of_fields:
        list_of_fields.remove(knight_position)

    return list_of_fields


def queen_rook_move():
    queen_beats = []
    rook_beats = []
    for i in range(8):
        queen_beats.append((i, queen_position[1]))
        queen_beats.append((queen_position[0], i))
        rook_beats.append((i, rook_position[1]))
        rook_beats.append((rook_position[0], i))
        queen_beats = queen_diagonal(i, queen_beats)

    queen_beats.extend(rook_beats)

    return queen_beats


def knight_aftermove(pos: int, knight_beats: list, indicator: int = 1):
    first = (knight_position[pos] - 1, knight_position[1-pos] + indicator*2)
    second = (knight_position[pos] + 1, knight_position[1-pos] + indicator*2)
    if pos == 1:
        first = (first[1], first[0])
        second = (second[1], second[0])

    if knight_position[pos] + 1 > 7:
        knight_beats.append(first)
    elif knight_position[pos] - 1 < 0:
        knight_beats.append(second)
    else:
        knight_beats.append(first)
        knight_beats.append(second)

    return knight_beats


def knight_move():
    knight_beats = []
    if knight_position[1] + 2 < 8:
        knight_beats = knight_aftermove(0, knight_beats)
    if knight_position[1] - 2 > -1:
        knight_beats = knight_aftermove(0, knight_beats, -1)
    if knight_position[0] + 2 < 8:
        knight_beats = knight_aftermove(1, knight_beats)
    if knight_position[0] - 2 > -1:
        knight_beats = knight_aftermove(1, knight_beats, -1)

    return knight_beats


def summary_moves():
    queen_rook_moves = queen_rook_move()
    knight_moves = knight_move()
    queen_rook_moves.extend(knight_moves)
    queen_rook_moves = list(dict.fromkeys(queen_rook_moves))
    queen_rook_moves = remove_positions(queen_rook_moves)

    return queen_rook_moves


def field_paint():
    for el in summary_moves():
        field[el[0]][el[1]] = '*'


def help_print():
    print('1) start')
    print('2) help')
    print('3) exit')


def input_logic(value: str):
    match value:
        case 'start':
            figure_positions()
            field_paint()
            field_print()
            print(summary_moves())
            print(len(summary_moves()))
            return True
        case 'help':
            help_print()
            return True
        case 'exit':
            return False
        case _:
            print('Wrong input!!!')
            return True
