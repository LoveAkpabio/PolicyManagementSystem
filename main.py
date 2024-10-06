from policyholder import Policyholder
from product import Product
from payment import Payment

def main():
    # Create Products
    health_insurance = Product("Health Insurance", 200)
    life_insurance = Product("Life Insurance", 150)

    # Create Policyholders
    john = Policyholder("John Doe", "john.doe@example.com")
    jane = Policyholder("Jane Smith", "jane.smith@example.com")

    # Register Policyholders
    john.register()
    jane.register()

    # Add Products to Policyholders
    john.add_product(health_insurance)
    jane.add_product(life_insurance)

    # Process Payments
    payment_john = Payment(health_insurance.premium)
    payment_jane = Payment(life_insurance.premium)

    payment_john.process_payment()
    payment_jane.process_payment()

    # Display Policyholder Details
    print(f"Policyholder: {john.name}, Email: {john.email}, Products: {[p.name for p in john.products]}")
    print(f"Policyholder: {jane.name}, Email: {jane.email}, Products: {[p.name for p in jane.products]}")

if __name__ == "__main__":
    main()
