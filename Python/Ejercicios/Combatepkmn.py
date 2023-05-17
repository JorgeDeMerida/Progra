import random
import os

vida_inicial_pikachu = 80
vida_inicial_squirtle = 90

vida_pikachu = 80
vida_squirtle = 90

while vida_squirtle > 0 and vida_pikachu > 0:
    print("turno de pikachu")
    ataque_pikachu = random.randint(1,2)

    if ataque_pikachu == 1:
        print("pikachu usó bola voltio")
        vida_squirtle -= 10
    else:
        print("pikachu uso onda trueno")
        vida_squirtle -= 11

    print("la vida de pikachu es {}, la vida de squirtle es {}" .format(vida_pikachu, vida_squirtle))

    barra_vida_pikachu = 10 * vida_pikachu / vida_inicial_pikachu
    barra_vida_squirtle = 10 * vida_squirtle / vida_inicial_squirtle
    print("pikachu    [{}{}]" .format("*" * int(barra_vida_pikachu), " " * (10 - int(barra_vida_pikachu))))
    print("squirtle    [{}{}]" .format("*" * int(barra_vida_squirtle), " " * (int(10 - barra_vida_squirtle))))

    input("Enter para continuar...")
    os.system("cls")
    print("Turno de squirtle")

    ataque_squirtle = None

    while ataque_squirtle not in ["A", "P", "B", "N"]:
        ataque_squirtle = input("¿Que ataque deseas usar? P = placaje A = pistola agua B = burbuja N = No hacer nada")

    if ataque_squirtle == "P":
        print("Squirtle uso placaje")
        vida_pikachu -= 10

    elif ataque_squirtle == "A":
        print("squirtle uso pístola agua")
        vida_pikachu -= 12

    elif ataque_squirtle == "B":
        print("squirtle uso burbuja")
        vida_pikachu -= 9
    elif ataque_squirtle == "N":
        print("squirtle no hace nada")

    print("la vida de pikachu es {}, la vida de squirtle es {}" .format(vida_pikachu, vida_squirtle))

if vida_pikachu > vida_squirtle:
    print("gana pikachu")
else:
    print("gana squirtle")

    input("Enter para continuar...")
    os.system("cls")