class Alpha:
    
    def fun1(self):
        print('Alpha class fun1()')

class Beta:

    def fun1(self):
        print('Beta class fun1()')

class Gamma(Alpha, Beta):
    pass

g = Gamma()
g.fun1()
print(Gamma.mro())