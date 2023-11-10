"""
sort    -   sorts the original list
sorted  -   creates a copy of sorted list and returns it

"""


l1 = [8, 3, 7, 10, 1, 9, 4, 2, 5, 6]
print(f"l1 :{l1}")

res_asc = sorted(l1)
print(f"Ascending :{res_asc}")

res_desc = sorted(l1, reverse=True)
print(f"Descending :{res_desc}")

print("-" * 60)

l1 = [8, 'zebra', 'yellow', 3, 'apple', 'red', 7, 'green', 'violet', 10,'orange', 'pink', 1, 'blue', 'purple', 9, 'cat', 4, 'dog', 2, 'xray', 5, 6, 19, 123, 1124, 27, 245, 2134]

print(f"l1 :{l1}")

print("-" * 70)

res = sorted(l1, key=ascii)

print(f"res :{res}")

print("-" * 60)
cities = ['thiruvananthapuram', 'bangalore', 'chennai', 'hyderabad', 'ooty', 'delhi', 'pune', 'kolkata', 'vishakapatnam']

print(f"cities :{cities}")

res_asc = sorted(cities, key=len)
print(f"Ascending Order :{res_asc}")

res_desc = sorted(cities, key=len, reverse=True)
print(f"Descending Order :{res_desc}")

