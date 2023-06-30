import csv
from Validators import Validators
from colorama import Fore
import copy
from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///usr.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    age = db.Column(db.String(80), nullable=False)
    birth_date = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(80), nullable=False)
    mobile_phone = db.Column(db.String(80), nullable=False)
    gender = db.Column(db.String(80), nullable=False)
    driver_license = db.Column(db.String(80), nullable=False)
    driver_license_date = db.Column(db.String(80), nullable=False)

    def __repr__(self):
        return f"{self.id} - {self.name} - {self.age} - {self.birth_date} - {self.email} - {self.mobile_phone} - " \
               f"{self.driver_license} - {self.driver_license_date}"

# class Memento:
#     def __init__(self, collection: list):
#         self.__collection = collection
#
#     @property
#     def collection(self):
#         return self.__collection
#
#     def __str__(self):
#         temp = ''
#         for i in range(len(self.__collection)):
#             temp += self.__collection[i].__str__() + '\n'
#         return temp


class Collection(Resource):
    class Add(Resource):
        def post(self):
            if request.is_json:
                usr = User(name=request.json['Name'], age=request.json['Age'],
                           birth_date=request.json['Birth date'], email=request.json['Email'],
                           mobile_phone=request.json['Mobile phone'], gender=request.json['Gender'],
                           driver_license=request.json['Driver license'],
                           driver_license_date=request.json['Driver license date'])
                db.session.add(usr)
                db.session.commit()
                # return a json response
                return make_response(jsonify({'Id': usr.id, 'Name': usr.name, 'Age': usr.age,
                                              'Birth date': usr.birth_date, 'Email': usr.email,
                                              'Mobile phone': usr.mobile_phone, 'Gender': usr.gender,
                                              'Driver license': usr.driver_license,
                                              'Driver license date': usr.driver_license_date}), 201)
            else:
                return {'error': 'Request must be JSON'}, 400

    class Get(Resource):
        def get(self):
            users = User.query.all()
            usr_list = []
            for usr in users:
                usr_data = {'Id': usr.id, 'Name': usr.name, 'Age': usr.age, 'Birth date': usr.birth_date,
                            'Email': usr.email, 'Mobile phone': usr.mobile_phone, 'Gender': usr.gender,
                            'Driver license': usr.driver_license, 'Driver license date': usr.driver_license_date}
                usr_list.append(usr_data)
            return {"Employees": usr_list}, 200

    # def delete_user(self, user_id):
    #     for user in self.__users:
    #         if user.id == user_id:
    #             self.__users.remove(user)
    #             self.__rewrite_file()
    #             return
    #
    #     print("There isn't user with this id")
    #
    # def date_by_id(self, user_id):
    #     for user in self.__users:
    #         if user.id == user_id:
    #             return user.birth_date
    #
    # def edit_user(self, user_id: str, to_edit: str, value: str):
    #     for user in self.__users:
    #         if user.id == user_id:
    #             temp = "user." + to_edit + "=" + '"' + value + '"'
    #             exec(temp)
    #             self.__rewrite_file()
    #             return
    #
    #     print("There isn't user with this id")
    #
    # def read_data_from_file(self):   # TODO decorators
    #     file = open("users_data.csv")
    #     csvreader = csv.reader(file)
    #     next(csvreader)
    #     for row in csvreader:
    #         if not row:
    #             continue
    #         user = []
    #         for i in range(len(row)):
    #             if i == 3:
    #                 if not Validators.field_check(self.__user_data_list[i], row[1], row[i]):
    #                     user.append('invalid')
    #                     continue
    #             else:
    #                 if not Validators.field_check(self.__user_data_list[i], row[i]):
    #                     user.append('invalid')
    #                     continue
    #             user.append(row[i])
    #
    #         self.add_user(User(*user))
    #
    #     file.close()
    #
    # def __rewrite_file(self):
    #     file = open("users_data.csv", "w", newline='')
    #     writer = csv.writer(file)
    #     writer.writerow(self.__user_data_list)
    #     for user in self.__users:
    #         temp = user.make_list_of_fields()
    #         writer.writerow(temp)
    #
    #     file.close()
    #
    # def search_duplicates(self, symbols: str):
    #     founded = ""
    #     for user in self.__users:
    #         founded += user.find_symbols(symbols)
    #
    #     if len(founded) == 0:
    #         print("No matches")
    #     else:
    #         print(founded)
    #
    # def sort(self, field: str):
    #     slices = ['[:2]', '[-7:-5]', '[-4:]']
    #     if field == 'birth_date' or field == 'driver_license_date':
    #         for i in range(len(slices)):
    #             line = "__users.sort(key=lambda x: x." + field + slices[i] + ", reverse=False)"
    #             exec(line, {"__users": self.__users})
    #     else:
    #         line = "__users.sort(key=lambda x: x." + field + ", reverse=False)"
    #         exec(line, {"__users": self.__users})
    #     self.__rewrite_file()
    #
    # @property
    # def list_len(self):
    #     return len(self.__users)
    #
    # def __str__(self):
    #     temp = ""
    #     for user in self.__users:
    #         temp += user.__str__() + "\n"
    #
    #     return temp

    # @property
    # def users(self):
    #     return self.__users

    # @users.setter
    # def users(self, users):
    #     self.__users = copy.deepcopy(users)

    # @property
    # def memento(self):
    #     return Memento(self.__users)

    # @memento.setter
    # def memento(self, memento: Memento):
    #     self.__users = copy.deepcopy(memento.collection)


# class CareTaker:
#     def __init__(self):
#         self.__history = []
#         self.__index = 0
#         self.__list_of_indexes = [0]
#
#     def add(self, originator: Collection):
#
#         memento = copy.deepcopy(originator.memento)
#         self.__history.append(memento)
#         self.__index = len(self.__history) - 1
#
#     def restore(self, collection: Collection):
#         memento = self.__history[self.__index]
#         collection.memento = memento
#
#     def undo(self, collection: Collection):
#         if self.__index > 0:
#             self.__index -= 1
#             memento = self.__history[self.__index]
#             collection.memento = memento
#         else:
#             print(Fore.RED + 'There are no records left' + Fore.RESET)
#             return
#
#     def redo(self, collection: Collection):
#         if self.__index > len(self.__history)-2:
#             print(Fore.RED + 'Newest record reached' + Fore.RESET)
#         else:
#             self.__index += 1
#             memento = self.__history[self.__index]
#             collection.memento = memento
#
#     def __str__(self):
#         temp = ''
#         for i in range(len(self.__history)):
#             temp += f'{i}) {self.__history[i]}'
#         temp += f'\n Current index: {self.__index}'
#         return temp

api.add_resource(Collection.Get, '/')
api.add_resource(Collection.Get, '/')

if __name__ == '__main__':
    app.run(debug=True)
