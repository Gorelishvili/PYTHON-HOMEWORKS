try:
    age = int(input("შეიყვანეთ ასაკი: "))

    if age < 0:
        raise ValueError("უარყოფითი ასაკი დაუშვებელია")

except ValueError as error:
    if str(error) == "invalid literal for int() with base 10":
        print("შეიყვანეთ მხოლოდ რიცხვი!")
    else:
        print(error)

else:
    if age < 18:
        print("არასრულწლოვანი")
    else:
        print("სრულწლოვანი")