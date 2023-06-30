from User import User
import csv
from Validators import Validators
from colorama import Fore
import copy


class Memento:
    def __init__(self, collection: list):
        self.__collection = collection

    @property
    def collection(self):
        return self.__collection

    def __str__(self):
        temp = ''
        for i in range(len(self.__collection)):
            temp += self.__collection[i].__str__() + '\n'
        return temp


class Collection:
    def __init__(self, users_list: list = []):
        self.__users = users_list
        self.__user_data_list = ['age', 'birth_date', 'driver_license', 'driver_license_date', 'email', 'gender', 'id',
                                 'mobile_phone', 'name']

    def add_user(self, user: User):
        check_list = ['driver_license', 'email', 'id', 'mobile_phone']
        for us in self.__users:
            for i in range(len(check_list)):
                if eval('us.' + check_list[i]) == eval('user.' + check_list[i]):
                    exec('user.' + check_list[i] + '="invalid"')
        self.__users.append(user)
        self.__rewrite_file()

    def delete_user(self, user_id):
        for user in self.__users:
            if user.id == user_id:
                self.__users.remove(user)
                self.__rewrite_file()
                return

        print("There isn't user with this id")

    def date_by_id(self, user_id):
        for user in self.__users:
            if user.id == user_id:
                return user.birth_date

    def edit_user(self, user_id: str, to_edit: str, value: str):
        for user in self.__users:
            if user.id == user_id:
                temp = "user." + to_edit + "=" + '"' + value + '"'
                exec(temp)
                self.__rewrite_file()
                return

        print("There isn't user with this id")

    def read_data_from_file(self):   # TODO decorators
        file = open("users_data.csv")
        csvreader = csv.reader(file)
        next(csvreader)
        for row in csvreader:
            if not row:
                continue
            user = []
            for i in range(len(row)):
                if i == 3:
                    if not Validators.field_check(self.__user_data_list[i], row[1], row[i]):
                        user.append('invalid')
                        continue
                else:
                    if not Validators.field_check(self.__user_data_list[i], row[i]):
                        user.append('invalid')
                        continue
                user.append(row[i])

            self.add_user(User(*user))

        file.close()

    def __rewrite_file(self):
        file = open("users_data.csv", "w", newline='')
        writer = csv.writer(file)
        writer.writerow(self.__user_data_list)
        for user in self.__users:
            temp = user.make_list_of_fields()
            writer.writerow(temp)

        file.close()

    def search_duplicates(self, symbols: str):
        founded = ""
        for user in self.__users:
            founded += user.find_symbols(symbols)

        if len(founded) == 0:
            print("No matches")
        else:
            print(founded)

    def sort(self, field: str):
        slices = ['[:2]', '[-7:-5]', '[-4:]']
        if field == 'birth_date' or field == 'driver_license_date':
            for i in range(len(slices)):
                line = "__users.sort(key=lambda x: x." + field + slices[i] + ", reverse=False)"
                exec(line, {"__users": self.__users})
        else:
            line = "__users.sort(key=lambda x: x." + field + ", reverse=False)"
            exec(line, {"__users": self.__users})
        self.__rewrite_file()

    @property
    def list_len(self):
        return len(self.__users)

    def __str__(self):
        temp = ""
        for user in self.__users:
            temp += user.__str__() + "\n"

        return temp

    @property
    def users(self):
        return self.__users

    @users.setter
    def users(self, users):
        self.__users = copy.deepcopy(users)

    @property
    def memento(self):
        return Memento(self.__users)

    @memento.setter
    def memento(self, memento: Memento):
        self.__users = copy.deepcopy(memento.collection)


class CareTaker:
    def __init__(self):
        self.__history = []
        self.__index = 0

    def add(self, originator: Collection):

        memento = copy.deepcopy(originator.memento)
        self.__history.append(memento)
        self.__index = len(self.__history) - 1

    def restore(self, collection: Collection):
        memento = self.__history[self.__index]
        collection.memento = memento

    def undo(self, collection: Collection):
        if self.__index > 0:
            self.__index -= 1
            memento = self.__history[self.__index]
            collection.memento = memento
        else:
            print(Fore.RED + 'There are no records left' + Fore.RESET)
            return

    def redo(self, collection: Collection):
        if self.__index > len(self.__history)-2:
            print(Fore.RED + 'Newest record reached' + Fore.RESET)
        else:
            self.__index += 1
            memento = self.__history[self.__index]
            collection.memento = memento

    def __str__(self):
        temp = ''
        for i in range(len(self.__history)):
            temp += f'{i}) {self.__history[i]}'
        temp += f'\n Current index: {self.__index}'
        return temp


