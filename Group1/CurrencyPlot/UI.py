import tkinter as tk
import Data
import Mathematics
from datetime import date

start_date = date(1, 1, 1)
end_date = date(1, 1, 1)
delta = 0
delta_predict = 0
start_date_str = ""
end_date_str = ""

root = tk.Tk()
root.geometry("300x300")
root.title(" Currency Predict ")


def input_length_restriction(value):
    max_date_length = 2
    max_month_length = 2
    max_year_length = 4

    if len(date_input_start.get("1.0", "end-1c")) > max_date_length:
        date_input_start.delete('end-2c')
    if len(month_input_start.get("1.0", "end-1c")) > max_month_length:
        month_input_start.delete('end-2c')
    if len(year_input_start.get("1.0", "end-1c")) > max_year_length:
        year_input_start.delete('end-2c')
    if len(date_input_end.get("1.0", "end-1c")) > max_date_length:
        date_input_end.delete('end-2c')
    if len(month_input_end.get("1.0", "end-1c")) > max_date_length:
        month_input_end.delete('end-2c')
    if len(year_input_end.get("1.0", "end-1c")) > max_year_length:
        year_input_end.delete('end-2c')
    if len(date_input_predict.get("1.0", "end-1c")) > max_date_length:
        date_input_predict.delete('end-2c')
    if len(month_input_predict.get("1.0", "end-1c")) > max_month_length:
        month_input_predict.delete('end-2c')
    if len(year_input_predict.get("1.0", "end-1c")) > max_year_length:
        year_input_predict.delete('end-2c')


def correct_input_date():
    if int(year_input_end.get("1.0", "end-1c")) < int(year_input_start.get("1.0", "end-1c")):
        error_label.config(text="Wrong input!! Check if your data is correct")
        return False
    else:
        if int(month_input_end.get("1.0", "end-1c")) < int(
                month_input_start.get("1.0", "end-1c")) and year_input_end.get("1.0", "end-1c") == \
                year_input_start.get("1.0", "end-1c"):
            error_label.config(text="Wrong input!! Check if your data is correct")
            return False
        else:
            if int(date_input_end.get("1.0", "end-1c")) < int(
                    date_input_start.get("1.0", "end-1c")) and \
                    year_input_end.get("1.0","end-1c") == year_input_start.get("1.0", "end-1c") \
                    and month_input_end.get("1.0", "end-1c") == month_input_start.get("1.0", "end-1c"):
                error_label.config(text="Wrong input!! Check if your data is correct")
                return False

    return True


def correct_input_predict():
    if int(year_input_predict.get("1.0", "end-1c")) < int(year_input_end.get("1.0", "end-1c")):
        error_label.config(text="Wrong input!! Check if your data is correct")
        return False
    else:
        if int(month_input_predict.get("1.0", "end-1c")) < \
                int(month_input_end.get("1.0", "end-1c")) \
                and year_input_predict.get("1.0", "end-1c") == year_input_end.get("1.0", "end-1c"):
            error_label.config(text="Wrong input!! Check if your data is correct")
            return False
        else:
            if int(date_input_predict.get("1.0", "end-1c")) < int(
                    date_input_end.get("1.0", "end-1c")) \
                    and year_input_predict.get("1.0", "end-1c") == year_input_end.get(
                "1.0", "end-1c") \
                    and month_input_predict.get("1.0", "end-1c") == month_input_end.get("1.0", "end-1c"):
                error_label.config(text="Wrong input!! Check if your data is correct")
                return False

    return True


def set_delta(predict):
    global delta, delta_predict
    start_date = date(int(year_input_start.get("1.0", "end-1c")), int(month_input_start.get("1.0", "end-1c")),
                      int(date_input_start.get("1.0", "end-1c")))
    end_date = date(int(year_input_end.get("1.0", "end-1c")), int(month_input_end.get("1.0", "end-1c")),
                    int(date_input_end.get("1.0", "end-1c")))
    delta = end_date - start_date

    if predict:
        start_date = date(int(year_input_start.get("1.0", "end-1c")), int(month_input_start.get("1.0", "end-1c")),
                          int(date_input_start.get("1.0", "end-1c")))
        end_date = date(int(year_input_predict.get("1.0", "end-1c")), int(month_input_predict.get("1.0", "end-1c")),
                        int(date_input_predict.get("1.0", "end-1c")))
        delta_predict = end_date - start_date


def button_logic():
    global start_date, end_date, delta, start_date_str, end_date_str

    sdate = date_input_start.get("1.0", "end-1c")
    smonth = month_input_start.get("1.0", "end-1c")
    syear = year_input_start.get("1.0", "end-1c")
    edate = date_input_end.get("1.0", "end-1c")
    emonth = month_input_end.get("1.0", "end-1c")
    eyear = year_input_end.get("1.0", "end-1c")


    if not sdate.isnumeric() or not smonth.isnumeric() or not syear.isnumeric() \
            or not edate.isnumeric() or not emonth.isnumeric() or not eyear.isnumeric():
        error_label.config(text="Wrong input!! Check if your data is correct")
        return

    if not correct_input_date():
        return

    error_label.config(text="")

    set_delta(False)

    start_date_str = date_input_start.get("1.0", "end-1c") + "." + month_input_start.get("1.0", "end-1c") + "." + \
                     year_input_start.get("1.0", "end-1c")
    end_date_str = date_input_end.get("1.0", "end-1c") + "." + month_input_end.get("1.0", "end-1c") + "." + \
                   year_input_end.get("1.0", "end-1c")

    Data.data_print(start_date_str, end_date_str)


