inventory ={
   "none": (23.00,5),
   "nones":(34.00,8),
   "proof":(32.00,9)
   }

print(inventory)

def addProduct(name="Sergio",price=24.02,amount=5):
    global inventory

    name = input("Enter the product name: ")
    price = float(input("Enter the price: "))
    amount = int(input("Enter the amount: "))
    
    inventory[name] = (price,amount)

    print(f"Product {name} added successfully!")
    
addProduct()
print(inventory)



def searchProduct(name):
    global inventory 
    x = inventory.get(name)
    
    if x :
        print("Producto encontrado")
        print(f"{name}: {x[0]} {x[1]}")
    else:
        print("Producto no encontrado")
    
    
searchProduct()


def updatePrice():
    global inventory

    name = input("Enter the product name: ").strip().lower()
    
    if name in inventory:
        current_price = inventory[name][0]
        print(f"The current price of {name} is: {current_price}")

        response = input("Want to change the price? (yes/no): ").strip().lower()

        if response == "yes":
            new_price = float(input("Enter the new price: "))
            inventory[name] = (new_price, inventory[name][1])  # Actualiza solo el precio
            print(f"The price of {name} has been updated to: {new_price}")
        else:
            print("No changes made.")
    else:
        print(f"Product {name} not found in inventory.")

# Ahora puedes ejecutarla sin argumentos
updatePrice()
print(inventory)



def deleteProduct():
    name = input("what product do you want to eliminate?: ") 
    if name in inventory:  
     del inventory[name]
     print("the product was removed!")
    else:
        print("the product does not exist!")
 
deleteProduct() 


def calculateValue():
    global inventory
    
    value = sum (map(lambda item: item[0] * item[1],inventory.values()))

    print(f"total inventory value: {value}")
      
calculateValue()       