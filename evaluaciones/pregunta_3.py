import math

def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_volumen_cilindro(radio, altura):
    area_base = calcular_area_circulo(radio)
    volumen = area_base * altura
    return volumen

def ejecutar_calculadora_geometrica():
    
    print('Bienvenido a la calculadora de Geometría')
    print('¿Qué deseas calcular?')
    print('1. Área de un círculo')
    print('2. Volumen d un cilindro')

    while True:
        opcion = input('Elige una opción (1 o 2): ')
        if opcion in ('1', '2'):
            break
        else:
            print('Opcion invalida. Por favor, elige 1 o 2.')

    while True:
        try:
            radio_str = input('Ingresa el radio: ')
            radio = float(radio_str)
            if radio < 0:
                print('El radio no puede ser negativo. Inténtelo de nuevo.')
                continue
            break
        except ValueError:
            print('Ingreso invalido. Por favor, ingresa un número para el radio.')
    
    if opcion == '1':
        area_calculada = calcular_area_circulo(radio)
        print(f'\nEl área del círculo con radio {radio:.2f} es: {area_calculada:.2f}')
    elif opcion == '2':
        while True:
            try:
                altura_str = input('Ingresa la altura del cilindro: ')
                altura = float(altura_str)
                if altura < 0:
                    print('La altura no puede ser negativa. Intentelo de nuevo.')
                    continue
                break
            except ValueError:
                print('Ingreso inválido. Por favor, ingresa un número para la altura.')

        volumen_calculado = calcular_volumen_cilindro(radio, altura)
        print(f'\nEl volumen del cilindro con radio {radio:.2f} y altura {altura:.2f} es: {volumen_calculado:.2f}')

ejecutar_calculadora_geometrica()