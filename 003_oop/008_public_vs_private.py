class PlayerCharacter:
    def __init__(self, name, age):
        self._name = name  
        self._age = age
            
    def speak(self):
        return f"My name is {self._name} and I am {self._age} years old."
       
player1 = PlayerCharacter('Cindy', 28)
player2 = PlayerCharacter('Tom', 21)

print(player2._name)
print(player2.speak())

'''
Here the user has overwritten the class attributes and methods.
Which we would ideally don't want users to do.
However for other users, like player2, all the original attributes and methods functionality is intact.
Hence there is a need for Private attributes and methods, so the user cannot modify them.

But in Python the concept of Private is not there, so we have to work around that. 

So, we can use:
    class PlayerCharacter:
        def __init__(self, name, age):
            self._name = name  
            self._age = age
            
    player1 = PlayerCharacter("Rohan", 22)
    player1.name = "!!!!" 

The user can still modify the attribute, by using 'player1._name = "!!!!"', but we are just letting him know
that '_name' is a private variable, and you should not change it.
            
It's a naming convention to start a private variable with '_' (an underscore), 
so other users will get to know about it.
Similarly we don't ever modify 'dunder' methods, they start and ends with two underscores (for eg. __init__)
        
'''