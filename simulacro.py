library=[
   {"title":"book1","price":23.00,"amount":45}
   ]

def addBook():
    library = []  # Lista para guardar todos los libros

    for i in range(2):
        title = input(f"Enter the name of the book {i+1}: ").strip()

        if title == "":
            print("Invalid title.\n")
            continue

        try:
            price = float(input(f"Enter price of the book {i+1}: "))
            if price < 0:
                print("Invalid price. Must be positive.\n")
                continue
        except ValueError:
            print("Invalid input. Price must be a number.\n")
            continue

        try:
            amount = int(input(f"Enter amount of the book {i+1}: "))
            if amount < 0:
                print("Invalid amount. Must be non-negative.\n")
                continue
        except ValueError:
            print("Invalid input. Amount must be an integer.\n")
            continue

        new_book = {"title": title, "price": price, "amount": amount}
        library.append(new_book)
        print(f"Book {i+1} added!\n")

    # Mostrar todos los libros agregados
    print("Library contents:")
    for l, book in enumerate(library, start=1):
        print(f"{l}. Title: {book['title']}, Price: ${book['price']:.2f}, Amount: {book['amount']}")

addBook()

def searchBook():
 title = input("What a book you want search?: ")

 for title in library:
     title = library[0]
     print(f"Book found: {title} ")
 else:
     print("the book dosen't exist in library")


searchBook()





