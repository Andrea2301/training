#Menu for the user to interact whit the program
def menu():
    print("=====Menu=======")
    print("1.Add new product")
    print("2.Search product")
    print("3.Update Product")
    print("4.Delete product")
    print("5.Calculate value of the inventory")
 
def main():
 while True:
 
  choice = input("\nSelect an opcion: ")
  if choice == '1':
   print("Adding new product")

menu()
main()