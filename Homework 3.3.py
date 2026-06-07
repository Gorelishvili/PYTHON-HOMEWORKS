word1 = input("შეიყვანეთ პირველი სიტყვა: ").lower()
word2 = input("შეიყვანეთ მეორე სიტყვა: ").lower()

if sorted(word1) == sorted(word2):
    print("ანაგრამებია")
else:
    print("ანაგრამა არ არის")