class Demo:
    a = 10
    b = 20


def main():
    print(Demo.a)
    print(Demo.b)
    
    Demo.a= 100
    Demo.b= 200
    print(Demo.a)
    print(Demo.b)
    

    d = Demo()
    print(d.a)
    print(d.b)

    d.a = 1000
    d.b = 2000

    print(d.a)
    print(d.b)
    
    print(Demo.a)
    print(Demo.b)
if __name__ == '__main__':
    main()