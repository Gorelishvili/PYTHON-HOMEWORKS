weight = float(input("შეიყვანეთ წონა (კგ): "))
height = float(input("შეიყვანეთ სიმაღლე (მ): "))

bmi = weight / (height ** 2)

print("BMI =", bmi)

if bmi < 19:
    print("underweight")
elif 19 <= bmi <= 25:
    print("normalweight")
else:
    print("overweight")