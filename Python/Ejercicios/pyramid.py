def pyramid(number_floor):
    for n in range(number_floor):
        if n % 2 == 0:
            print(" " * ((number_floor - n - 1 ) // 2) + "*" * (n + 1) + " " * ((number_floor - n - 1) // 2))


def main():
    pyramid(int(input("¿Cuantas estrellas quieres en la última fila?")))


if __name__ == "__main__":
    main()