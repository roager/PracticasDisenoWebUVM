class tarea3():
    def promedio(self, objetoCalificaciones):
        return sum(objetoCalificaciones) / len(objetoCalificaciones)

    def mostrar_calificaciones(self, objetoCalificaciones):
        for i in range(len(objetoCalificaciones)):
            print(f"Calificación {i + 1}: {objetoCalificaciones[i]}")   

    def actualizar_calificacion_especifica(self, objetoCalificaciones, indice, nueva_calificacion):
        objetoCalificaciones[indice] = nueva_calificacion

tarea = tarea3()

calificaciones = []
for i in range(5):
    calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
    calificaciones.append(calificacion)

tarea.mostrar_calificaciones(calificaciones)

print(f"El promedio de las calificaciones es: {tarea.promedio(calificaciones)}")

indiceCalificacion = int(input("Ingresa el índice de la calificación a actualizar (0 a 4): "))
calificacionNew = float(input(f"Ingresa la nueva calificación del estudiante {indiceCalificacion + 1}: "))

tarea.actualizar_calificacion_especifica(calificaciones, indiceCalificacion, calificacionNew)

tarea.mostrar_calificaciones(calificaciones)









#calificaciones = []
#longitudLista = int(input(f"Ingresa la longitud de la lista de calificaciones: "))
#for i in range(longitudLista):
#    calificacion = float(input(f"Ingresa la calificación {i + 1}: "))
#    calificaciones.append(calificacion)
#print(f"Lista de calificaciones: {calificaciones}")