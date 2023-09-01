import random


numPerros=0
datosPoliperros = {
  "nombre":[],
  "huellaDactilar":[]
}

fotosPoliperros = {
  "foto":[]
}

print("------------ POLIPERROS -------------")
print("\n\t\t *** Bienvenido(a) ***\n")

print("¿Que acción desea realizar?")
print(f'*  1) Registrar poliperros')
print(f'*  2) Mostrar poliperros')
print(f'*  3) Registrar foto del poliperro')
print(f'*  4) Guardar en archivo')
print(f'*  5) Salir del sistema')
tipoAccion=int(input("Ingrese la opción: "))



while tipoAccion !=5:
  
  if tipoAccion == 1:
    numPerros = int(input("Ingrese el número de poliperros a registrar: "))
    for i in range(numPerros):
      print("Ingrese los datos del poliperro", i + 1)
      nombre = input("Nombre: ")
      huellaDactilar = input("huellaDactilar: ")
  
      datosPoliperros['nombre'].append(nombre)
      datosPoliperros['huellaDactilar'].append(huellaDactilar)

    print("¿Que acción desea realizar?")
    print(f'*  1) Registrar poliperros')
    print(f'*  2) Mostrar poliperros')
    print(f'*  3) Registrar foto del poliperro')
    print(f'*  4) Guardar en archivo')
    print(f'*  5) Salir del sistema')
    tipoAccion=int(input("Ingrese la opción: "))
  
  elif tipoAccion == 2:
    
    for i in range(numPerros):
      print("-------------------------------------")
      print("Mostrando los datos del poliperro", i + 1)
      print("* Nombre:", datosPoliperros['nombre'][i])
      print("* Huella dactilar:", datosPoliperros['huellaDactilar'][i])
      if("foto" in datosPoliperros):
        print("* Foto: ",fotosPoliperros['foto'][i])
      print("-------------------------------------")
      
    print("¿Que acción desea realizar?")
    print(f'*  1) Registrar poliperros')
    print(f'*  2) Mostrar poliperros')
    print(f'*  3) Registrar foto del poliperro')
    print(f'*  4) Guardar en archivo')
    print(f'*  5) Salir del sistema')
    tipoAccion=int(input("Ingrese la opción: "))
    
  elif tipoAccion == 3:
    
    for i in range(numPerros):
      print("Ingrese la foto para el poliperro", i + 1)
      print("¿El poliperro disponde de foto?")
      foto = input("Ingrese si o no: ")
      if(foto=="si"):
        foto = input("Foto: ")
        fotosPoliperros['foto'].append(foto)
      else:
        fotosPoliperros['foto'].append("foto-prueba.jpg")
        
    datosPoliperros.update(fotosPoliperros)
    print("¿Que acción desea realizar?")
    print(f'*  1) Registrar poliperros')
    print(f'*  2) Mostrar poliperros')
    print(f'*  3) Registrar foto del poliperro')
    print(f'*  4) Guardar en archivo')
    print(f'*  5) Salir del sistema')
    tipoAccion=int(input("Ingrese la opción: "))
  elif tipoAccion == 4:
    archivo = open("C:/Users/ALGORITMOS/Downloads/python/perro/poliperro.txt", 'w')
    for i in range(numPerros):
        archivo.write(f"Poliperro {i + 1}:\n")
        archivo.write(f"Nombre: {datosPoliperros['nombre'][i]}\n")
        archivo.write(f"Huella dactilar: {datosPoliperros['huellaDactilar'][i]}\n")
        if "foto" in datosPoliperros and i < len(datosPoliperros['foto']):
            archivo.write(f"Foto: {datosPoliperros['foto'][i]}\n")
        archivo.write("\n")
    
    archivo.close()
    
    print("Los datos de los poliperros se han guardado en el archivo 'poliperro.txt'.")
    
    print("¿Que acción desea realizar?")
    print(f'*  1) Registrar poliperros')
    print(f'*  2) Mostrar poliperros')
    print(f'*  3) Registrar foto del poliperro')
    print(f'*  4) Guardar en archivo')
    print(f'*  5) Salir del sistema')
    tipoAccion = int(input("Ingrese la opción: "))
    
print("Muchas gracias")
