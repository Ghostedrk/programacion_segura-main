from data.conexion import leer_datos, insertar_datos
from prettytable import PrettyTable
from auxiliares.mensajes import sin_datos

def cargar_listado_docentes():
    consulta = "SELECT id, rut_docente, nombre_docente, email_docente FROM docentes WHERE habilitado = 1"
    lista_docentes = leer_datos(consulta)
    if lista_docentes is not None:
        return lista_docentes

def mostrar_listado_docentes():
    print()
    print('Listado de Docentes')
    tabla_docentes = PrettyTable()
    tabla_docentes.field_names = [
        'Id', 'RUT Docente', 'Nombre Docente', 'Email Docente']
    lista = cargar_listado_docentes()
    if lista is not None and len(lista) > 0:
        for docente in lista:
            docente_list = list(docente)
            if docente_list[3] is None:
                docente_list[3] = 'Sin Información'
            tabla_docentes.add_row(docente_list)  
        print(tabla_docentes)
    else:
        print(sin_datos)

def agregar_docente():
    mostrar_listado_docentes()
    rut_docente = input('Ingrese RUT del docente: ')
    nombre_docente = input('Ingrese nombre del docente: ')
    email_docente = input('Ingrese email del docente: ')

    consulta = '''
        INSERT INTO docentes (rut_docente, nombre_docente, email_docente, habilitado) VALUES
        (%s, %s, %s, %s)
    '''
    valores = (
        rut_docente.upper(),
        nombre_docente.title(),
        email_docente.lower(),
        1
    )

    if rut_docente and nombre_docente != '':
        insertar_datos(consulta, valores)

    mostrar_listado_docentes()

def actualizar_docente():
    mostrar_listado_docentes()
    try:
        id_docente = int(input('Ingrese el ID del docente a actualizar: '))
    except ValueError:
        print("ID inválido.")
        return

    consulta_verificacion = "SELECT * FROM docentes WHERE id = %s"
    resultado = leer_datos(consulta_verificacion, (id_docente,))
    if not resultado:
        print("No existe un docente con ese ID.")
        return

    nuevo_rut = input('Ingrese el nuevo RUT del docente: ').upper()
    nuevo_nombre = input('Ingrese el nuevo nombre del docente: ').title()
    nuevo_email = input('Ingrese el nuevo email del docente: ').lower()

    consulta = '''
        UPDATE docentes
        SET rut_docente = %s, nombre_docente = %s, email_docente = %s
        WHERE id = %s
    '''
    valores = (nuevo_rut, nuevo_nombre, nuevo_email, id_docente)
    insertar_datos(consulta, valores)
    print("Docente actualizado correctamente.")
    mostrar_listado_docentes()

def eliminar_docente():
    while True:
        mostrar_listado_docentes()
        try:
            id_docente = int(input('Ingrese el ID del docente a eliminar: '))
        except ValueError:
            print("ID inválido. Intente nuevamente.")
            continue

        consulta_verificacion = "SELECT * FROM docentes WHERE id = %s"
        resultado = leer_datos(consulta_verificacion, (id_docente,))
        if not resultado:
            print("No existe un docente con ese ID. Intente nuevamente.")
            continue

        confirmacion = input("¿Está seguro que desea eliminar el docente? (s/n): ").lower()
        if confirmacion == 's':
            consulta = "DELETE FROM docentes WHERE id = %s"
            insertar_datos(consulta, (id_docente,))
            print("Docente eliminado correctamente.")
        else:
            print("Eliminación cancelada.")
        mostrar_listado_docentes()
        break