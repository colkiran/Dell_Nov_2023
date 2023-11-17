
def outerFun():
    gname = 'Sachin'
    def innerFun():

        nonlocal  gname     # only a local variable can be used as non_local variable

        gname = "Mr." + gname

        print("Hello World")

        print(f"Guest Name :{gname}")

    innerFun()

outerFun()
