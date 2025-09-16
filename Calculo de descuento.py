def calcular_descuento(monto_total, porcentaje_descuento=10):
    """
    Calcula el monto del descuento basado en el porcentaje dado.

    :param monto_total: float, monto total de la compra
    :param porcentaje_descuento: float, porcentaje de descuento (por defecto 10%)
    :return: float, monto del descuento
    """
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento


def main():
    # Primera llamada: solo monto total, usa descuento por defecto 10%
    monto1 = 1500.0
    descuento1 = calcular_descuento(monto1)
    total_pagar1 = monto1 - descuento1
    print(f"Compra 1: Monto total = ${monto1:.2f}")
    print(f"Descuento aplicado = ${descuento1:.2f}")
    print(f"Monto final a pagar = ${total_pagar1:.2f}\n")

    # Segunda llamada: monto total y porcentaje de descuento personalizado
    monto2 = 2000.0
    porcentaje2 = 15  # 15% de descuento
    descuento2 = calcular_descuento(monto2, porcentaje2)
    total_pagar2 = monto2 - descuento2
    print(f"Compra 2: Monto total = ${monto2:.2f}")
    print(f"Descuento aplicado ({porcentaje2}%) = ${descuento2:.2f}")
    print(f"Monto final a pagar = ${total_pagar2:.2f}")


if __name__ == "__main__":
    main()