def predict_button_logic():
    if not date_input_start.get("1.0", "end-1c").isnumeric() \
            or not month_input_start.get("1.0", "end-1c").isnumeric() \
            or not year_input_start.get("1.0", "end-1c").isnumeric() \
            or not date_input_end.get("1.0", "end-1c").isnumeric() \
            or not month_input_end.get("1.0", "end-1c").isnumeric() \
            or not year_input_end.get("1.0", "end-1c").isnumeric() \
            or not date_input_predict.get("1.0", "end-1c").isnumeric() \
            or not month_input_predict.get("1.0", "end-1c").isnumeric() \
            or not year_input_predict.get("1.0", "end-1c").isnumeric():
        error_label.config(text="Wrong input!! Check if your data is correct")
        return
    if not correct_input_date():
        return
    if not correct_input_predict():
        return
    set_delta(True)
    error_label.config(text="")
    start_date_str = date_input_start.get("1.0", "end-1c") + "." + month_input_start.get("1.0", "end-1c") + "." + \
                     year_input_start.get("1.0", "end-1c")
    end_date_str = date_input_end.get("1.0", "end-1c") + "." + month_input_end.get("1.0", "end-1c") + \
                   "." + year_input_end.get("1.0", "end-1c")
    Data.write_to_file(start_date_str, end_date_str)
    prediction = Mathematics.predicts(delta_predict.days + 1)
    usd_prediction = "USD: " + str(prediction[0])
    eur_prediction = "EUR: " + str(prediction[1])

    predict_window = tk.Toplevel(root)
    predict_label_text = tk.Label(predict_window, text="Prediction:")
    predict_label_text.grid(row=0, column=0)
    tk.Label(predict_window, text=usd_prediction).grid(row=1, column=0)
    tk.Label(predict_window, text=eur_prediction).grid(row=2, column=0)


tk.Label(root, text="Start of period").grid(row=0, column=0)
tk.Label(root, text="Date").grid(row=1, column=0)
tk.Label(root, text="Month").grid(row=1, column=1)
tk.Label(root, text="Year").grid(row=1, column=2)
tk.Label(root, text="End of period").grid(row=3, column=0)
tk.Label(root, text="Date").grid(row=4, column=0)
tk.Label(root, text="Month").grid(row=4, column=1)
tk.Label(root, text="Year").grid(row=4, column=2)

date_input_start = tk.Text(root, height=1, width=2, bg="light yellow")
date_input_start.grid(row=2, column=0)
date_input_start.bind('<KeyRelease>', input_length_restriction)
date_input_end = tk.Text(root, height=1, width=2, bg="light yellow")
date_input_end.grid(row=5, column=0)
date_input_end.bind('<KeyRelease>', input_length_restriction)

month_input_start = tk.Text(root, height=1, width=2, bg="light yellow")
month_input_start.grid(row=2, column=1)
month_input_start.bind('<KeyRelease>', input_length_restriction)
month_input_end = tk.Text(root, height=1, width=2, bg="light yellow")
month_input_end.grid(row=5, column=1)
month_input_end.bind('<KeyRelease>', input_length_restriction)

year_input_start = tk.Text(root, height=1, width=4, bg="light yellow")
year_input_start.grid(row=2, column=2)
year_input_start.bind('<KeyRelease>', input_length_restriction)
year_input_end = tk.Text(root, height=1, width=4, bg="light yellow")
year_input_end.grid(row=5, column=2)
year_input_end.bind('<KeyRelease>', input_length_restriction)

graph_build_button = tk.Button(root, text="Build Graph", height=1, command=button_logic)

tk.Label().grid(row=6)
error_label = tk.Label()
error_label.grid(row=7, columnspan=100)
graph_build_button.grid(row=8, column=0)

predict_button = tk.Button(root, text="Predict", height=1, command=predict_button_logic)
predict_button.grid(row=8, column=1)
tk.Label(root, text="Predict date").grid(row=9, column=0)

tk.Label(root, text="Date").grid(row=10, column=0)
tk.Label(root, text="Month").grid(row=10, column=1)
tk.Label(root, text="Year").grid(row=10, column=2)

date_input_predict = tk.Text(root, height=1, width=2, bg="light yellow")
date_input_predict.grid(row=11, column=0)
date_input_predict.bind('<KeyRelease>', input_length_restriction)
month_input_predict = tk.Text(root, height=1, width=2, bg="light yellow")
month_input_predict.grid(row=11, column=1)
month_input_predict.bind('<KeyRelease>', input_length_restriction)
year_input_predict = tk.Text(root, height=1, width=4, bg="light yellow")
year_input_predict.grid(row=11, column=2)
year_input_predict.bind('<KeyRelease>', input_length_restriction)


root.mainloop()