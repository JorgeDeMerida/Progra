SALIDA = "SALIR"

lista_compra = []


def exportar(nombre):
    expo = open("{}.txt" .format(nombre), "w")
    expo.write("\n" .join(lista_compra))
    expo.close()


def preguntar_producto_usuario():
    return input("Introduce un producto [{} para salir]" .format(SALIDA))


def main():
    input_usuario = preguntar_producto_usuario()

    while input_usuario != SALIDA:
        lista_compra.append(input_usuario)
        print("\n".join(lista_compra))
        input_usuario = preguntar_producto_usuario()

    exportar(input("Nombre del archivo"))


if __name__ == "__main__":
    main()