print("Welcome to the shopping cart program")
item_names = []
item_prices = []
item=''
while item !='Done':
    item = input("Enter item name (or done to finish): ").title()

    if item=='Done':
        break
    else:
        price = int(input(f"Enter price of {item}: "))
        item_names.append(item)
        item_prices.append(price)

total_price = sum(item_prices)

print ("\nCart Summary:")
for i in range(len(item_names)):
    print(f"{item_names[i]} - {item_prices[i]}")

print(f"\nTotal Price:{total_price}")

discount=0
if total_price > 100:
    discount = total_price * 0.10
    print(f"Discount: {discount}")
final_price = total_price-discount
print(f"Final price: {final_price}")
