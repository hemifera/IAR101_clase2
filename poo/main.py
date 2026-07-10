from estadisticas import Statistics

milista1 = [23, 3, 32, 32, 54, 36, 54645, 3]
milista2 = [2,76,83,353,5,6876,57,56,546]
milista3 = [87657,56,76,575,543,543,8756,87,8]
listas = []
for lista in [milista1, milista2, milista3]:
    listas.append(lista)

# listas.append(milista1, milista2, milista3)
for lista in listas:
    stat = Statistics(lista)
    print(f"Suma: {stat.suma()} y Longitud: {stat.longitud()}")
    print(f"Promedio: {stat.promedio():.2f}") # Redondeado a 2 decimales para que se vea limpio