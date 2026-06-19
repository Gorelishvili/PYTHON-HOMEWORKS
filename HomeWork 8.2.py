# ა) ყველა პროდუქტის დასახელების დაბეჭდვა

products = [
    {"cola": {"price": 1.5, "quantity": 10}},
    {"fanta": {"price": 2.5, "quantity": 5}},
    {"snickers": {"price": 3.5, "quantity": 12}},
    {"water": {"price": 4.5, "quantity": 8}},
    {"beer": {"price": 6.5, "quantity": 5}}
]

for item in products:
    for name in item:
        print(name)


# ბ) ყველა პროდუქტის საერთო ღირებულების გამოთვლა        

total = 0

for item in products:
    for name, info in item.items():
        total += info["price"] * info["quantity"]

print(total)