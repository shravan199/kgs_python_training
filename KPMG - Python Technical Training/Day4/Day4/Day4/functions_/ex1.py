def demo():
    print("This is demo function.")
    age=90
    dept="l&D"
    other="l&D"
    return age,dept,other #{"age":age,"dept":dept,"other":other}#[dept,age,other]

  
v=demo()
print(v)#v[1]
print(type(v))

