
print("append".center(60, "-"))
l1 = list(range(1, 6))
print(f"l1 :{l1}")

l1.append(6)
l1.append(7)
l1.append(8)
print(f"l1 :{l1}")

l1.append([9, 10, 11, 12, 13])
print(f"l1 :{l1}")

print("insert".center(60, "-"))
l2 = list(range(1, 6))
print(f"l2 :{l2}")

l2.insert(1, 1.5)
l2.insert(3, 2.5)
l2.insert(5, 3.5)
l2.insert(7, 4.5)

print(f"l2 :{l2}")

print("Extend".center(60, "-"))
l3 = list(range(1, 4))
print(f"l3 :{l3}")

l3.extend([4, 5, 6, 7, 8])
print(f"l3 :{l3}")

print("copy".center(40, "-"))
l1 = list(range(1, 6))
print(f"l1 before :{l1}")

# copy the list l1 to l2
l2 = l1             # shallow copy - shallow copy not only copies the data it also copies the address

print(f"l2 before :{l2}")
l2.extend([6, 7, 8, 9, 10])

print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("=" * 60)
l3 = list(range(10, 51, 10))
print(f"l3 before :{l3}")

# copy l3 to l4
l4 = l3.copy()              # Deep copy - only copies the data
print(f"l4 before :{l4}")

l4.extend([60, 70, 80, 90])
print(f"l4 after :{l4}")
print(f"l3 after :{l3}")

print("=" * 60)
l5 = [2, 4, 6, 8, [1, 2, 3, 4, 5], 10]
print(f"l5 before :{l5}")

# copy l5 to l6
l6 = l5.copy()
print(f"l6 before :{l6}")

l6[4].extend([6, 7, 8])
print(f"l6 after :{l6}")
print(f"l5 after :{l5}")

print("=" * 60)
from copy import deepcopy
l7 = [1, 2, 3, [5, 10, 15, 20, 25], 4, 5]
print(f"l7 before :{l7}")

# copy l7 to l8
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

l8[3].append(30)
l8[3].append(35)
l8[3].append(40)
l8[3].append(45)

print(f"l8 after :{l8}")
print(f"l7 after :{l7}")



