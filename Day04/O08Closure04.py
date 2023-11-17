
def fun(*args):
    print(f"fun called....{args}")

x = 10
y = 20
z = 30
fun()
fun(x)
fun(x, y)
fun(x, y, z)

print("-" * 60)

def sum(x, y):
    print(f"Adding {x} and {y}")
    return x + y

def diff(x, y):
    print(f"Subtracting {y} from {x}")
    return x - y

# HOF  -  function that takes a function as argument or returns a function as a return value
def outerFun(fnc):
    loginfo = "Logging into the process....."
    def innerFun(*args):
        print(loginfo)
        print(fnc(*args))
        print("-" * 60)

    return innerFun

sumLogger = outerFun(sum)
sumLogger(10, 20)

diffLogger = outerFun(diff)
diffLogger(20, 8)
