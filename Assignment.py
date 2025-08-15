def calculate_discount(price, discount_percent):
    discount = (discount_percent / 100)*price
    if discount_percent >= 20:
        finalPrice = price - discount
    else:
        finalPrice = price
    return finalPrice

price = float(input("Enter the price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))

print(f"{calculate_discount(price, discount_percent):.2f} Ksh")
