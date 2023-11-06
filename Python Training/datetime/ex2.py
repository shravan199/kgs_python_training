from datetime import datetime

date = datetime.now().strftime(r"%Y-%m-%d %H:%M:%S %p")
print(date , type(date))