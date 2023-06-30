import csv


def line(currency_array):
    ei2 = float(len(currency_array) * (len(currency_array) + 1) * (2 * len(currency_array) + 1)) / 6
    ei = float(len(currency_array) + 1) / 2 * len(currency_array)
    ey = 0
    eiy = 0
    for i in range(len(currency_array)):
        ey += currency_array[i]
        eiy += currency_array[i] * (i + 1)

    arr = [[ei2, ei, eiy], [ei, len(currency_array), ey]]
    final_numbers = []

    x = float(arr[1][0] / arr[0][0])
    arr[0] = [element * x for element in arr[0]]
    for j in range(len(arr[0])):
        arr[0][j] = arr[0][j] - arr[1][j]
    final_numbers.append(float(arr[0][2] / arr[0][1]))
    final_numbers.append((arr[1][2] - arr[1][1] * final_numbers[0]) / arr[1][0])
    final_numbers.reverse()

    return final_numbers


def predicts(day_to_predict):
    file = open("CurrencyFile.csv")
    data = csv.reader(file)

    row_counter = 0

    usd_arr = []
    eur_arr = []
    next(data)
    for row in data:
        usd_arr.append(float(row[1]))
        eur_arr.append(float(row[2]))
        row_counter += 1

    usd = line(usd_arr)
    eur = line(eur_arr)

    predict = [usd[0] * day_to_predict + usd[1], eur[0] * day_to_predict + eur[1]]

    return predict