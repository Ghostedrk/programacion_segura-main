listado_docentes = """
SELECT id, rut_docente, nombre_docente, email_docente
FROM docentes
WHERE habilitado = 1
"""