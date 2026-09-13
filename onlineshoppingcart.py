class InvalidQuantityError(Exception):
    pass
class Product:
    def __init__(self, product_id, product_name, price, quantity):
        self.product_id = product_id
        self.product_name = product_name
        self.__price = price
        self.__quantity = quantity
        if price < 0:
            raise ValueError("Price cannot be negative")
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")
    def get_price(self):
        return self.__price
    def get_quantity(self):
        return self.__quantity
    def set_quantity(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")
        self.__quantity = quantity
    def increase_quantity(self, quantity):
        if quantity <= 0:
            raise InvalidQuantityError("Quantity must be greater than 0")
        self.__quantity += quantity
    def subtotal(self):
        return self.__price * self.__quantity
    def __str__(self):
        return (
            f"{self.product_id}  "
            f"{self.product_name}  "
            f"₹{self.__price}  "
            f"x{self.__quantity}  "
            f"= ₹{self.subtotal()}"
        )
class ShoppingCart:
    def __init__(self):
        self.products = []
    def add_product(self, product):
        for existing_product in self.products:
            if existing_product.product_id == product.product_id:
                existing_product.increase_quantity(
                    product.get_quantity()
                )
                print("Product quantity updated")
                return
        self.products.append(product)
        print("Product added successfully")
    def remove_product(self, product_id):
        for product in self.products:
            if product.product_id == product_id:
                self.products.remove(product)
                print("Product removed successfully")
                return
        print("Product not found")
    def update_quantity(self, product_id, quantity):
        for product in self.products:
            if product.product_id == product_id:
                product.set_quantity(quantity)
                print("Quantity updated successfully")
                return
        print("Product not found")
    def calculate_total(self):
        total = 0
        for product in self.products:
            total += product.subtotal()
        return total
    def apply_discount(self):
        total = self.calculate_total()
        if total >= 10000:
            return total * 0.20
        elif total >= 5000:
            return total * 0.10
        else:
            return 0
    def display_cart(self):
        if len(self.products) == 0:
            print("Cart is empty")
            return
        print("\n--------- Shopping Cart ---------")
        for product in self.products:
            print(product)
    def most_expensive_product(self):
        if len(self.products) == 0:
            return None
        expensive = self.products[0]
        for product in self.products:
            if product.get_price() > expensive.get_price():
                expensive = product
        return expensive
    def number_of_products(self):
        return len(self.products)
    def checkout(self):
        total = self.calculate_total()
        discount = self.apply_discount()
        final_amount = total - discount
        print("\n--------- Checkout ---------")
        print("Cart Total: ₹", total)
        print("Discount: ₹", discount)
        print("Final Amount: ₹", final_amount)
        print("----------------------------")
        print("Checkout Successful!")
product1 = Product(101, "Laptop", 60000, 1)
product2 = Product(102, "Mouse", 1000, 2)
product3 = Product(103, "Keyboard", 2000, 1)
cart = ShoppingCart()
cart.add_product(product1)
cart.add_product(product2)
cart.add_product(product3)
cart.display_cart()
cart.update_quantity(102, 3)
print("\nAfter updating quantity:")
cart.display_cart()
cart.remove_product(103)
print("\nAfter removing product:")
cart.display_cart()
print("\nNumber of different products:",
      cart.number_of_products())
expensive = cart.most_expensive_product()
if expensive:
    print("Most expensive product:", expensive.product_name)
cart.checkout()