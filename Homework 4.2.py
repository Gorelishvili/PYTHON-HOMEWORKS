num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))
operator = input("შეიყვანეთ ოპერატორი (+, -, *, /): ")

if operator == "+":
    print("შედეგი =", num1 + num2)
elif operator == "-":
    print("შედეგი =", num1 - num2)
elif operator == "*":
    print("შედეგი =", num1 * num2)
elif operator == "/":
    if num2 != 0:
        print("შედეგი =", num1 / num2)
else:
    print("არასწორი ოპერატორი!")