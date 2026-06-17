import random

numbers = []

for i in range(20):
    numbers.append(random.randint(-50, 50))

even_numbers = []

for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)

print("პირველი სია:", numbers)
print("ლუწი რიცხვების სია:", even_numbers)