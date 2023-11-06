class DemoClass:
    print(f'This is my first class')
    
#variable length keyword arguments
def collect_student_data(sid, **data):
    print(sid)
    print(data)
    
    print(type(data))

collect_student_data(1,name='Shravan', age= 24, gender= 'Male', 
                     mob_num=989889984, father_name='Ram Bhavan Jha', country='India' )