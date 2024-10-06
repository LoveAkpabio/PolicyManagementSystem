class Product:
    def __init__(self, name, premium):
        self.name = name
        self.premium = premium
        self.active = True

    def update(self, new_name, new_premium):
        self.name = new_name
        self.premium = new_premium
        print(f"Product updated to {self.name} with premium {self.premium}.")

    def suspend(self):
        self.active = False
        print(f"{self.name} has been suspended.")
