from colorama import Fore


class User:
    def __init__(self,
                 age: str,
                 birth_date: str,
                 driver_license: str,
                 driver_license_date: str,
                 email: str,
                 gender: str,
                 usr_id: str,
                 mobile_phone: str,
                 name: str,
                 ):
        self.__id = usr_id
        self.__name = name
        self.__age = age
        self.__birth_date = birth_date
        self.__email = email
        self.__mobile_phone = mobile_phone
        self.__gender = gender
        self.__driver_license = driver_license
        self.__driver_license_date = driver_license_date
        self.__user_data_list = [el[7:] for el in dir(self) if el not in dir(User)]
        self.__number_of_fields = len(self.__user_data_list)

    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, value: str):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value: str):
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value: str):
        self.__age = value
        
    @property
    def birth_date(self):
        return self.__birth_date

    @birth_date.setter
    def birth_date(self, value: str):
        self.__birth_date = value
    
    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value: str):
        self.email = value
        
    @property
    def mobile_phone(self):
        return self.__mobile_phone

    @mobile_phone.setter
    def mobile_phone(self, value: str):
        self.__mobile_phone = value
        
    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value: str):
        self.__gender = value

    @property
    def driver_license(self):
        return self.__driver_license

    @driver_license.setter
    def driver_license(self, value: str):
        self.__driver_license = value

    @property
    def driver_license_date(self):
        return self.__driver_license_date

    @driver_license_date.setter
    def driver_license_date(self, value: str):
        self.__driver_license_date = value

    def __str__(self):
        temp = ""
        for i in range(self.__number_of_fields):
            line = "'" + self.__user_data_list[i] + ": '+" + "self." + self.__user_data_list[i] + "+'| '"
            if i == self.__number_of_fields-1:
                line = line[:-5]
            invalid_check = eval("self." + self.__user_data_list[i])
            if invalid_check == 'invalid':
                temp += Fore.RED + eval(line)[:-2] + Fore.RESET + '| '
            else:
                temp += eval(line)

        return temp

    def find_symbols(self, symbols):
        founded = ""
        for el in self.__user_data_list:
            value = "self." + el
            if symbols in eval(value):
                founded += eval(value) + " in user id=" + self.__id + "\n"

        return founded

    def make_list_of_fields(self):
        temp_list = []
        for el in self.__user_data_list:
            temp = 'self.' + el
            temp_list.append(eval(temp))

        return temp_list
