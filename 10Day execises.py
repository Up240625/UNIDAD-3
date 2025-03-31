# Iterar de 0 a 10 usando un bucle for y luego un bucle while
print("Iterar de 0 a 10:")
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1

# Iterar de 10 a 0 usando un bucle for y luego un bucle while
print("\nIterar de 10 a 0:")
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1

# Generar el triángulo usando un bucle
print("\nTriángulo:")
for i in range(1, 8):
    print("#" * i)

# Usar bucles anidados para generar la cuadrícula
print("\nCuadrícula:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()

# Imprimir el patrón multiplicando números
print("\nPatrón multiplicado:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")

# Iterar la lista y imprimir los elementos
print("\nLista de elementos:")
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)

# Iterar de 0 a 100 y imprimir números pares
print("\nNúmeros pares de 0 a 100:")
for i in range(0, 101, 2):
    print(i)

# Iterar de 0 a 100 y imprimir números impares
print("\nNúmeros impares de 0 a 100:")
for i in range(1, 101, 2):
    print(i)

# Nivel 2: sumar números de 0 a 100
print("\nSuma de todos los números de 0 a 100:")
total_sum = sum(range(101))
print(f"La suma de todos los números es: {total_sum}")

# Sumar pares e impares
even_sum = sum(i for i in range(101) if i % 2 == 0)
odd_sum = sum(i for i in range(101) if i % 2 != 0)
print(f"La suma de todos los pares es: {even_sum}")
print(f"La suma de todos los impares es: {odd_sum}")

# Nivel 3: países con "land"
print("\nPaíses con 'land':")
countries = ["Finland", "Switzerland", "Iceland", "Thailand"]
for country in countries:
    if "land" in country:
        print(country)

# Lista de frutas en orden inverso
print("\nFrutas en orden inverso:")
fruits = ['banana', 'cherry', 'mango', 'strawberries']
for fruit in reversed(fruits):
    print(fruit)