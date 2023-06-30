import csv
import sys
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


matplotlib.use('TkAgg')


def write_to_file(start_date, end_date):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    url = "https://asviobank.ua/usi-kursi.html?begin_date=" + start_date + "&end_date=" + end_date + \
              "&submit=%D0%97%D0%B0%D0%BF%D1%80%D0%BE%D1%81"
    driver.get(url)

    writing = []
    elems = driver.find_elements(By.TAG_NAME, "tr")
    for elem in elems:
        day = elem.find_element(By.XPATH, "./td[1]").text
        usd = elem.find_element(By.XPATH, "./td[2]").text
        eur = elem.find_element(By.XPATH, "./td[3]").text
        writing.append([day, usd, eur])

    driver.quit()

    writing = writing[1:]
    writing.reverse()

    with open('CurrencyFile.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Usd', 'Eur'])
        for i in range(len(writing)):
            writer.writerow([writing[i][0], float(writing[i][1]), float(writing[i][2])])

    return


def data_print(start_date, end_date):
    plt.close()
    write_to_file(start_date, end_date)

    df = pd.read_csv('CurrencyFile.csv')
    df.plot(x='Date')

    plt.show()

    plt.savefig(sys.stdout.buffer)
    sys.stdout.flush()

