import math

a = int(input("შეიყვანეთ პირველი კათეტი: "))
b = int(input("შეიყვანეთ მეორე კათეტი: "))

if a > 0 and b > 0:
    hypotenuse = math.sqrt(a**2 + b**2)
    area = (a * b) / 2

    print("ჰიპოთენუზა:", hypotenuse)
    print("ფართობი:", area)
else:
    print("გთხოვთ შეიყვანოთ დადებითი მთელი რიცხვები.")