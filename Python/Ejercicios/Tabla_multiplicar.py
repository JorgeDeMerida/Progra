numero_multiplicar = int(input("Número a multiplicar"))

for n in range(1,11):
    multiplicacion = n * numero_multiplicar
    print("{} x {} = {}" .format(numero_multiplicar, n, multiplicacion))