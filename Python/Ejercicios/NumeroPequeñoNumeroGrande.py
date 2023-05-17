lista_numeros = []
numero_a_añadir = None

while numero_a_añadir != "Q":
    numero_a_añadir = input("Escriba el numero que desea añadir. Pulse [Q] para salir")
    if numero_a_añadir != "Q":
        numero_a_añadir = int(numero_a_añadir)
        lista_numeros.append(numero_a_añadir)
        print(lista_numeros)

numero_mayor = max(lista_numeros)
numero_menor = min(lista_numeros)

print("La lista de números es {}. El numero más grande es: {}, el más pequeño es: {}" .format(lista_numeros, numero_mayor, numero_menor))