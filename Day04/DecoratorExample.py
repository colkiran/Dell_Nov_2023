

from datetime import datetime
def timeCalc(fnc):

    def helper(arg):
        print("function called.....")
        st = datetime.now()
        fnc(arg)
        et = datetime.now()
        print("function executed successfully......")
        print(f"time taken {et - st}")

    return helper

@timeCalc
def fun(cntr):
    lst = []
    for i in range(1, cntr+1):
        for j in range(1, i + 1):
            lst.append(j ** 2)

fun(6500)

# OOPs
#@classmethod
#@abstractmethod
