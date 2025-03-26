perro = {}

perro["nombre"]="max"
perro["color"]="cafe"
perro["raza"]="pastor velga"
perro["patas"]="4"
perro["edad"]="5"

print("Diccionario perro")

estudiante={
    "nombre" : "Fernando ",
    "apellido":"flores",
    "genero":"masculino",
    "edad":"18",
    "estado_civil":"soltero",
    "habilidades":"[python]",
    "pais":"Mexico",
    "ciudad":"Aguascalientes",
    "direccion": "Lomas del ajederez#225"
}

longitud_estudiante = len(estudiante)
print("Longitud del diccionario estudiante:", longitud_estudiante)

tipo_habilidades = type(estudiante['habilidades'])
print("Tipo de dato de habilidades:", tipo_habilidades)

estudiante['habilidades'].append('Análisis de Datos')
estudiante['habilidades'].append('Machine Learning')
print("Habilidades actualizadas:", estudiante['habilidades'])

claves_estudiante = list(estudiante.keys())
print("Claves del diccionario estudiante:", claves_estudiante)

valores_estudiante = list(estudiante.values())
print("Valores del diccionario estudiante:", valores_estudiante)

tuplas_estudiante = list(estudiante.items())
print("Diccionario como lista de tuplas:", tuplas_estudiante)

estudiante.pop('estado_civil')
print("Diccionario estudiante después de eliminar estado civil:", estudiante)

del perro
print("Diccionario perro eliminado.")
