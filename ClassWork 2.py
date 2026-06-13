import random

secret_number = random.randint(1, 100)
lives = 5

while lives > 0:
    guess = int(input("შეიყვანე რიცხვი 1-დან 100-მდე: "))

    if guess == secret_number:
        print("გილოცავ! შენ მოიგე!")
        break

    lives -= 1

    if guess < secret_number:
        print("ჩაფიქრებული რიცხვი უფრო მეტია.")
    else:
        print("ჩაფიქრებული რიცხვი უფრო ნაკლებია.")

    print("დარჩენილი სიცოცხლეები:", lives)

if lives == 0:
    print("შენ წააგე!")
    print("ჩაფიქრებული რიცხვი იყო:", secret_number)