'''

Ejercicio 1: Registro de calificaciones
Supón que necesitas registrar las calificaciones de los alumnos en una materia
específica. Se te pide crear un programa que permita almacenar las notas de los
alumnos y realice algunas operaciones básicas con estas notas.

Requerimientos:
1 Crear un array para almacenar las calificaciones de 5 alumnos.
2 Pedir al usuario ingresar las calificaciones de los 5 alumnos.
3 Mostrar por pantalla todas las calificaciones ingresadas.
4 Calcular y mostrar el promedio de las calificaciones.
5 Pedir al usuario modificar la calificación de un alumno específico.
6 Mostrar por pantalla la lista actualizada de notas.
'''

# 1 Crear un array para almacenar las calificaciones de 5 alumnos. 

calificaciones = []

# 2 Pedir al usuario ingresar las calificaciones de los 5 alumnos.

def ingresar_calificaciones(index: int, calificacion: float):
    calificaciones.insert(index, calificacion)
    return calificaciones
   
ingresar_calificaciones(0, 10)
ingresar_calificaciones(1, 8)
ingresar_calificaciones(2, 7)
ingresar_calificaciones(3, 5.5)
ingresar_calificaciones(4, 6)

# 3 Mostrar por pantalla todas las calificaciones ingresadas.
print(f'Las calificaciones son {calificaciones}')

# 4 Calcular y mostrar el promedio de las calificaciones.

def calcular_promedio(calificaciones: list):
    if len(calificaciones) == 0:  
        print('No hay calificaciones capturadas')
        return None
    promedio = sum(calificaciones) / len(calificaciones)  
    print(f'El promedio de las calificaciones es {promedio}')
    return promedio

calcular_promedio(calificaciones)

# 5 Pedir al usuario modificar la calificación de un alumno específic. (lo hice por indice en la lista de calificaciones)

def modificar_calificacion(index: int, calificacion: float):
    calificaciones[index] = calificacion
    
    return calificaciones

modificar_calificacion(0, 5)

# 6 Mostrar por pantalla la lista actualizada de notas.
print(f'Las calificaciones se han modificado, Nuevas calificaciones: {calificaciones}')
