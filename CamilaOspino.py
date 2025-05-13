
inventory={ #dictionary where products are stored
    
    
    "none":(23.00,5),
    "test":(23.00,5),
    "tests":(34.00,6)
}




def addProduct(): #allows you to add a new product to the inventory with price and quantity

    for i in range(5):
        
        name=(input(f"Enter the name product {i+1}:  "))
        
        try:
            price = float(input(f"Enter price {i+1}:  "))
            amount = int(input(f"Enter amount {i+1}:  "))
            if price <=0 or  amount<=0: 
                print("the value must be positive number")  
        except ValueError:
            return
        print("Try again!")
        print(f"New product added{name}!")  
        inventory[name] = (price,amount)
        continue   
  

def searchProduct():#allows you to search for a product in the inventory by returning its name, price and quantity   
   global inventory
   
   name = (input("Enter the product name you want to search for: "))
   
   if name in inventory:
       x = inventory.get(name)
       print(f"Found!")  
       print(f"{name}: {x[0]} {x[1]}")      
   else:
       print("Not Found")

       
def updatePrice():#allows you to update the price of a specific product
   
    print (inventory)
    
    name = input("Enter the name of the product you want to modify: ")
    currentPrice = inventory[name][0]
    if name in inventory:
        print(f"Current price of: {name} is {currentPrice} ")
    
    response = input("You want to modify it? (yes/no)")
    if response == "yes":
        newPrice = float(input("Enter the new price:"))
        if newPrice > 0 :
            inventory[name]=(newPrice,inventory[name][1])
            print(f"modified price!: {newPrice}")
            print(inventory)
        else:
            print("no changes were made")            


def deleteProduct():#allows you to delete a product from the inventory if it is in the
    global inventory
    name = input("What product do you want to delete?: ")
    
    if name in inventory:
        del inventory[name]
        print("deleted product")
        print(inventory)
    elif name not in inventory:
        print("the product is not in inventory!")
   
   
def totalValue():#shows the accumulated value of the inventory
    global inventory
    value = sum(map(lambda item: item[0] * item[1], inventory.values()))
    print(f"the total value of the inventory: {value:.2f}")
  
def menu():
    print("=================") 
    print("       MENU      ")
    print("=================")  
    print("1.Add new product")
    print("2.Search for a product")
    print("3.Update the price of a product")
    print("4.Delete a product")
    print("5.Calculate inventory value")
    print("6.Exit")


def main():
   
    while True:
        menu()
        choice = input("\nselect an option: ")
  
        if choice == '1':
            addProduct()
        elif choice == '2':
            searchProduct()
            print(inventory)
        elif choice== '3':
            updatePrice()
        elif choice == '4':
            deleteProduct()
        elif choice== '5':
            totalValue()
        elif choice =='6':
            print("Bye!!")
            exit()
        else:
            print("invalid option !!")
        continue 
main()


 


