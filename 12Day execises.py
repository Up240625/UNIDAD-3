import random
def id_usuario_aleatorio():
    caracteres = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    id_generado = ''
    contador = 0
    while contador < 6:
        id_generado = id_generado + random.choice(caracteres)
        contador = contador + 1
    return id_generado

def generar_ids_usuario():
    caracteres = 'amcrefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
    num_chars = int(input("Ingrese el número de caracteres: "))
    num_ids = int(input("Ingrese el número de IDs a generar: "))
    lista_ids = []
    contador_ids = 0
    while contador_ids < num_ids:
        id_generado = ''
        contador_caracteres = 0
        while contador_caracteres < num_chars:
            id_generado = id_generado + random.choice(caracteres)
            contador_caracteres = contador_caracteres + 1
        lista_ids.append(id_generado)
        contador_ids = contador_ids + 1
    return lista_ids

def color_rgb_aleatorio():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = "rgb(" + str(r) + "," + str(g) + "," + str(b) + ")"
    return color

def lista_colores_hexadecimales(n):
    caracteres = '0123456789amcref'
    lista_colores = []
    contador = 0
    while contador < n:
        color = '#'
        contador_caracteres = 0
        while contador_caracteres < 6:
            color = color + random.choice(caracteres)
            contador_caracteres = contador_caracteres + 1
        lista_colores.append(color)
        contador = contador + 1
    return lista_colores

def lista_colores_rgb(n):
    lista_colores = []
    contador = 0
    while contador < n:
        lista_colores.append(color_rgb_aleatorio())
        contador = contador + 1
    return lista_colores

def generar_colores(tipo_color, n):
    if tipo_color == 'hexa':
        return lista_colores_hexadecimales(n)
    else:
        if tipo_color == 'rgb':
            return lista_colores_rgb(n)
        else:
            return "Tipo de color no válido"

def mezclar_lista(lista):
    lista_mezclada = []
    while len(lista) > 0:
        elemento = random.choice(lista)
        lista.remove(elemento)
        lista_mezclada.append(elemento)
    return lista_mezclada

def numeros_aleatorios_unicos():
    numeros = [0,1,2,3,4,5,6,7,8,9]
    seleccionados = []
    contador = 0
    while contador < 7:
        numero = random.choice(numeros)
        numeros.remove(numero)
        seleccionados.append(numero)
        contador = contador + 1
    return seleccionados