from dataclasses import dataclass


@dataclass
class Product:
    name: str
    category: str
    price: float
    quantity: int

    @property
    def total_value(self):
        return self.price * self.quantity


class Store:
    def __init__(self):
        self.products = []

    def add_product(self, name, category, price, quantity):
        self.products.append(
            Product(name, category, price, quantity)
        )

    def sort_products(self):
        self.products.sort(
            key=lambda product: product.total_value,
            reverse=True
        )

    def get_total_value(self):
        return sum(
            product.total_value for product in self.products
        )

    def get_most_valuable(self):
        if not self.products:
            return None

        return max(
            self.products,
            key=lambda product: product.total_value
        )

    def print_report(self):
        print("Store Inventory")
        print("================")

        for product in self.products:
            print(
                f"{product.name} | "
                f"{product.category} | "
                f"${product.price:.2f} | "
                f"{product.quantity} units | "
                f"${product.total_value:.2f}"
            )

        print("================")
        print(f"Products: {len(self.products)}")
        print(f"Total Value: ${self.get_total_value():.2f}")

        most_valuable = self.get_most_valuable()

        if most_valuable:
            print(f"Most Valuable: {most_valuable.name}")
            print(
                f"Item Value: ${most_valuable.total_value:.2f}"
            )


store = Store()

store.add_product("Laptop", "Electronics", 899.99, 6)
store.add_product("Keyboard", "Accessories", 79.50, 15)
store.add_product("Monitor", "Electronics", 249.99, 10)
store.add_product("Mouse", "Accessories", 39.99, 24)
store.add_product("Headphones", "Audio", 129.99, 12)

store.sort_products()
store.print_report()