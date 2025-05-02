# Function to request the product name, validating that it only contains letters and spaces
def get_product_name():
    while True:
        name = input("Enter the product name: ").strip()
        # Check if the input is not empty and only contains letters
        if name and all(word.isalpha() for word in name.replace(" ", "").split()):
            return name
        else:
            print("Invalid name. Only letters and spaces are allowed.")

# Function to request a positive number (used for price and quantity)
def get_positive_number(message):
    while True:
        try:
            value = float(input(message))
            if value > 0:
                return value  # Return the value if it's positive
            else:
                print("You must enter a positive number.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Function to request the discount percentage, ensuring it's between 0 and 100
def get_discount():
    while True:
        try:
            discount = float(input("Enter the discount percentage (0 to 100): "))
            if 0 <= discount <= 100:
                return discount  # Return the discount if it's within range
            else:
                print("The discount must be between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number.")

# Requesting input from the user
product_name = get_product_name()
unit_price = get_positive_number("Enter the unit price of the product: ")
quantity = get_positive_number("Enter the quantity of products: ")
discount = get_discount()

# Calculate the total cost before discount
subtotal = unit_price * quantity

# Calculate the discount amount
discount_amount = subtotal * (discount / 100)

# Calculate the final total after applying the discount
total_cost = subtotal - discount_amount

# Display a formatted summary of the purchase with two decimal places
print("\n--- PURCHASE SUMMARY ---")
print(f"Product: {product_name}")
print(f"Quantity: {int(quantity)}")
print(f"Unit price: ${unit_price:.2f}")
print(f"Discount applied: {discount:.2f}%")
print(f"Total to pay: ${total_cost:.2f}")


