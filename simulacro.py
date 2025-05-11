# Initial inventory with 5 books
inventory = [
    {"title": "The Great Gatsby", "price": 12.99, "quantity": 10},
    {"title": "1984", "price": 9.50, "quantity": 5},
    {"title": "To Kill a Mockingbird", "price": 11.00, "quantity": 8},
    {"title": "Moby Dick", "price": 14.75, "quantity": 3},
    {"title": "Pride and Prejudice", "price": 10.25, "quantity": 6}
]

def add_book():
    title = input("Enter book title: ")
    try:
        price = float(input("Enter book price: "))
        quantity = int(input("Enter quantity available: "))
        if price <= 0 or quantity <= 0:
            print("Price and quantity must be positive numbers.")
            return
        inventory.append({"title": title, "price": price, "quantity": quantity})
        print("Book added successfully.")
    except ValueError:
        print("Invalid input. Price must be a number and quantity an integer.")

def find_book(title):
    for book in inventory:
        if book["title"].lower() == title.lower():
            return book
    return None

def consult_book():
    title = input("Enter book title to consult: ")
    book = find_book(title)
    if book:
        print(f"Title: {book['title']}, Price: ${book['price']:.2f}, Quantity: {book['quantity']}")
    else:
        print("Book not found in inventory.")

def update_price():
    title = input("Enter book title to update price: ")
    book = find_book(title)
    if book:
        try:
            new_price = float(input("Enter new price: "))
            if new_price <= 0:
                print("Price must be a positive number.")
                return
            book["price"] = new_price
            print("Price updated successfully.")
        except ValueError:
            print("Invalid input. Price must be a number.")
    else:
        print("Book not found in inventory.")

def delete_book():
    title = input("Enter book title to delete: ")
    book = find_book(title)
    if book:
        inventory.remove(book)
        print("Book deleted successfully.")
    else:
        print("Book not found in inventory.")

def calculate_total_value():
    total = sum(book["price"] * book["quantity"] for book in inventory)
    print(f"Total inventory value: ${total:.2f}")

def show_menu():
    print("\n--- Book Inventory Menu ---")
    print("1. Add a new book")
    print("2. Consult a book")
    print("3. Update book price")
    print("4. Delete a book")
    print("5. Show total inventory value")
    print("6. Exit")

def main():
    while True:
        show_menu()
        choice = input("Select an option (1-6): ")
        if choice == "1":
            add_book()
        elif choice == "2":
            consult_book()
        elif choice == "3":
            update_price()
        elif choice == "4":
            delete_book()
        elif choice == "5":
            calculate_total_value()
        elif choice == "6":
            print("Exiting program.")
            break
        else:
            print("Invalid option. Please try again.")

# Start the program
main()
 




