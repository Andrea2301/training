from inventory import addProduct,inventory,searchProduct,updatePrice,deleteProduct,calculateValue

#Menu for the user to interact whit the program
def menu():
    print("=====Menu=======")
    print("1.Add new product")
    print("2.Search product")
    print("3.Update Product")
    print("4.Delete product")
    print("5.Calculate value of the inventory")
    print("6.Exit!")
 
def main():
    while True:
        menu()
        choice = input("\nSelect an option: ")
        if choice == '1':
            addProduct()
            print(inventory)
    
        elif choice == '2':
            searchProduct()
        elif choice == '3':
            print(inventory)
            updatePrice()
            print(inventory)
        elif choice == '4':
            print(inventory)
            deleteProduct()
        elif choice == '5':
            calculateValue()
        elif choice == '6':
            
            print("Good bye!!")
            exit()      
        else:
            print("invalid option. Try again!")
            continue
        


main()


if 5 > 4:
    print('5 es mayor a 4')
elif 5 < 4:
    print('5 es menor a 4')
else:
    print("Que verga")