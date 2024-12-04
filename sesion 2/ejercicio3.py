def bonos (puntuaciones):
  bono =  puntuaciones*3000000
  return bono

def nivel_rendimiento (puntuaciones):
  if puntuaciones == 1.0 or puntuaciones == 1:
    nivel = "bajo"
  elif puntuaciones == 1.5:
    nivel = "medio"
  elif puntuaciones == 2.0 or puntuaciones == 2.5:
    nivel = "alto"
  else: 
    nivel = "excelente"
  
  return nivel;
  
puntuaciones = float(input("ingrese la puntuacion que sacaste: "))
rn=bonos(puntuaciones)
nb=nivel_rendimiento(puntuaciones)
print(f"tu bono es de {rn} y tu nivel es {nb}")
