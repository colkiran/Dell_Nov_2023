
def greet():
    print("Greetings Mr.Sachin, Welcome to the event.....")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# gname is non default argument, city is default argument
def greetGstCity(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.......")

greet()             # calling the function
print("-" * 60)

greetGst("Sachin")
greetGst("Sourav")

print("-" * 60)

greetGstCity("Sachin")
greetGstCity("Rohit")
greetGstCity("Rahul", "Bangalore")

print("-" * 60)
# return values
def add(x, y):
    return x + y

a = 18
b = 16
print(f"The sum of {a} and {b} is {add(a, b)}")

# recursive calls - return mandatory
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n - 1)

num = 5
print(f"The factorial of {num} is {fact(num)}")

print("-" * 60)
# how many values can a function return

def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithCalc(20, 8)
print(f"res :{res}")

print("-" * 60)
# named arguments
def admsn(fname, lname, dob, city, adr, qlf, gender, mrdst, exp):
    print(f"Name :{fname} {lname}")
    print(f"DOB             :{dob}")
    print(f"City          :{city}")
    print(f"Address         :{adr}")
    print(f"Qualification   :{qlf}")
    print(f"Gender          :{gender}")
    print(f"Marital Status  :{mrdst}")
    print(f"Experience      :{exp}")

admsn(adr = "MG Road", city="Bangalore", exp="5 years", gender="Male", fname="Micheal", lname="Slater", dob="13/05/1982", qlf="B.E", mrdst="Bachelor")

print("-" * 60)
# variable length argument
# *arg, **kwarg
# *arg  -   will accept more than one argument and stores it in a tuple
# **kwarg - will accept data like a dictionary

def multinumbers(*numbers):
    print(f"numbers :{numbers}")
    print(*numbers)         #unpack the list
    num = 1
    for x in numbers:
        num *= x
    return num

res = multinumbers(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 60)
def extractDetials(**details):
    print(details)
    print("-" * 60)
    for k, v in details.items():
        print(k, "=>", v)

extractDetials(name="Rahul", age=34, runs=145, oppn="Sri Lanka")

print("-" * 60)

def fun():
    # this is a comment
    "this is a doc string"
    print("hello world")

fun()
print(fun.__doc__)      # doc string

print("-" * 60)

def fun1(x, y):
    """
    fun1(x, y)
    -----------

    fun1 takes two arguments x and y
    1. if x and y both are integers then we get the sum of the numbers
    2. if x and y both are strings then we get a concatenated string
    3. if x and y both are of different then throws an error

    """

    return x + y

print(fun1(10,20))
print(fun1("hello", "world"))

help(fun1)
