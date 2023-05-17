contador_mayus = 0
mayus = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
cadena = input("De una cadena para contar las mayusculas")

for letra in cadena:
    if letra in mayus:
        contador_mayus += 1
print("La cadena tiene {} mayusculas" .format(contador_mayus))