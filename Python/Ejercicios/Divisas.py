euro_dolar = 1.05
euro_libra = 0.85
dolar_euro = 0.95
dolar_libra = 0.81
libra_dolar = 1.23
libra_euro = 1.17

conversion_deseada = input("""elije el tipo de cambio que quieres
A = de euro a dolar
B = de euro a libra
C = de dolar a euro
D = de dolar a libra
E = de libra a dolar
f = de libra a euro""")

if conversion_deseada == "A":
    dinero = input("importe a convertir: ")
    dinero = float(dinero)
    conv = dinero * euro_dolar
    print(conv)

elif conversion_deseada == "B":
    dinero = input("importe a convertir: ")
    dinero = float(dinero)
    conv = dinero * euro_libra
    print(conv)

elif conversion_deseada == "C":
    dinero = input("importe a convertir: ")
    dinero = float(dinero)
    conv = dinero * dolar_euro
    print(conv)

elif conversion_deseada == "D":
    dinero = input("importe a convertir: ")
    dinero = float(dinero)
    conv = dinero * dolar_libra
    print(conv)

elif conversion_deseada == "E":
    dinero = input("importe a convertir: ")
    dinero = float(dinero)
    conv = dinero * libra_dolar
    print(conv)

elif conversion_deseada == "F":
    dinero = input("importe a convertir: ")
    dinero = float(dinero)
    conv_euro = dinero * libra_euro
    print(conv)
else:
    print("Debes esoger una conversión")
    exit()

