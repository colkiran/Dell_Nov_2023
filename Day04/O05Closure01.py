
# closure

def outerFun(gname):
    gname = "Mr." + gname

    def innerFun():

        print(f"Greeting {gname}")

    return innerFun

inref = outerFun("Sachin")

inref()         # out of the scope of outerFun

