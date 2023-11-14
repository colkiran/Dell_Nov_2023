
lst1 = list(range(1, 11))
squares = [x ** 2 for x in lst1]
print(f"squares :{squares}")

print("-" * 60)
sentence = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")
words = [word for word in sentence.split()]
print(f"words :{words}")

words = [(word, len(word)) for word in sentence.split() if word != "the"]
print(f"words :{words}")

print("-" * 60)

fruits = [
    ('apple', 285),
    ('orange', 80),
    ('grapes', 120),
    ('pineapple', 70),
    ('gauva', 90),
    ('watermelon', 150),
    ('banana', 140),
    ('strawberry', 350)
]

print(f"Fruits :{fruits}")
print("-" * 60)

price = ["fruit" for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[0] for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] * 0.9 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

price = [fruit[1] * 0.75 for fruit in fruits]
print(f"price :{price}")
print("-" * 60)

expnsFrts = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75)
             for fruit in fruits if fruit[1] > 100]
print(f"Expensive Fruits :{expnsFrts}")
