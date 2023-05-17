cadena = input("De una cadena para contar")
espacios = " "
comas = ","
vocales = "aeiou"

contador_espacios = 0
contador_comas = 0
contador_vocales = 0

for letra in cadena:
    if letra in espacios:
        contador_espacios += 1
    elif letra in comas:
        contador_comas += 1
    elif letra in vocales:
        contador_vocales += 1

print("la cadena tiene {} espacios, {} comas. {} vocales" .format(contador_espacios, contador_comas, contador_vocales))
