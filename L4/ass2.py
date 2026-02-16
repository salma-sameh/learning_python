from abc import ABC, abstractmethod


# ================= Abstract Product =================
class Product(ABC):
    def __init__(self, name, price):
        self.__name = name        # Encapsulation
        self.__price = price

    def get_name(self):
        return self.__name

    def _get_price_value(self):
        return self.__price

    @abstractmethod
    def get_price(self):
        pass

    @abstractmethod
    def get_description(self):
        pass


# ================= Subclasses =================
class Electronics(Product):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.__brand = brand

    def get_price(self):
        return self._get_price_value()

    def get_description(self):
        return f"Electronics: {self.get_name()} (Brand: {self.__brand})"


class Clothing(Product):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.__size = size

    def get_price(self):
        return self._get_price_value()

    def get_description(self):
        return f"Clothing: {self.get_name()} (Size: {self.__size})"


class Book(Product):
    def __init__(self, name, price, author):
        super().__init__(name, price)
        self.__author = author

    def get_price(self):
        return self._get_price_value()

    def get_description(self):
        return f"Book: {self.get_name()} (Author: {self.__author})"


# ================= Shopping Cart =================
class ShoppingCart:
    def __init__(self):
        self.__products = []      # Encapsulation

    def add_product(self, product):
        self.__products.append(product)

    def remove_product(self, product_name):
        self.__products = [
            p for p in self.__products if p.get_name() != product_name
        ]

    def calculate_total(self):
        return sum(p.get_price() for p in self.__products)

    def save_to_file(self, filename="cart.txt"):
        with open(filename, "w") as file:
            for p in self.__products:
                file.write(p.get_description() + "\n")
            file.write(f"Total: {self.calculate_total()}")

    # Dunder: length of cart
    def __len__(self):
        return len(self.__products)

    # Dunder: string representation
    def __str__(self):
        if not self.__products:
            return "Cart is empty"

        result = "Shopping Cart:\n"
        for p in self.__products:
            result += f"{p.get_description()} - ${p.get_price()}\n"

        result += f"Total: ${self.calculate_total()}"
        return result


# ================= Test =================
if __name__ == "__main__":
    cart = ShoppingCart()

    e = Electronics("Laptop", 1000, "HP")
    c = Clothing("T-Shirt", 30, "M")
    b = Book("Python Guide", 50, "Ali")

    cart.add_product(e)
    cart.add_product(c)
    cart.add_product(b)

    print(cart)
    print("Items in cart:", len(cart))

    cart.remove_product("T-Shirt")
    print("\nAfter removal:")
    print(cart)

    cart.save_to_file()
