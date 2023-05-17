def fibonacci(largo):
    lista_fibonacci = [0,1]
    for n in range(0, largo):
        suma_fibonacci = lista_fibonacci[n] + lista_fibonacci[n + 1]
        lista_fibonacci.append(suma_fibonacci)
        print(lista_fibonacci[n])

def main():
    fibonacci(int(input("Posicion en fibonacci")))

if __name__ == "__main__":
    main()