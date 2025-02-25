def suma(num1,num2):
  return num1 + num2

def resta(num1,num2):
  return num1 - num2

def multiplicacion(num1,num2):
  return num1 * num2

def division(num1,num2):
  if num2 == 0:
    return "No se puede dividir por cero"
  return num1 / num2

def calculadora():
  print("Bienvenido a la calculadora")
  print("1. Suma")
  print("2. Resta")
  print("3. Multiplicación")
  print("4. División")

  while True:
    opcion = input("Seleccione una opción 1-4 o pulsa Q para salir: ")
    if opcion == "Q":
      print("Gracias por usar la calculadora")
      break
    if opcion not in ["1","2","3","4"]:
      print("Opción no válida")
      continue
    num1 = int(input("ingrese el primer numero: "))
    num2 = int(input("ingrese el segundo numero: "))

    if opcion == "1":
      print(suma(num1,num2))
    elif opcion == "2":
      print(resta(num1,num2))
    elif opcion == "3":
      print(multiplicacion(num1,num2))
    elif opcion == "4":
     print(division(num1,num2))
calculadora()
