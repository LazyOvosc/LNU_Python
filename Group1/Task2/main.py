import csv


class Route:
    def __init__(self, start_station, end_station, number_of_stops, length):
        self.start_station = start_station
        self.end_station = end_station
        self.number_of_stops = number_of_stops
        self.length = int(length)

    def __str__(self):
        return self.start_station + self.end_station + self.number_of_stops + ' ' + str(self.length)


route_array = []

certain_stop_array = []


def print_route(array):
    for route in array:
        print(route)


def read_data():
    global route_array
    file = open("Objects.csv")
    data = csv.reader(file)
    next(data)

    for row in data:
        temp = Route(row[0], row[1], row[2], row[3])
        route_array.append(temp)


def sort_array():
    global route_array
    route_array.sort(key=lambda x: x.length, reverse=True)
    print_route(route_array)


def avg_length():
    global route_array
    print("Enter avg number:")
    x = int(input())
    print("avg < list:")
    for route in route_array:
        if float(route.length)/float(route.number_of_stops) < x:
            print(route)


def certain_array_create():
    global route_array, certain_stop_array
    print("Enter stop name:")
    station_exist = False
    temp = input()
    for route in route_array:
        if route.start_station == temp:
            certain_stop_array.append(route)
            station_exist = True

    if station_exist:
        print_route(certain_stop_array)
    else:
        print("No such name")


def max_stops_output():
    global route_array
    print("Routes with max length")
    max_el = max(route_array, key=lambda x: x.length).length
    for route in route_array:
        if route.length == max_el:
            print(route)


read_data()
sort_array()
avg_length()
certain_array_create()
max_stops_output()
