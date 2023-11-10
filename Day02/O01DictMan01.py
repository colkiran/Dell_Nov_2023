
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 60)

d2 = {'name': 'Sachin', 'age': 32, 'runs': 80, 'oppn': 'WI', 'venue': 'Sabina Park'}
print(f"d2 :{d2}")

print(f"Name :{d2['name']}")
print(f"Runs :{d2['runs']}")

print("-" * 60)

d3 = dict([('name', 'sachin'), ('age', 32), ('runs', 45), ('oppn', 'Eng')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 60)

d4 = dict(name='sachin', age=34, runs=50, oppn='PAK')
print(f"d4 :{d4}")
print(type(d4))

# CRUD
d2 = {'name': 'Sachin', 'age': 32, 'runs': 80, 'oppn': 'WI', 'venue': 'Sabina Park'}
print(f"d2 :{d2}")

print(f"Name :{d2['name']}")
print(f"Runs :{d2['runs']}")

# iterate through the dictionary
print("-" * 60)

for x in d2:
    print(x, "=>", d2[x])


# add
d2['year'] = '1998'
d2['team'] = 'India'
d2['runs'] = 145
d2['name'] = 'Tendulkar'

print(f"d2 :{d2}")


print("-" * 60)
# del
del d2['age']
del d2['venue']

print(f"d2 :{d2}")

print(dir(d2))

print("-" * 60)

player = {'name': 'Sachin', 'age': 32, 'runs': 80, 'oppn': 'WI', 'venue': 'Sabina Park'}

print(f"player :{player}")

print("-" * 60)
# keys
kys = player.keys()
print(f"keys :{kys}")

print("-" * 60)
# values
vls = player.values()
print(f"values :{vls}")

print("-" * 60)
# fromkeys
cities = ['blr', 'che', 'del', 'hyd', 'mum', 'kol']
print(f"cities :{cities}")

res = dict.fromkeys(cities)
print(f"res :{res}")

res = dict.fromkeys(cities, 23)
print(f"res :{res}")

print("-" * 60)
# items
for k, v in player.items():
    print(k, "=>", v)
