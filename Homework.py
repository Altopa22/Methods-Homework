def sumar(x, y):
    return x + y

def restar(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Error: No se puede dividir entre cero"
    return x / y

while True:
    num1 = int(input('Introduce el primer número: '))
    num2 = int(input('Introduce el segundo número: '))
    operacion = int(input("Selecciona la operación a realizar:\n 1) Sumar\n 2) Restar\n 3) Multiplicar\n 4) Dividir\n"))

    if operacion == 1:
        resultado = sumar(num1, num2)
        tipo_operacion = "suma"
    elif operacion == 2:
        resultado = restar(num1, num2)
        tipo_operacion = "resta"
    elif operacion == 3:
        resultado = multiplicar(num1, num2)
        tipo_operacion = "multiplicación"
    elif operacion == 4:
        resultado = dividir(num1, num2)
        tipo_operacion = "división"
    else:
        resultado = None
        tipo_operacion = "operación no válida"

    if resultado is not None:
        print(f"El resultado de la {tipo_operacion} entre {num1} y {num2} es: {resultado}")
    else:
        print("Has seleccionado una operación no válida.")

    continuar = input("¿Quieres realizar otra operación? (s/n): ")
    if continuar.lower() != 's':
        break

print("Gracias por usar nuestra calculadora.")
