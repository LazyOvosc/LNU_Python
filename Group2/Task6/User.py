from flask import Flask, request, jsonify, make_response
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
db = SQLAlchemy(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///emp.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


class User:
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
    # def find_symbols(self, symbols):
    #     founded = ""
    #     for el in self.__user_data_list:
    #         value = "self." + el
    #         if symbols in eval(value):
    #             founded += eval(value) + " in user id=" + self.__id + "\n"
    #
    #     return founded
    #
    # def make_list_of_fields(self):
    #     temp_list = []
    #     for el in self.__user_data_list:
    #         temp = 'self.' + el
    #         temp_list.append(eval(temp))
    #
    #     return temp_list
