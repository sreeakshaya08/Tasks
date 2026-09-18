class FoodOrder:

    def __init__(self, order_id, customer_name, food_item, price, quantity):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.price = price
        self.quantity = quantity

    def calculate_total(self):
        return self.price * self.quantity

    def apply_discount(self):
        total = self.calculate_total()

        if total >= 2000:
            discount = total * 0.20
        elif total >= 1000:
            discount = total * 0.10
        elif total >= 500:
            discount = total * 0.05
        else:
            discount = 0

        return discount

    def generate_bill(self):
        total = self.calculate_total()
        discount = self.apply_discount()
        final_amount = total - discount

        print("\n----- FOOD ORDER BILL -----")
        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Total: ₹", total)
        print("Discount: ₹", discount)
        print("Final Amount: ₹", final_amount)


# Creating objects
order1 = FoodOrder(101, "Akshaya", "Pizza", 600, 3)
order2 = FoodOrder(102, "Rahul", "Burger", 300, 2)
order3 = FoodOrder(103, "Sneha", "Biryani", 450, 5)

# Display bills
order1.generate_bill()
order2.generate_bill()
order3.generate_bill()


orders = [order1, order2, order3]

# Highest bill
highest_order = max(orders, key=lambda order: order.calculate_total())

print("\n----- HIGHEST BILL -----")
print("Customer:", highest_order.customer_name)
print("Food:", highest_order.food_item)
print("Amount: ₹", highest_order.calculate_total())


# Total revenue
total_revenue = sum(order.calculate_total() for order in orders)

print("\nTotal Revenue: ₹", total_revenue)


# Average order amount
average = total_revenue / len(orders)

print("Average Order Amount: ₹", average)


# Customer who spent the most
highest_spender = max(
    orders,
    key=lambda order: order.calculate_total() - order.apply_discount()
)

print("\n----- HIGHEST SPENDER -----")
print("Customer:", highest_spender.customer_name)
print(
    "Amount Spent: ₹",
    highest_spender.calculate_total() - highest_spender.apply_discount()
)