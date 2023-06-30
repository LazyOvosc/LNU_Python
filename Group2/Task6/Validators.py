from colorama import Fore


class Validators:
    @staticmethod
    def smart_email(func):
        def inner(mail: str):
            res = func(mail)
            if not res:
                print(Fore.CYAN + 'Main must end with @gmail.com')
            return res
        return inner

    @staticmethod
    @smart_email
    def email_check(mail: str):
        if len(mail) < 11:
            return False
        if mail[len(mail) - 10:] != "@gmail.com":
            return False

        return True

    @staticmethod
    def smart_only_letters(func):
        def inner(to_check: str):
            res = func(to_check)
            if not res:
                print(Fore.CYAN + 'Unexpected symbols' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_only_letters
    def only_letters_check(to_check: str):
        return to_check.isalpha()

    @staticmethod
    def smart_only_first_uppercase(func):
        def inner(to_check: str):
            res = func(to_check)
            if not res:
                print(Fore.CYAN + 'First letter is not uppercase' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_only_first_uppercase
    def only_first_uppercase_check(to_check: str):
        return to_check.istitle()

    @staticmethod
    def smart_name(func):
        def inner(name: str):
            res = func(name)
            if not res:
                print(Fore.CYAN + 'First letter is not capital or unexpected symbol' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_name
    def name_check(name: str):
        if not Validators.only_letters_check(name):
            return False
        if not Validators.only_first_uppercase_check(name):
            return False

        return True

    @staticmethod
    def smart_age(func):
        def inner(age: str):
            res = func(age)
            if not res:
                print(Fore.CYAN + 'To big/small age or unexpected literals' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_age
    def age_check(age: str):
        if not Validators.only_numbers_check(age):
            return False

        if int(age) < 0 or int(age) > 119:
            return False

        return True

    @staticmethod
    def smart_only_numbers(func):
        def inner(to_check: str):
            res = func(to_check)
            if not res:
                print(Fore.CYAN + 'Unexpected literals' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_only_numbers
    def only_numbers_check(to_check: str):
        return to_check.isdigit()

    @staticmethod
    def smart_gender(func):
        def inner(gender: str):
            res = func(gender)
            if not res:
                print(Fore.CYAN + 'Non existing gender' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_gender
    def gender_check(gender: str):
        if gender != "male" and gender != "female":
            return False

        return True

    @staticmethod
    def smart_date(func):
        def inner(date: str):
            res = func(date)
            if not res:
                print(Fore.CYAN + 'Wrong date format or unexpected literals' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_date
    def date_check(date: str):
        if len(date) != 10:
            return False

        year = date[-4:]
        month = date[-7:-5]
        day = date[:2]

        if not Validators.only_numbers_check(year):
            return False
        if not Validators.only_numbers_check(month):
            return False
        if not Validators.only_numbers_check(day):
            return False

        if date[2] != "." or date[5] != ".":
            return False

        if int(year) > 2022 or int(year) < 1920:
            return False
        if int(month) < 1 or int(month) > 12:
            return False
        if int(day) > 31 or int(day) < 1:
            return False

        if 13 > int(month) > 6:
            if int(month) % 2 == 0 and int(day) > 31:
                return False
            if int(month) % 2 == 1 and int(day) > 30:
                return False
        else:
            if int(month) == 2 and int(year) % 4 == 0 and int(day) > 29:
                return False
            elif int(month) == 2 and int(year) % 4 != 0 and int(day) > 28:
                return False
            if int(month) % 2 == 0 and int(day) > 30:
                return False
            if int(month) % 2 == 1 and int(day) > 31:
                return False

        return True

    @staticmethod
    def smart_license_date(func):
        def inner(date: str, license_date: str):
            res = func(date, license_date)
            if not res:
                print(Fore.CYAN + 'Wrong date format, unexpected literals or age gap < 16' + Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_license_date
    def license_date_check(date: str, license_date: str):
        if not Validators.date_check(date) or not Validators.date_check(license_date):
            return False
        date_year = int(date[-4:])
        date_month = int(date[-7:-5])
        date_day = int(date[:2])
        license_date_year = int(license_date[-4:])
        license_date_month = int(license_date[-7:-5])
        license_date_day = int(license_date[:2])
        if license_date_year < date_year:
            return False
        if license_date_year - date_year == 16:
            if license_date_month == date_month:
                if license_date_day == date_day:
                    return True
                elif license_date_day - date_day > 0:
                    return True
                else:
                    return False
            elif license_date_month - date_month > 0:
                return True
        elif license_date_year - date_year > 16:
            return True
        return False

    @staticmethod
    def smart_mobile_phone(func):
        def inner(mobile_phone: str):
            res = func(mobile_phone)
            if not res:
                print(Fore.CYAN + 'Missing "+", unexpected characters or wrong length' +  Fore.RESET)
            return res
        return inner

    @staticmethod
    @smart_mobile_phone
    def mobile_phone_check(mobile_phone: str):
        if mobile_phone[0] != "+" or len(mobile_phone) != 13 or not Validators.only_numbers_check(mobile_phone[1:]):
            return False
        return True

    @staticmethod
    def smart_field(func):
        def inner(field: str, option: str, license_date: str = ''):
            res = func(field, option, license_date)
            if not res:
                print(Fore.RED + f'Wrong field: {option}' + Fore.RESET)
                print('-------------------------------------------------------------')
            return res
        return inner

    @staticmethod
    @smart_field
    def field_check(field: str, option: str, license_date: str = ''):
        check_dir = {'id': Validators.only_numbers_check, 'name': Validators.name_check,
                     'age': Validators.age_check, 'birth_date': Validators.date_check,
                     'email': Validators.email_check, 'mobile_phone': Validators.mobile_phone_check,
                     'gender': Validators.gender_check, 'driver_license': Validators.only_numbers_check,
                     'driver_license_date': Validators.license_date_check}

        if field == 'driver_license_date':
            return check_dir[field](option, license_date)
        return check_dir[field](option)




