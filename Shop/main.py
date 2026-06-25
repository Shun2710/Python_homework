import sys

sys.stdout.reconfigure(encoding="utf-8")


class Product:
    def __init__(self, name, category, price, quantity):
        self.name = name
        self.category = category
        self.price = float(price)
        self.quantity = int(quantity)

    def change_price(self, new_price):
        self.price = float(new_price)

    def change_quantity(self, new_quantity):
        self.quantity = int(new_quantity)

    def __str__(self):
        return f"{self.name} ({self.category}) - {self.price} грн, на складе: {self.quantity}"


class Order:
    def __init__(self):
        self.products = []
        self.total_amount = 0

    def add_product(self, product, quantity):
        if product.quantity >= quantity:
            self.products.append((product, quantity))
            product.quantity -= quantity
            self.calculate_total()
        else:
            print(f"Недостаточно товара {product.name}")

    def calculate_total(self):
        self.total_amount = sum(
            product.price * quantity
            for product, quantity in self.products
        )
        return self.total_amount

    def __str__(self):
        result = "Заказ:\n"
        for product, quantity in self.products:
            result += f"- {product.name} x {quantity}\n"
        result += f"Общая сумма: {self.total_amount} грн"
        return result


class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.orders = []

    def add_order(self, order):
        self.orders.append(order)

    def __str__(self):
        return f"{self.name} ({self.email})"


def load_products(filename):
    products = []

    with open(filename, "r", encoding="utf-8") as file:
        for line in file:
            name, category, price, quantity = line.strip().split(";")
            products.append(Product(name, category, price, quantity))

    return products


products = load_products("products.txt")

print("Список товаров:")
for product in products:
    print(product)

customer = Customer("Иван Петров", "ivan@gmail.com")

order = Order()
order.add_product(products[0], 2)
order.add_product(products[1], 1)

customer.add_order(order)

print("\nДанные клиента:")
print(customer)

print("\nИнформация о заказе:")
print(order)

print("\nОстаток товаров:")
for product in products:
    print(product)