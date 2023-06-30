import csv
import copy
from colorama import Fore


class Node:
    def __init__(self, value=None):
        self.__value = value
        self.__next = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, val):
        self.__value = val

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, val):
        self.__next = val


class List:
    def __init__(self, root: Node = None, strategy=None):
        self.__root = root
        self.__strategy = strategy

    def append(self, data):
        new_node = Node(data)
        if self.__root:
            current = self.__root
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.__root = new_node

    def pop(self, pos):
        if pos < 1:
            print(Fore.RED + "position should be >= 1." + Fore.RESET)
        elif pos == 1 and self.__root is not None:
            node_to_delete = self.__root
            self.__root = self.__root.next
            node_to_delete = None
        else:
            temp = self.__root
            for i in range(1, pos - 1):
                if temp is not None:
                    temp = temp.next
            if temp is not None and temp.next is not None:
                node_to_delete = temp.next
                temp.next = temp.next.next
                node_to_delete = None
            else:
                print(Fore.RED + "The node is already null." + Fore.RESET)

    def delete_range(self, start: int, end: int):
        while end > start:
            self.pop(start)
            end -= 1

    def find_at(self, pos: int):
        if pos < 0 or pos > self.length - 1:
            print(Fore.RED + 'Wrong index' + Fore.RESET)
            return None
        temp = self.__root
        for i in range(pos):
            temp = temp.next

        return temp.value

    def do_strategy(self):
        temp_list = self.__strategy()
        self.__root = temp_list

    def __str__(self):
        current = self.__root
        temp = ''
        while current is not None:
            temp += f'{current.value} '
            current = current.next
        return temp

    @property
    def strategy(self):
        return self.__strategy

    @property
    def root(self):
        return self.__root

    @root.setter
    def root(self, val):
        self.__root = val

    @property
    def length(self):
        count = 0
        temp_linked = copy.deepcopy(self.__root)
        while temp_linked:
            count += 1
            temp_linked = temp_linked.next
        return count


def read_file():
    l = List()
    file_name = input(Fore.GREEN + 'Enter file name: ' + Fore.RESET)
    with open(file_name) as file:
        csvreader = csv.reader(file)
        for row in csvreader:
            for el in row:
                l.append(el)
    return l.root


def iterator():
    length = int(input(Fore.GREEN + 'Enter length of the list: ' + Fore.RESET))
    l = []
    linked = List()
    for i in range(length):
        val = input(Fore.GREEN + "Enter value: " + Fore.RESET)
        l.append(val)
    it = iter(l)
    for i in range(len(l)):
        linked.append(next(it))
    return linked.root
