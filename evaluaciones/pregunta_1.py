def calcular_estadisticas_principiante():
   
    numeros_str = input("Ingresa los números separados por comas (ejemplo: 10,20,30,40): ")
    
    try:
        lista_numeros = [float(num.strip()) for num in numeros_str.split(',')]
    except ValueError:
        print("Error: Asegúrate de ingresar solo números separados por comas.")
        return 

    if not lista_numeros:
        print("No se ingresaron números. No se pueden calcular las estadísticas.")
        return

    n = len(lista_numeros)

    print("\nCalculando la Media")
    suma_total = 0
    for numero in lista_numeros:
        suma_total = suma_total + numero
    
    media = suma_total / n
    print(f"La suma total de los números es: {suma_total}")
    print(f"El número de elementos (n) es: {n}")
    print(f"La media es: {media:.2f}") 

    print("\nCalculando la Varianza")
    suma_diferencias_cuadrado = 0
    for numero in lista_numeros:
        diferencia = numero - media
        diferencia_cuadrado = diferencia ** 2
        suma_diferencias_cuadrado = suma_diferencias_cuadrado + diferencia_cuadrado
        print(f"Número: {numero}, Diferencia con la media ({media:.2f}): {diferencia:.2f}, Diferencia al cuadrado: {diferencia_cuadrado:.2f}")

    if n > 1:
        varianza = suma_diferencias_cuadrado / (n - 1)
        print(f"La suma de las diferencias al cuadrado es: {suma_diferencias_cuadrado:.2f}")
        print(f"Dividimos por (n-1): {n-1}")
        print(f"La varianza es: {varianza:.2f}")
    else:
        varianza = 0.0 
        print("Solo hay un número, la varianza es 0.")
        print(f"La varianza es: {varianza:.2f}")

    print("\nCalculando la Desviación Típica")
    desviacion_tipica = varianza ** 0.5 
    print(f"La desviación típica (raíz cuadrada de la varianza) es: {desviacion_tipica:.2f}")

    resultados = {
        "media": round(media, 2), 
        "varianza": round(varianza, 2),
        "desviacion_tipica": round(desviacion_tipica, 2)
    }
    print("\nResultados Finales")
    print("Diccionario de resultados:", resultados)

calcular_estadisticas_principiante()