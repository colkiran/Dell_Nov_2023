
l1 = list()
print(f"l1 :{l1}")      # format statement - interpolation
print(type(l1))         # RTTI - runtime type identification

print("-" * 60)

l2 = [1, 2, 3, 'four', 'five', 'six', 7.3, 8.2, 9.0, 10+2j, 11-5j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 60)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 60)
l1 = list(range(1, 11))
print(f"l1 :{l1}")

print(f"l1[0] :{l1[0]}")

l1[5] = 5.5
print(f"l1 :{l1}")

# print(dir(l1))
print("-" * 60)

lst1 = list(range(10, 31, 10))
print(f"lst1 :{lst1}")

a, b, c = lst1
print(a, b, c, sep=", ")

print("-" * 60)
lst1 = list(range(10, 101, 10))
print(f"lst1 :{lst1}")

*a, b, c = lst1
print(a, b, c, sep=", ")

print("-" * 60)
a, *b, c = lst1
print(a, b, c, sep=", ")

print("-" * 60)
a, b, *c = lst1
print(a, b, c, sep=", ")

print("-" * 60)
lst1 = [1, 2, 3, 4, 5]
lst2 = [6, 7, 8, 9, 10]

print(f"lst1 :{lst1}")
print(f"lst2 :{lst2}")

lst3 = [lst1, lst2]
print(len(lst3))

print("-" * 60)
lst4 = [*lst1, *lst2]
print(len(lst4))
