
letters = ['a', 'b', 'c', 'd', 'e', 'f']
print(f"letters :{letters}")

for letter in letters:
    print(letter)

print("-" * 60)

for letter in enumerate(letters):
    print(letter)

print("-" * 60)

for letter in enumerate(letters):
    print(letter[0], letter[1])

print("-" * 60)
lst1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"lst1 :{lst1}")

print("-" * 60)
for l in lst1:
    print(l)

print("-" * 60)
for l in enumerate(lst1):
    print(l)

print("-" * 60)
for inx, l in enumerate(lst1):
    print(inx, l)

print("-" * 60)
for idx, lst in enumerate(lst1):
    print(f"list({idx})")
    for ix, l in enumerate(lst):
        print(ix, l)

