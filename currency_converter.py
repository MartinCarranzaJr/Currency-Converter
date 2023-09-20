def convertir_dolares_a_lempiras(dolares):
    tasa_cambio = 24.72
    return dolares * tasa_cambio


def solicitar_input(mensaje):
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Por favor, introduce un número válido.")


def main():
    print("Bienvenidos a mi tercer programa en Python")
    print("Este programa es un convertidor de divisas de dólares a Lempira de Honduras")

    Dolar = solicitar_input("Ingresa cantidad en dólares aquí: ")
    Lempira = convertir_dolares_a_lempiras(Dolar)

    print("Cambio a Lempiras es {:.2f}".format(Lempira))


if __name__ == "__main__":
    main()
