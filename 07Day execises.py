it_companies = {"Nissan", "Tesla", "Google"}

longitud = len(it_companies)
print("Longitud del conjunto it_companies:", longitud)

it_companies.add("Twitter")
print("it_companies después de añadir Pinterest:", it_companies)

it_companies.update({"Apple", "Sonny", "Uber"})
print("it_companies después de añadir varias empresas:", it_companies)

it_companies.remove("Google")
print("it_companies después de eliminar Discord:", it_companies)

it_companies.discard("Sonny")
print("it_companies después de desechar Pinterest:", it_companies)

A = {10, 20, 30, 40}
B = {30, 40, 50, 70}

union = A | B
print("Unión de A y B:", union)

interseccion = A & B
print("Intersección de A y B:", interseccion)

diferencia = A - B
print("Diferencia A - B:", diferencia)

diferencia_simetrica = A ^ B
print("Diferencia simétrica entre A y B:", diferencia_simetrica)

es_subconjunto = A <= B
print("¿Es A un subconjunto de B?", es_subconjunto)