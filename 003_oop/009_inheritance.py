class User():
    def sign_in(self):
        return "User is logged in."
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
     
    def attack(self):
        return f"{self.name} is attacking with {self.power} power."
        
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
     
    def attack(self):
        return f"{self.name} is attacking with arrows - {self.num_arrows} arrows left."

wizard1 = Wizard("Merlin", 50)
archer1 = Archer('Robin', 100)

print(wizard1.sign_in())
print(wizard1.attack())

print(archer1.sign_in())
print(archer1.attack())

# isinstance(instance, class)
print(isinstance(wizard1, Wizard)) # True
print(isinstance(wizard1, User)) # True
