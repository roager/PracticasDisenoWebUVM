# Comparación de Implementaciones: Ejercicios de Python

Este archivo compara tres implementaciones de código diferentes: dos ejemplos básicos de **Python** y un ejercicio de **Jupyter Notebook**. También se incluye un ejemplo de código que suma los números del 1 al 10 usando un bucle.

## 1. **Ejercicio 1: Suma de los Números del 1 al 10 (Python Básico)**

El siguiente código suma los números del 1 al 10 usando un bucle **`for`**. Es una forma sencilla de realizar una suma secuencial.

### Implementación:
1. Se utiliza un bucle **`for`** para iterar sobre los números del 1 al 10.
2. La suma de los números se realiza dentro del bucle, acumulando el resultado en la variable **`suma`**.
3. Finalmente, se imprime el resultado de la suma total.

### Ejemplo de código:

```python
i = 0
suma = 0  

for i in range(1, 11):  
    suma += i  

print(f"La suma del conjunto de 1 a 10 es: {suma}")
