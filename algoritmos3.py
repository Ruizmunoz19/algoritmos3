
#Conversor de Unidades: Crea una aplicación que convierta entre diferentes unidades, como conversor de monedas, de unidades de medida, etc.
def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9/5) + 32
    return fahrenheit

def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5/9
    return celsius

def main():
    temperatura = float(input("Ingresa la temperatura: "))
    unidad = input("Ingresa la unidad de medida (C para Celsius, F para Fahrenheit): ").upper()

    if unidad == "C":
        fahrenheit = celsius_to_fahrenheit(temperatura)
        print(f"{temperatura} grados Celsius equivalen a {fahrenheit} grados Fahrenheit.")
    elif unidad == "F":
        celsius = fahrenheit_to_celsius(temperatura)
        print(f"{temperatura} grados Fahrenheit equivalen a {celsius} grados Celsius.")
    else:
        print("Unidad de medida no válida. Por favor, ingresa 'C' para Celsius o 'F' para Fahrenheit.")

if __name__ == "__main__":
    main()