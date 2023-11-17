

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player initialized......")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def createPlayer(cls, fname, lname, age):
        print("Factory......")
        return cls(f"{fname} {lname}", age)          # calls the constructor


ply1 = Player("Sachin", 32)
ply1.get_details()

print("-" * 60)

ply2 = Player.createPlayer("Virat", "Kholi", 35)
ply2.get_details()
