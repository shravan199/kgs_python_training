dic = {'name': 'Suresh', 'age': 24, 89:'test', 'email_id': 'suresh@gmail.com', 
       98.89 : 'xyz', ('user_name', 'pwd'): ('suresh123', 'suresh@123'),
         89: 'test2'}

# How to update value within dict
dic['name'] = 'Mahesh'

dic.update({'age': 26})
dic.update({'Mob No.': 903454554})

for k,v in dic.items():
    print(f'{k} : {v}')