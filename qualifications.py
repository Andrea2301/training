while True:  # Validate a single grade
    try:
     qualification = float(input(f"enter note: "))
     if 0 <= qualification <= 100:
        break
     else:
        print("¡Enter a grade between 0 and 100!")
    except ValueError:
       print("Invalid entry. Please enter a number.")

# Check if the grade is passing or failing
if qualification >=75:
  print("¡approved!")
else:
  print("¡failed!")

   # Input multiple grades separated by commas
notes = input("Enter notes: ")
list_notes = [float(n.strip())for n in notes.split(",") if n.strip()]

    # Calculate the average of the grades
suma = 0
for nota in list_notes:
   suma += nota
average = suma / len(list_notes)
print(f"your grade point average is: {average:.2f}")

    # Prompt the user to enter a value for comparison
while True:
    entrance = input("Enter a value to compare: ")
    if not entrance.strip():  # Si está vacío o solo espacios
        print("No number was entered.")
        continue
    try:
        valor = float(entrance)
        break
    except ValueError:
        print("Please enter a valid number.")

    # Count how many grades are greater than the comparison value
counter_Majors= 0
for nota in list_notes:
     if nota > valor:
      counter_Majors += 1

 
    # Display the result of the comparison     
if counter_Majors >0:
 print(f"Cantidad de calificaciones mayores que: {valor}:{counter_Majors}")
else:
   print(f"No se encontaron calificaiones mayores a {valor}. ")

#

     




    



