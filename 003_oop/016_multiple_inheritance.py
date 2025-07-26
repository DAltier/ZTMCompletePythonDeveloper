class User():
    def signed_in(self):
        print("User is logged in.")
        
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power
     
    def attack(self):
        print(f"{self.name} is attacking with {self.power} power.")
        
class Archer(User):
    def __init__(self, name, arrows):
        self.name = name
        self.arrows = arrows
     
    def attack(self):
        print(f"{self.name} is attacking with {self.arrows} arrows.")
        
    def check_arrows(self):
        print(f"{self.arrows} arrows left.")

class HybridBorg(Wizard, Archer):   # notice the order, in that order only it will give preference
    def __init__(self, name, power, arrows):
        Wizard.__init__(self,name,power)
        Archer.__init__(self,name,arrows)

hb1 = HybridBorg("Borgie", 50, 100)
hb1.attack()

print(hb1.name)
print(hb1.power)
print(hb1.arrows)

hb1.check_arrows()

hb1.signed_in()