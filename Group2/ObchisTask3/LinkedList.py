class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def get_data(self):
        return self.value

    def set_data(self, value):
        self.value = value

    def get_next(self):
        return self.next

    def set_next(self, value):
        self.next = value


class LinkedList:
    def __init__(self, root: Node = None):
        self.__root = root
        self.__length = 0

    @property
    def length(self):
        return self.__length

    def append(self, data):
        new_node = Node(data)
        if self.__root:
            current = self.__root
            while current.next:
                current = current.next
            current.next = new_node
            self.__length += 1
        else:
            self.__root = new_node
            self.__length += 1

    def keyboard_input(self, values: list):
        self.delete_list()
        for i in range(len(values)):
            self.append(values[i])

    def delete_list(self):
        while self.__root is not None:
            temp = self.__root
            self.__root = self.__root.next
            temp = None

    def remove_at(self, value):
        current = self.__root
        iterator = 0
        if iterator == value:
            self.__root = current.next
            self.__length -= 1
        else:
            while current:
                if iterator == value:
                    break
                prev = current
                current = current.next
                iterator += 1
            if current is None:
                print(f'{value} is not found')
                return

            prev.next = current.next
            current = None
            self.__length -= 1

    def add_at(self, pos, value):
        new_node = Node(value)
        if pos < 0 or pos > self.__length:
            print(f'Wrong position')
        elif pos == 0:
            new_node.next = self.__root
            self.__root = new_node
            self.__length += 1
        else:
            temp = self.__root
            for i in range(pos-1):
                if temp is not None:
                    temp = temp.next

            if temp is not None:
                new_node.next = temp.next
                temp.next = new_node
                self.__length += 1
            else:
                print('Previous node is invalid')

    def find_at(self, pos: int):
        if pos < 0 or pos > self.__length-1:
            print('Wrong index')
            return
        temp = self.__root
        for i in range(pos):
            temp = temp.next

        return temp

    def __str__(self):
        current = self.__root
        temp = ''
        while current is not None:
            temp += f'{current.get_data()} '
            current = current.next
        return temp