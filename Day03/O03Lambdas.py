
def add(x, y):
    return x + y

a = add

res = a(16, 37)
print(f"res :{res}")

print("-" * 60)

b = lambda x, y: x + y
res = b(32, 48)
print(f"res :{res}")

# lambdas - map, filter and reduce

# map(funtion, list)    -   implement the expression on every element of the list
# filter(function, list) -  filter expression will return a True or False
# reduce(function, list) -  list will get reduced into a single value

print("-" * 60)
# map

lst1 = list(range(1, 11))
print(f"lst1 :{lst1}")

res = list(map(lambda x: x ** 2, lst1))
print(f"res :{res}")

print("-" * 60)
# filter

lst2 = list(range(1, 26))
print(f"lst2 :{lst2}")
res = list(filter(lambda x: x % 3 == 0, lst2))
print(f"res :{res}")

print("-" * 60)
# reduce
from functools import reduce
lst3 = [8, 3, 5, 9, 1, 4, 10, 6, 2, 7]
print(f"lst3 :{lst3}")

res = reduce(lambda x, y: x if x > y else y, lst3)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, lst3)
print(f"res :{res}")
