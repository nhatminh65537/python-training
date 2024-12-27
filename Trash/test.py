x = 66
def f():
    def g():
        def h():
            global x
            x = 88
        h()
    g()
f()
print(x)

print(globals())

class C:
    print(10)

    def f():
        print(20)
    
    def g(x):
        if x is None:
            f()
        else:
            print("g called with", x)
    g(None)

a = C()
a.g()