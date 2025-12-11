try:
    number_of_items = int(input("Enter no. of items: "))
    if number_of_items <= 0:
        raise ValueError("Cart is empty")

    total_price = 200 + number_of_items
    average_price = total_price / number_of_items
    print("The average price is:", average_price)

except ValueError:
    print("Your cart is empty please add items")

print("Thank you for using this program")


