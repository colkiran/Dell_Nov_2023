
def callMe():
    print("apples from Ooty.....")

def fun(fnc):
    print("Hello.......")
    fnc()
    print("Hi.......")
    print("-" * 60)

    def defineMe():
        print("Oranges from Kanpur......")

    return defineMe

def funCallBack(fnc):
    print("Mera Bharath Mahan......")
    fnc()
    print("India is great.......")

funCallBack(fun(callMe))


"""
def fun(fnc):
    print("Greetings")
    fnc()
    def fun3():
        print("Thanks")
    return fun3
    
    
def fun1(fnc):
    print("Hi")
    fnc()
    print("hello")

def fun2():
    print("hola")
    

fun1(fun(fun2))
"""