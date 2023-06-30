import numpy as np
import copy


class Matrix:
    def __init__(self):
        self.__matrix = None
        self.__length = None
        self.__width = None

    @property
    def length(self):
        return self.__length

    @property
    def width(self):
        return self.__width

    @property
    def matrix(self):
        return self.__matrix

    def __iter__(self):
        for i in range(self.__length):
            for j in range(self.__width):
                yield self.__matrix[i][j]

    def spiral_iter(self):
        matrix = copy.copy(self.__matrix)
        while matrix:
            temp = list(matrix.pop(0))
            for i in range(len(temp)):
                yield temp[i]
            matrix = [*zip(*matrix)][::-1]

    def keyboard_input(self):
        matrix = []
        length = int(input('Enter length of the matrix: '))
        for i in range(length):
            temp_array = [int(el) for el in input(f'Enter {i+1} row: ').split()]
            matrix.append(temp_array)
        self.__matrix = matrix
        self.__length = len(matrix)
        self.__width = len(matrix[0])

    def add(self, matrix):
        return np.add(self.__matrix, matrix)

    def multiply(self, matrix):
        return np.multiply(self.__matrix, matrix)

    def subtract(self, matrix):
        return np.subtract(self.__matrix, matrix)

    def divide(self, matrix):
        return np.divide(self.__matrix, matrix)

    def inverse(self):
        return np.invert(self.__matrix)

    def transpose(self):
        return np.transpose(self.__matrix)

    def solve(self, equals: list):
        if len(self.__matrix) != len(self.__matrix[0]) or len(self.__matrix) != len(equals):
            print('Cannot solve!!!')
            return
        return np.linalg.solve(self.__matrix, equals)

    def eig(self):
        return np.linalg.eig(self.__matrix)

    def norm(self):
        return np.linalg.norm(self.__matrix)

    def vectors(self):
        return np.linalg.eigh(self.__matrix)[1]

    def __str__(self):
        temp = ''
        for i in range(self.__length):
            for j in range(self.__width):
                temp = temp + str(self.__matrix[i][j]) + ' '
            temp = temp + '\n'

        return temp
