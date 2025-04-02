def sumar_dos_numeros(a, b):
    resultado = a + b
    return resultado

def area_circulo(r):
    import math
    area = math.pi * r * r
    return area

def sumar_todos(*args):
    for numero in args:
        if not isinstance(numero, (int, float)):
            return "Todos los elementos deben ser números."
    suma = 0
    for numero in args:
        suma += numero
    return suma
def convertir_celsius_a_fahrenheit(c):
    fahrenheit = (c * 9/5) + 32
    return fahrenheit

def determinar_estacion(mes):
    if mes in ['Septiembre', 'Octubre', 'Noviembre']:
        return "Otoño"
    elif mes in ['Diciembre', 'Enero', 'Febrero']:
        return "Invierno"
    elif mes in ['Marzo', 'Abril', 'Mayo']:
        return "Primavera"
    elif mes in ['Junio', 'Julio', 'Agosto']:
        return "Verano"
    else:
        return "Mes no válido"


def calcular_pendiente(x1, y1, x2, y2):
    pendiente = (y2 - y1) / (x2 - x1)
    return pendiente

def resolver_ecuacion_cuadratica(a, b, c):
    import math
    discriminante = b**2 - 4*a*c
    if discriminante < 0:
        return "No hay soluciones reales"
    elif discriminante == 0:
        return -b / (2*a)
    else:
        raiz1 = (-b + math.sqrt(discriminante)) / (2*a)
        raiz2 = (-b - math.sqrt(discriminante)) / (2*a)
        return raiz1, raiz2

def imprimir_lista(lista):
    for elemento in lista:
        print(elemento)

def invertir_lista(lista):
    lista_invertida = []
    for i in range(len(lista) - 1, -1, -1):
        lista_invertida.append(lista[i])
    return lista_invertida

def convertir_mayusculas(lista):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(elemento.upper())
    return nueva_lista

def agregar_elemento(lista, elemento):
    lista.append(elemento)
    return lista

def eliminar_elemento(lista, elemento):
    if elemento in lista:
        lista.remove(elemento)
    return lista

def suma_numeros(n):
    suma = 0
    for i in range(n + 1):
        suma += i
    return suma

def suma_impares(n):
    suma = 0
    for i in range(n + 1):
        if i % 2 != 0:
            suma += i
    return suma

def suma_pares(n):
    suma = 0
    for i in range(n + 1):
        if i % 2 == 0:
            suma += i
    return suma

def contar_pares_impares(n):
    pares = 0
    impares = 0
    for i in range(n + 1):
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
    return f"Cantidad de pares: {pares}, cantidad de impares: {impares}"

def calcular_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def elementos_unicos(lista):
    conjunto = set()
    for elemento in lista:
        if elemento in conjunto:
            return False
        conjunto.add(elemento)
    return True

def idiomas_mas_hablados(n=5):
    idiomas = {'Inglés': 1500, 'Español': 500, 'Francés': 280, 'Chino': 1200, 'Arabe': 600}
    lista_ordenada = sorted(idiomas.items(), key=lambda x: x[1], reverse=True)
    return lista_ordenada[:n]

def paises_mas_poblados(n=5):
    poblacion = {'China': 1400, 'India': 1380, 'EEUU': 330, 'Indonesia': 270, 'Brasil': 212}
    lista_ordenada = sorted(poblacion.items(), key=lambda x: x[1], reverse=True)
    return lista_ordenada[:n]