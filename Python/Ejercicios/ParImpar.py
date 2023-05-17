def es_impar(numero):
    if int(numero) % 2 == 1:
        return 1
    else:
        return 0

def main():
    if es_impar(int(input("prueba de impares"))) == 1:
        print(bool(1))
    else:
        print(bool(0))

if __name__ == "__main__":
    main()