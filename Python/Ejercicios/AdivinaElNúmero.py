import random


def adivina():
    return int(input("Intenta adivinar el número"))


def main():
    adivina()
    numero_magico = random.randint(0,10)
    while adivina() != numero_magico:
        adivina()
    print("Haz adivinado el número")


if __name__ == "__main__":
    main()