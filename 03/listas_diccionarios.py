# Ejemplo de operaciones básicas con listas y diccionarios en Python

def main():
    """
    Función principal para ejecutar el ejemplo.
    Ejecutar utilizando breakpoints y observar como cambian los objetos con cada instrucción. 
    """
    
    # Operaciones con listas
    print("Operaciones con listas:")
    frutas = ["manzana", "plátano", "naranja"]  # Crear una lista
    print("Lista inicial:", frutas)

    frutas.append("pera")  # Agregar un elemento
    print("Después de agregar 'pera':", frutas)

    frutas.pop()  # Eliminar el último elemento
    print("Después de usar pop():", frutas)

    frutas.insert(1, "fresa")  # Insertar un elemento en un índice específico
    print("Después de insertar 'fresa' en la posición 1:", frutas)

    print("Elemento en la posición 1:", frutas[1])  # Acceder a un elemento por índice

    # Operaciones con diccionarios
    print("\nOperaciones con diccionarios:")
    estudiante = {"nombre": "Juan", "edad": 20, "curso": "Matemáticas"}  # Crear un diccionario
    print("Diccionario inicial:", estudiante)

    estudiante["edad"] = 21  # Modificar un valor
    print("Después de actualizar la edad:", estudiante)

    estudiante["ciudad"] = "Ciudad de México"  # Agregar un nuevo par clave-valor
    print("Después de agregar 'ciudad':", estudiante)

    valor_curso = estudiante.pop("curso", "No disponible")  # Eliminar un par clave-valor con pop
    print("Después de eliminar 'curso' con pop():", estudiante)
    print("Valor eliminado (curso):", valor_curso)

    # Usar .get para acceder a valores de forma segura
    ciudad = estudiante.get("ciudad", "No especificado")
    print("Ciudad del estudiante (usando get):", ciudad)

    estado = estudiante.get("estado", "No especificado")
    print("Estado del estudiante (usando get):", estado)

    # Listas de diccionarios
    print("\nListas de diccionarios:")
    estudiantes = [
        {"nombre": "Juan", "edad": 21},
        {"nombre": "María", "edad": 22},
        {"nombre": "Pedro", "edad": 20}
    ]
    print("Lista inicial de diccionarios:", estudiantes)

    # Agregar un nuevo diccionario a la lista
    estudiantes.append({"nombre": "Ana", "edad": 23})
    print("Después de agregar un nuevo estudiante:", estudiantes)

    # Acceder a un elemento en la lista de diccionarios
    print("Nombre del primer estudiante:", estudiantes[0]["nombre"])

    # Actualizar el nombre del segundo estudiante
    estudiantes[1]["nombre"] = "Maria Fernanda"
    print("Después de actualizar el nombre del segundo estudiante:", estudiantes)

if __name__ == "__main__":
    main()
