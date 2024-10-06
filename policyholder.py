class Policyholder:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.active = True
        self.products = []

    def register(self):
        self.active = True
        print(f"{self.name} has been registered.")

    def suspend(self):
        self.active = False
        print(f"{self.name} has been suspended.")

    def reactivate(self):
        self.active = True
        print(f"{self.name} has been reactivated.")

    def add_product(self, product):
        self.products.append(product)
        print(f"{product.name} has been added to {self.name}'s account.")
