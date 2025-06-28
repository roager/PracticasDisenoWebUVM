i=0
promedioCalifs=0
arregloCalificaciones = [0] * 5

print("Dame las calificaciones de los 5 alumnos")
for i in range(len(arregloCalificaciones)):
    arregloCalificaciones[i] = int(input(f"Ingresa la calificación del alumno {i+1}: "))
    promedioCalifs = promedioCalifs + arregloCalificaciones[i]


promedioCalifs = promedioCalifs/5
print("Las calificaciones son: ")
print(str(arregloCalificaciones) + "")

print("El promedio de calificaciones es: " + str(promedioCalifs))

print("Por favor cambia el número de calificación de uno de los alumnos. Del 1 al 5, indica cuál vas a modificar:")
i = int(input())

print("Dame su nueva calificación")

arregloCalificaciones[i-1]= int(input())

print("Las nuevas calificaciones son: ")
print(str(arregloCalificaciones) + "")


