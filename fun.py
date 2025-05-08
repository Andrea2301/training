inventory ={
   "none": (23.00,5),
   "nones":(34.00,8),
   "proof":(32.00,9)
   }

print(inventory)

def addProduct(name="Sergio",price=24.02,amount=5):
    global inventory
    
    inventory[name] = (price,amount)
    
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
    
    
searchProduct("none")


def updatePrice(price):
    global inventory
    
    

   
updatePrice()


def deleteProduct(name):
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