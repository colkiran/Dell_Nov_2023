
def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun

# simple Curry
EngGrt = outerFun("Welcome")
TelGrt = outerFun("Namaskaram")

EngGrt('Sachin')
EngGrt("Virat")
TelGrt("Laxman")
