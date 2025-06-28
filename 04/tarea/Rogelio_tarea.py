# Prueba Rogelio Guzman - para dar PUSH al Repositorio...


# Ejercicio 1: Registro de calificaciones
# Supón que necesitas registrar las calificaciones de los alumnos en una materia
# específica. Se te pide crear un programa que permita almacenar las notas de los
# alumnos y realice algunas operaciones básicas con estas notas.
# Requerimientos:
# 1 Crear un array para almacenar las calificaciones de 5 alumnos.
# 2 Pedir al usuario ingresar las calificaciones de los 5 alumnos.
# 3 Mostrar por pantalla todas las calificaciones ingresadas.
# 4 Calcular y mostrar el promedio de las calificaciones.
# 5 Pedir al usuario modificar la calificación de un alumno específico.
# 6 Mostrar por pantalla la lista actualizada de notas.
# prueba para black formatter
print("ROGELIO GUZMAN J -  UVM")
print(
    "PROGRAMA QUE PIDE, MUESTRA, PROMEDIA, MODIFICA Y ACTUALIZA CALIFICACIONES DE 5 ALUMNOS de la UVM"
)


# Función para calcular el promedio
def calcular_promedio(calificaciones):
    return sum(calificaciones) / len(calificaciones)


# 1 ARRAY -  Lista para almacenar los nombres y calificaciones
alumnos = []
calificaciones = []

# 2 Pedir nombre y calificación de 5 alumnos
for i in range(5):
    nombre = input(f"Ingrese el 'NOMBRE' del alumno {i + 1}: ")
    calificacion = float(input(f"Ingrese la 'CALIFICACION' de {nombre}: "))
    alumnos.append(nombre)
    calificaciones.append(calificacion)


# 3  Mostramos los resultados
print("\nLa Lista de alumnos y sus calificaciones es la siguiente... :")
for i in range(5):
    print(f"Nombre: {alumnos[i]}, Calificación: {calificaciones[i]}")


# 4 Calcular y mostrar el promedio inicial
promedio_inicial = calcular_promedio(calificaciones)
print(f"\nEl promedio inicial de las calificaciones es: {promedio_inicial:.2f}")

# 5  Opción para modificar calificaciones
modificar = input("\n¿Desea modificar alguna calificación? (si/no): ").strip().lower()

if modificar == "si":
    while True:
        nombre_modificar = input(
            "Ingrese el NOMBRE del alumno cuya calificación desea modificar (o teclee 'listo' para terminar): "
        )
        if nombre_modificar.lower() == "listo":
            break
        if nombre_modificar in alumnos:
            nueva_calificacion = float(
                input(f"Ingrese la NUEVA calificación para {nombre_modificar}: ")
            )
            index = alumnos.index(nombre_modificar)
            calificaciones[index] = nueva_calificacion
            print(f"La calificación de {nombre_modificar} ha sido actualizada.")
        else:
            print("Alumno no encontrado. Intente de nuevo.")

    # Calcular y mostrar el nuevo promedio
    nuevo_promedio = calcular_promedio(calificaciones)
    print(f"\nEl NUEVO promedio de las calificaciones es: {nuevo_promedio:.2f}")
else:
    print(" FIN. Gracias por usar el programa")

# Mostrar por pantalla la lista actualizada de CALIFICACIONES.
print(f"Las calificaciones se han modificado, Nuevas calificaciones: {calificaciones}")

# 6 Mostramos los resultados actualizados en forma de lista actualizada
print("\nLa Lista de alumnos y sus calificaciones es la siguiente... :")
for i in range(5):
    print(f"Nombre: {alumnos[i]}, Calificación: {calificaciones[i]}")

print(" FIN. Gracias por usar el programa")
