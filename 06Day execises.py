
tupla_vacia = ()


hermanas = ('Stefy', 'Scarlet', 'Sofia')  
hermanos = ('marco', 'raul')  


hermanos_y_hermanas = hermanas + hermanos
print(hermanos_y_hermanas)  


cantidad_siblings = len(hermanos_y_hermanas)
print(f"Tengo {cantidad_siblings} hermanos y hermanas.")  


padre = 'Fernando'
madre = 'Veronica'
familia = hermanos_y_hermanas + (padre, madre)
print(familia) 

familia = ('Stefy', 'Scarlet', 'Sofia''Veronica','marco', 'raul','Fernando')
hermanos_y_hermanas, padre, madre = familia[:-2], familia[-2], familia[-1]
print(f"Hermanos y hermanas: {hermanos_y_hermanas}")  
print(f"Padre: {padre}, Madre: {madre}")  


frutas = ('Manzana', 'Banana', 'Cereza')
vegetales = ('Zanahoria', 'Brócoli', 'Espinaca')
productos_animales = ('Leche', 'Huevo', 'Queso')

food_stuff_tp = frutas + vegetales + productos_animales
print(food_stuff_tp)  


if len(food_stuff_tp) % 2 != 0:
    middle_item = [len(food_stuff_tp) // 2]
    print(f"Elemento del medio: {middle_item}") 
else:
    middle_items = food_stuff_tp[len(food_stuff_tp) // 2 - 1: len(food_stuff_tp) // 2 + 1]
    print(f"Elementos del medio: {middle_items}")  

primeros_tres_ultimos_tres = food_stuff_tp[:3] + food_stuff_tp[-3:]
print(f"Primeros tres y últimos tres elementos: {primeros_tres_ultimos_tres}")  
del food_stuff_tp
nordic_countries = ('Finland', 'Denmark', 'Norway', 'Iceland')
print('Estonia' in nordic_countries)  
print('Iceland' in nordic_countries)