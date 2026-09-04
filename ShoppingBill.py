def get_product_price(product):
    match product:
        case "M":
            return 10000
        case "L":
            return 50000
        case "H":
            return 2000
        case _:
            return None
def calculate_total_price(price, quantity):
    return price * quantity
def calculate_discount(total_price, discount_percentage):
    return total_price * discount_percentage / 100
def calculate_final_amount(total_price, discount):
    return total_price - discount

product = input("Enter Product (M/L/H): ").upper()
price = get_product_price(product)
if price is None:
    print("Invalid Product")
else:
    try:
        quantity = int(input("Enter Quantity: "))
        if quantity <= 0:
            print("Invalid Quantity")
        else:
            try:
                discount_percentage = float(
                    input("Enter Discount Percentage: ")
                )
                if discount_percentage < 0:
                    print("Invalid Discount Percentage")
                else:
                    match product:
                        case "M":
                            product_name = "Mobile"
                        case "L":
                            product_name = "Laptop"
                        case "H":
                            product_name = "Headphones"

                    total_price = calculate_total_price(price, quantity)
                    discount = calculate_discount(
                        total_price,
                        discount_percentage
                    )
                    final_amount = calculate_final_amount(
                        total_price,
                        discount
                    )
                    print("\n----- Bill Summary -----")
                    print("Product:", product_name)
                    print("Product Price: ₹", price)
                    print("Quantity:", quantity)
                    print("Total Price: ₹", total_price)
                    print("Discount Amount: ₹", discount)
                    print("Final Amount: ₹", final_amount)

            except ValueError:
                print("Invalid Discount Input")
    except ValueError:
        print("Invalid Quantity Input")