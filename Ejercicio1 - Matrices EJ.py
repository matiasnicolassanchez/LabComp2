import random

matriz_ventas = [[int() for j in range(15)] for i in range(10)]
ventas_vendedor = []
ventas_modelo = []
ventas_vend = int
ventas_mod = int
mayor_venta = 0


for i in range(10):
    for j in range(15):
        matriz_ventas[i][j] = random.randint(0, 50)

for i in range(10):
    for j in range(15):
        matriz_ventas[i][j]
        print(" ", matriz_ventas[i][j], end="")
    print(" ")

# Se recorre la matriz y se imprime cuantas vento registro cada vendedor por cada uno de los modelos
for i in range(10):
    for j in range(15):
        print(f"El vendedor {i+1} registra {matriz_ventas[i][j]} ventas de automoviles del modelo {j+1}")

# Se calculan la cantidad de automoviles que vendio cada vendedor y se almacenan en un vector
for i in range(10):
    ventas_vend = 0
    for j in range(15):
        ventas_vend += matriz_ventas[i][j]
        if j == 14:
            ventas_vendedor.append(ventas_vend)
for i in ventas_vendedor:
    print(f"El vendedor {(ventas_vendedor.index(i))+1} registra un total de ventas de {i} ventas")

# Se calcula la cantidad de automoviles vendidos por modelo y almacenan en un vector
for j in range(15):
    ventas_mod = 0
    for i in range(10):
        ventas_mod += matriz_ventas[i][j]
        if i == 9:
            ventas_modelo.append(ventas_mod)
for i in ventas_modelo:
    print(f"El modelo de auto {(ventas_modelo.index(i))+1} registro {i} ventas en el mes")

# Se comparan las ventas totales de cada vendedor y se obtiene el vendedor que mayor ventas registro en el mes
for i in ventas_vendedor:
    if int(i) > mayor_venta:
        mayor_venta = int(i)
print(f"El vendedor que registro mayor número de ventas es el vendedor {(ventas_vendedor.index(mayor_venta))+1}")
