class PlayerCharacter:
	def __init__(self, name, age):
		self.name = name
		self.age = age

	def speak(self):
		return f"My name is {self.name} and I am {self.age} years old."

player1 = PlayerCharacter('Cindy', 28)
player2 = PlayerCharacter('Tom', 21)

print(player1.name)
print(player1.age)
print(player1.speak())
print(player2.name)
print(player2.age)

# classes have methods, dictionaries don't