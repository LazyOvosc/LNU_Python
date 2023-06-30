import random as rand


class ArrayWithSearch:
    def __init__(self):
        self.__array = []

    def user_input(self):
        arr = [int(el) for el in input('Enter your array: ').split(' ')]
        self.__array = self.__bubble_sort(arr)

    def random_input(self):
        size = int(input('Enter size of array: '))
        minimum = int(input('Enter min: '))
        maximum = int(input('Enter max: '))
        arr = []
        for i in range(size):
            arr.append(rand.randint(minimum, maximum))

        self.__array = self.__bubble_sort(arr)

    @staticmethod
    def __bubble_sort(arr: list):
        swapped = False
        number_of_checks = 0
        for i in range(len(arr)-1):
            for j in range(len(arr)-i-1):
                if arr[j] > arr[j+1]:
                    number_of_checks += 1
                    swapped = True
                    arr[j], arr[j+1] = arr[j+1], arr[j]

            if not swapped:
                print(f'Number of checks: {number_of_checks}')
                return arr

        print(f'Number of checks: {number_of_checks}')
        return arr

    def binary_search(self):
        num = int(input('Enter number to find: '))
        bottom = 0
        top = len(self.__array) - 1
        while bottom <= top:
            middle = bottom + (top - bottom)//2

            if self.__array[middle] == num:
                print(f'Position of the {num} is {middle}')
                return
            elif self.__array[middle] < num:
                bottom = middle + 1
            else:
                top = middle - 1

        print(f'Element {num} is not found')

    def __str__(self):
        temp = ''
        for el in self.__array:
            temp += str(el) + ' '

        return temp
