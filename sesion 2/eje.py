def grupo_pais (pais, nombre):
  pais = pais.lower()
  if pais == "colombia" and len(nombre) < 5:
    return "pertenece al grupo A precios@😍:  "
  elif pais == "mexico" and len(nombre) >= 5:
    return "pertenece al grupo B chango 🐒: "
  else: 
    return "pertenece al grupo C mi pololo"

pais = input("ingrese cual es su pais de origen 🌆: ").lower()
nombre = input("Ingrese su nombre 🔠: ")
grupos= grupo_pais(pais, nombre)
print(f"la persona de nombre {nombre} de pais de origen {pais}, {grupos} ")
