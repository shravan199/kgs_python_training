class A:
    def fun(self):
        print('A')

class B:
    def fun(self):
        print('B')

class C(A,B):
    def fun(self):
        super().fun()
        print('C')

c = C()
#print(help(c)) # C,B
c.fun()