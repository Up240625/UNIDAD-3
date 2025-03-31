
print("Iterar de 0 a 10:")
for i in range(11):
    print(i)

i = 0
while i <= 10:
    print(i)
    i += 1


print("\nIterar de 10 a 0:")
for i in range(10, -1, -1):
    print(i)

i = 10
while i >= 0:
    print(i)
    i -= 1


print("\nTriángulo:")
for i in range(1, 8):
    print("#" * i)


print("\nCuadrícula:")
for i in range(8):
    for j in range(8):
        print("#", end=" ")
    print()


print("\nPatrón multiplicado:")
for i in range(11):
    print(f"{i} x {i} = {i * i}")


print("\nLista de elementos:")
languages = ['Python', 'Numpy', 'Pandas', 'Django', 'Flask']
for language in languages:
    print(language)


print("\nNúmeros pares de 0 a 100:")
for i in range(0, 101, 2):
    print(i)


print("\nNúmeros impares de 0 a 100:")
for i in range(1, 101, 2):
    print(i)


print("\nSuma de todos los números de 0 a 100:")
total_sum = sum(range(101))
print(f"La suma de todos los números es: {total_sum}")


even_sum = sum(i for i in range(101) if i % 2 == 0)
odd_sum = sum(i for i in range(101) if i % 2 != 0)
print(f"La suma de todos los pares es: {even_sum}")
print(f"La suma de todos los impares es: {odd_sum}")


print("\nPaíses con 'land':")
countries = ["Finland", "Switzerland", "Iceland", "Thailand"]
for country in countries:
    if "land" in country:
        print(country)


print("\nFrutas en orden inverso:")
fruits = ['banana', 'cherry', 'mango', 'strawberries']
for fruit in reversed(fruits):
    print(fruit)