def sumar(a: int, b: int):
    suma = a + b 
    print("Suma completada... ")
    return suma

def main():
    print("Hello World!")

    print("Ahora haré una suma de dos variables. ")

    a = 5
    b = 10

    suma = sumar(a, b)

    print(f"La suma es {suma}")

if __name__ == "__main__":
    main()