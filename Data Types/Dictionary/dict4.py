d1 = {'name': 'Suresh', 'age': 24, 89:'test', 'email_id': 'suresh@gmail.com', 
       98.89 : 'xyz', ('user_name', 'pwd'): ('suresh123', 'suresh@123'),
         89: 'test2'}

print(f'd1: {d1}, address: {id(d1)}\n')

d2 = d1.copy()
print(f'd2: {d2}, address: {id(d2)}\n')

d3 = d1
d3['address'] = 'xyz city-8945'
print(f'd3: {d3}, address: {id(d3)}\n')

print(f'd1: {d1}, address: {id(d1)}\n')
7
d2.clear()

print(f'd2: {d2}, address: {id(d2)}\n')

d1_address_value = d1.pop('address')
print(f'd1_address_value: {d1_address_value}')

print(f'd3: {d3}, address: {id(d3)}\n')

print(f'd1: {d1}, address: {id(d1)}\n')




