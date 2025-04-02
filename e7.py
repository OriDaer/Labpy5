def calcular_descuento(precio_original, porcentaje_descuento):
    descuento = precio_original * (porcentaje_descuento / 100)
    precio_final = precio_original - descuento
    return precio_final

def main():
    precio_original = float(input('Ingrese el precio original del artículo: '))
    porcentaje_descuento = float(input('Ingrese el porcentaje de descuento: '))

    precio_final = calcular_descuento(precio_original, porcentaje_descuento)

    print(f'El precio final después de aplicar un descuento de {porcentaje_descuento}% es: ${precio_final:.2f}')

if __name__ == '__main__':
    main()
