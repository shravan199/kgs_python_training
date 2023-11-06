from datetime import date, time, datetime as dt

# YYYY-MM-dd
today_date = dt.today()

print(f'Today\'s date: {today_date}, type: {type(today_date)} ')

# dd/MM/YYYY (30/10/2023)

formatted_date = today_date.strftime(format='%d/%m/%Y')
print(f'Today\'s foratted date: {formatted_date}, type: {type(formatted_date)} ')

# 30-Oct-2023

formatted_date = today_date.strftime(format='%d-%b-%Y')
print(f'Today\'s foratted date: {formatted_date}, type: {type(formatted_date)} ')


dob = dt(year= 1990, month=10, day=30)

if today_date.day == dob.day and today_date.month == dob.month:
    print(f'Happy birthday dear!. You are { today_date.year - dob.year} years old.')

