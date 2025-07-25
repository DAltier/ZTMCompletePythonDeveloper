class PlayerCharacter:
	membership = True # class object attribute
	def __init__(self, name, age):
		if self.membership: # or PlayerCharacter.membership
			self.name = name
			self.age = age

	def run(self):
		print('run')
		return 'done'
	
	def shout(self):
		return f'My name in {self.name}.'

player1 = PlayerCharacter('Cindy', 28)
player2 = PlayerCharacter('Tom', 21)

print(player1.name)
print(player1.age)
print(player1.shout())
print(player2.name)
print(player2.age)
print(player2.shout())

print(player1.membership)

# help(player1)