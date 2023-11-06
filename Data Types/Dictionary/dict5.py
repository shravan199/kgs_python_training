d1 = {'name': 'Suresh', 'age': 24, 89:'test', 'email_id': 'suresh@gmail.com', 
       98.89 : 'xyz', ('user_name', 'pwd'): ('suresh123', 'suresh@123'),
         89: 'test2'}

print(f'd1: {d1}')

d1_popitem_value = d1.popitem()

print(f'd1_popitem_value: {d1_popitem_value}')
d1.setdefault('address',  'It is default address')

print(f'd1: {d1}')