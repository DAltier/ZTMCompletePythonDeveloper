class User():
    def signed_in(self):
        return "User is logged in."
        
    def attack(self):
        return "Do nothing."
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
     
    def attack(self):
        print(User.attack(self))  # Just a way to use parent class method.
        return f"{self.name} is attacking with {self.power} power."
        
class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows
     
    def attack(self):
        return f"{self.name} is attacking with arrows - {self.num_arrows} arrows left."

wizard1 = Wizard("Merlin", 50)
archer1 = Archer('Robin', 30)

def player_attack(char):
    return char.attack()
    
print(player_attack(wizard1))
print(player_attack(archer1))
# notice that these two instances are executing the child class method and not the parent class method.

'''
This is polymorphism.
Even though we are using the same function, it is giving different output based on the object.
'''