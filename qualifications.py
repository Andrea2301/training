while True:
    try:
     calificacion = float(input(f"Ingrese su nota: "))
     if 0 <= calificacion <= 100:
        break
     else:
        print("¡ingrese una nota entre 0 y 100!")
    except ValueError:
       print("Entrada invalida. Ingrese un numero")

if calificacion >=75:
  print("¡Aprobado!")
else:
  print("¡Reprobado!")


  notas = input("Ingresa notas Ej: 23,23,5,2,3,")
  lista_notas = [float(n.strip())for n in notas.split(",") if n.strip()]

suma = 0
for nota in lista_notas:
   suma += nota
promedio = suma / len(lista_notas)
print(f"su promedio de notas es: {promedio:.2f}")


while True:
   try:
      valor = float(input("Ingrese un valor para comparar"))
      break
   except ValueError:
      print("ingrese un numero valido")

contador_Mayores= 0
for nota in lista_notas:
     if notas > valor:
      contador_Mayores += 1
      

      promedio = sum(lista_notas) / len(lista_notas)

      print(f"Cantidad de calificaciones mayores que{valor}:{contador_Mayores}")



    



