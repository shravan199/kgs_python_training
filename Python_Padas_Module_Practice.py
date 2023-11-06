import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)



_4wheels = pd.Series(('car', 'zeep', 'marshal', 'scarpio'), 
                      index=['1.', '2.', '3.', '4.'])

print()
print(_4wheels)


print()
print(_4wheels['3.'])

print(_4wheels[3])

weather = {
   'Monday: Dec 19,2022' : '16 ℃',
   'Tuesday: Dec 20, 2O22' : '14.5 ℃'
}

print()
print(pd.Series(weather))