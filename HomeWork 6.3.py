price = 50
valid_bills = [5, 10, 20]

print("გადასახდელი თანხა არის:", price, "ლარი")

while price > 0:
    bill = int(input("შეიყვანეთ კუპიურა (5, 10 ან 20): "))

    # ვალიდაციის შემოწმება
    if bill not in valid_bills:
        print("შეიტანეთ ვალიდური კუპიურა!")
        continue

    # თუ კუპიურა სწორია
    price -= bill

    # თუ ჯერ კიდევ დარჩა გადასახდელი
    if price > 0:
        print("დარჩენილია გადასახდელი:", price, "ლარი")

# თუ ზედმეტი გადაიხადა
if price < 0:
    print("თქვენი ხურდაა:", abs(price), "ლარი")
else:
    print("გადახდა დასრულებულია.")