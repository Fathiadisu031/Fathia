def calculate_discount(price, discount_percent):
    final_price = price * (1 - discount_percent / 100)
    if discount_percent >= 20:
        return final_price
    return price



price = float(input("Enter the original price: "))

discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price , discount_percent)

print(f"The final price after discount is: {final_price}")
