print(type(int(str(100))))
print(int("0b100",2))
print(bin(5))

birth_year = input('what year were you born? ')
age = 2025 - int(birth_year)
print(f'You are {age} years old.')