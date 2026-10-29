notas = {
    "Fischer" : [],
    "Smaha": [],
    "Iglesias": [],
    "Perez": [],
    "Campos": []
}

while True:
   print ("\n MENU ") 
   print ("1.Ver todas las notas")
   print ("2.Ver notas por apellido")
   print ("3.Cargar notas")
   print ("4.Promedio")
   print ("5.Salir")
   opcion = input("\n Ingrese una opcion: ")

   if opcion == 1:
      
      print ("\n NOTAS ALUMNOS  ")
      for alumno,lista in notas.item():
        if lista == []:
         print ("\nAlumno: {alumno}")
         print ("Notas: {notas}")
        else:
         print ("\n Alumno: {alumno}")
         print ("Notas: Notas aun no cargadas")

   elif opcion == 2:

     print ("\n NOTAS POR APELLIDO ")
     apellido = input("Ingrese el apellido del alumno: ")
     if apellido in notas:
       if notas[apellido] == ():
         print (f"{apellido}:{notas[apellido]}")
       else:
         print (f"{apellido}:No tiene sus notas cargadas aun")
     else:
        print ("El alumno no esta registrado")

   elif opcion == 3:
     
     print ("\n CARGA DE NOTAS")
     apellido = input ("Ingrese el apellido del alumno: ")
     if apellido in notas:
       notas[apellido] = []
       for i in range (1, 5):
         nota = int(input(f"Nota {i}: "))
         notas[apellido].append(nota)
     else: 
         print ("No existe el alumno")

   elif opcion == 4: 
     
     apellido = input ("Apellido: ")
     if apellido in notas:
       if len(notas[apellido]) == 0:
         print ("No hay notas para promediar")
       else:
         promedio = sum(notas[apellido]) / len(notas[apellido])
         print("Promedio:", promedio)
     else:
       print ("No existe el apellido ingresado")
   elif opcion == 5:
     print ("Saliendo . . .")
     break

         

       

    

         

    


     




