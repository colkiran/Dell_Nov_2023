
from collections import namedtuple
def arithCalc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    nmdtpl = namedtuple("ArithCalculator", "sum diff prod quot")
    arithcalc = nmdtpl(sum= sum, diff=diff, prod=prod, quot=quot)
    return arithcalc


res = arithCalc(20, 8)
print(f"res :{res}")

print(f"Sum  :{res.sum}")
print(f"Diff :{res.diff}")
print(f"Prod :{res.prod}")
print(f"quot :{res.quot}")


