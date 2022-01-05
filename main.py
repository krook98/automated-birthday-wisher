import datetime as dt
import random
import pandas
import smtplib

MY_EMAIL = {}  # feel free to enter :)
MY_PASSWORD = {}  # feel free to enter :)


today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv('birthdays.csv')
birthdays_dict = {(data_row['month'], data_row['day']): data_row for (index, data_row) in data.iterrows()}

if today_tuple in birthdays_dict:
    path = f'./letters/letter_{random.randint(1,3)}.txt'
    person = birthdays_dict[today_tuple]
    with open(path, 'r') as file:
        content = file.read()
        content = content.replace('[NAME]', person['name'])


with smtplib.SMTP('smtp.gmail.com', 587) as connection:
    connection.starttls()
    connection.login(user = MY_EMAIL, password = MY_PASSWORD)
    connection.sendmail(from_addr = MY_EMAIL, to_addrs = person['email'], msg = f'Subject: Happy Birthday!\n\n{content}')



