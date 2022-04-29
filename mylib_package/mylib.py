import pandas as pd
import datetime
import requests

currencyname = input("Please choose the currency: USD, EUR or BTC: ")
date = input('Enter a date in YYYY-MM-DD format: ')
todaydate = datetime.datetime.strptime(date, "%Y-%m-%d").date()

url_privat = f'https://minfin.com.ua/company/privatbank/currency/{todaydate}/'
url_nbu = f'https://minfin.com.ua/currency/nbu/{todaydate}/'

r_privat = requests.get(url_privat)
r_nbu = requests.get(url_nbu)

df_privat = pd.read_html(r_privat.text)[0]
df_nbu = pd.read_html(r_nbu.text)[1]


def result():
    df_priv_chage = df_privat.rename(columns={'Покупка': 'Rate', 'Валюта': 'Currency'})
    df_nbu_chage = df_nbu.rename(columns={'Курс': 'Rate', 'Валюта': 'Currency'})
    df_nbu_res = df_nbu_chage.loc[df_nbu_chage['Currency'] == currencyname, ['Currency', 'Rate']]
    df_priv_res = df_priv_chage.loc[df_priv_chage['Currency'] == currencyname, ['Currency', 'Rate']]
    print(f"NBU rate:\n{df_nbu_res}")
    print(f"PrivatBank rate:\n{df_priv_res}")


if __name__ == '__main__':
    result()
