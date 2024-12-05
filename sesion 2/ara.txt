productos = {}

def producto():
  nombre = input("ingrese el nombre de el producto que desea agregar:  ").upper() 
  if nombre in productos: 
    print ("el producto que deseas guardar ya se encuentra registrado...")
  else : 
    while True: 
      try:
        cantidad = int ( input ("ingrese la cantidad de el producto que desea agregar:  "))
        if cantidad <= 0:
          productos[nombre] = cantidad
          print (f"se ha agregado la cantidad de {cantidad} productos de {nombre}")
          break
        else:
          print("el valor a agregar debe ser positivo...")   
        print()
        precio = float ( input ("ingrese el precio de el producto que desea agregar:  "))
        if precio <= 0:
          productos[nombre] = precio
          print (f"se ha agregado el precio de {precio} pesos al procducto:  {nombre}")
          break
        else:
          print("el valor a agregar debe ser positivo...")
        break
      except ValueError:
        print("el valor ingresado esta mal. por favor intentelo nuevamente....")
def eliminar_producto():
  nombre = input("ingrese el nombre de el producto que desea eliminar:  ").upper()
  if nombre in productos:
    del productos[nombre]
    print (f"se ha eliminado el producto {nombre}")

def actualizar_cantidad():
  nombre = input("ingrese el nombre de el producto que desea actualizar:  ").upper()
  if nombre in productos:
    while True:
      try:
        cantidad = int ( input ("ingrese la cantidad de el producto que desea actualizar:  "))
        if cantidad <= 0:
          productos[nombre] = cantidad
          print (f"se ha actualizado la cantidad {cantidad} productos de {nombre}")
          break
        else: 
          print("el valor a agregar debe ser positivo...")
      except ValueError:
        print("el valor ingresado esta mal. por favor intentelo nuevamente....")

  else:
    print("el producto que desea actualizar no se ecuentra registrado...")

def productos_agotandose ():
  print("\nlos productos que estan por acabarsen son:  ")
  producto_terminadose = {nombre: cantidad for nombre, cantidad in productos.items()  if cantidad <= 5}
  if producto_terminadose:
    for nombre, cantidad in producto_terminadose.items():
        print(f"{nombre}: {cantidad}")
    else:
      print("no hay productos por acabarse")

def mostrar_inventario():
  print("\nel inventario de productos es:  ")
  
  if productos:
    for nombre, cantidad in productos.items():
      print(f"{nombre}: {cantidad}")
    else: 
      print("no hay productos en el inventario")

def menu ():
  print ("\f Bienvenido al inventario")
  print("1. agregar un producto")
  print("2. eliminar un producto")
  print("3. actualizar la cantidad de un producto")
  print("4. mostrar los productos que estan por acabarse")
  print("5. mostrar el inventario de productos")
  print("6. salir")

while True:
  menu()
  opcion = input("\n que desea realizar?:  ").strip()
  if opcion == "1":
    producto()
  elif opcion == "2":
    eliminar_producto()
  elif opcion == "3":
    actualizar_cantidad()
  elif opcion == "4":
    productos_agotandose()
  elif opcion == "5":
    mostrar_inventario()
  elif opcion == "6":
    print("gracias por usar el inventario")
  else:
    print("opcion no valida, vuelvalo a intentar")
    break
