from datetime import date

#YYYY-MM-dd
today_date  = date.today()
print(f'Today\'s date : {today_date}')

employee_dob = []

dob = date(2023, 10, 30)
print(dob)
# dd/mm/YYYY
formatted_date = today_date.strftime(format='%d-%b-%Y')
print(f'formatted today\'s date : {formatted_date}')

if (today_date == dob):
    print('Happy birtdhday dear!')
