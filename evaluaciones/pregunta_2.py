def calcular_total_factura():
    
    print("Calculadora de Facturas con IVA")

    while True:
        try:
            cantidad_sin_iva_str = input("Ingresa la cantidad sin IVA (ejemplo: 100.50): ")
            cantidad_sin_iva = float(cantidad_sin_iva_str)
            if cantidad_sin_iva < 0:
                print("La cantidad no puede ser negativa. Intenta de nuevo.")
                continue
            break 
        except ValueError:
            print("Eso no parece un número válido. Intenta de nuevo.")

    porcentaje_iva_str = input("Ingresa el porcentaje de IVA a aplicar (ejemplo: 19). Deja en blanco para usar 21%: ")

    if porcentaje_iva_str == "":
        porcentaje_iva = 21 
        print("No ingresaste un porcentaje de IVA, se aplicará el 21%.")
    else:
        try:
            porcentaje_iva = float(porcentaje_iva_str)
            if porcentaje_iva < 0:
                print("El porcentaje de IVA no puede ser negativo. Se usará 21% por defecto.")
                porcentaje_iva = 21
        except ValueError:
            print("Eso no es un número válido para el IVA. Se aplicará el 21% por defecto.")
            porcentaje_iva = 21 

    factor_iva = porcentaje_iva / 100

    monto_iva = cantidad_sin_iva * factor_iva
    total_factura = cantidad_sin_iva + monto_iva

    print("\nResumen de la Factura")
    print(f"Cantidad sin IVA: ${cantidad_sin_iva:.2f}")
    print(f"Porcentaje de IVA aplicado: {porcentaje_iva:.0f}%") 
    print(f"Monto del IVA: ${monto_iva:.2f}")
    print(f"Total de la factura (con IVA): ${total_factura:.2f}")

calcular_total_factura()