# Comparación de Implementaciones: Ejercicios de Python

Este archivo compara tres implementaciones de código diferentes: dos ejemplos básicos de **Python** y un ejemplo de **Backend con FastAPI**. También se incluyen detalles de un ejercicio en un **Jupyter Notebook**.

## 1. **Ejercicio 1: Comparación de Valores (Jupyter Notebook)**

El **`Ejercicio1.ipynb`** solicita dos valores numéricos del usuario, luego los compara y muestra el resultado en función de si uno es mayor, menor o igual al otro.

### Implementación:
1. Se usan las funciones **`input()`** y **`print()`** para capturar y mostrar los valores ingresados por el usuario.
2. Los valores ingresados se comparan utilizando las sentencias condicionales `if`, `elif`, y `else`.
3. El código es ejecutado de forma interactiva en un **Jupyter Notebook**, donde el usuario ingresa los valores y se muestran los resultados de inmediato.

### Ejemplo de código en el notebook:

```python
valorA = input("Por favor, ingresa un valor para A: ")
print("El valor ingresado de valorA es:", valorA)

valorB = input("Por favor, ingresa un valor para B: ")
print("El valor ingresado de valorB es:", valorB)

if valorA == valorB:
    print(f"A y B son iguales: {valorA} = {valorB}")
elif valorA > valorB:
    print(f"A es mayor que B: {valorA} > {valorB}")
elif valorA < valorB:
    print(f"A es menor que B: {valorA} < {valorB}")
else:
    print("Los valores no son comparables.")
