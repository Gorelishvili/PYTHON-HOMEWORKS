def text_info(text):
    upper_count = 0

    for char in text:
        if char.isupper():
            upper_count += 1

    return upper_count, text.upper()


user_text = input("შეიყვანეთ ტექსტი: ")

count, upper_text = text_info(user_text)

print("დიდი ასოების რაოდენობა:", count)
print("ტექსტი uppercase-ში:", upper_text)