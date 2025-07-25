def say_hello(name, age):
    print(f'Hi {name}, your age is {age}')
    
# Default Parameters
def say_hello2(name="John", age=25):
    print(f'Hi {name}, your age is {age}')

# Positional Arguments
say_hello("Alex", 27)

# Default Arguments
say_hello2()
say_hello2("Alex")

# Key Arguments
say_hello(age = 89, name = "Jessie")