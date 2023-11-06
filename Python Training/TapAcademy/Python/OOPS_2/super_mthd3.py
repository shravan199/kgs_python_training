class A:
    def fun(self):
        print('A')

class B(A):
    def fun(self):
        print('B')

class C(B):
    def fun(self):
        super(B,self).fun()
        print('C')

c = C()
c.fun()