desea_comprar = None
lista_compra = []

while desea_comprar != "Q":
    desea_comprar = input("¿Que desea comprar? (Q) para salir")
    if desea_comprar == "Q":
        print(lista_compra)
    else:
        añadir_compra = input("¿Desea añadir {} a la lista de compra? (S/N)" .format(desea_comprar))
        if añadir_compra == "S":
            lista_compra.append(desea_comprar)