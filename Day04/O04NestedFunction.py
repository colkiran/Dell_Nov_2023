
def outerFun(gname):
    gn = "Mr." + gname
    def innerFun():

        print(f"Greetings {gname}")
        print(gn)

    innerFun()

outerFun("Rahul")
