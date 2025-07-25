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
	
	@classmethod
	def adding_things(cls, num1, num2):
		return num1 + num2
	
	@classmethod
	def adding_things_2(cls, num1, num2):
		return cls('Teddy', num1 + num2)
	
	@staticmethod
	def adding_things_3(num1, num2):
		return num1 + num2

player1 = PlayerCharacter('Cindy', 28)
player2 = PlayerCharacter('Tom', 21)

print(player1.adding_things(2, 3))

print(PlayerCharacter.adding_things(4, 5))

player3 = PlayerCharacter.adding_things_2(5, 6)