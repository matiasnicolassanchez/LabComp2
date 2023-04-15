import csv
from typing import TextIO

# arch = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\Videojuegos.txt"

# with open(arch, "r") as archivo:
#     next(archivo, None)
#     for linea in archivo:
#         linea = linea.rstrip()
#         separador = ","
#         lista = linea.split(separador)
#         nombre = lista[0]
#         calificacion = int(lista[1])
#         precio = float(lista[2])
#         print(f"Juego: {nombre} con calificación {calificacion} y precio {precio}")


# with open(arch, "r") as archivo:
#     lector = csv.reader(archivo, delimiter=",")
#     next(lector, None)
#     for fila in lector:
#         nombre = fila[0]
#         calificacion = int(fila[1])
#         precio = float(fila[2])
#         print(f"Juego: {nombre} con calificación {calificacion} y precio {precio}")
#         print(f"{fila}")
#
arch = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\Facturacion.txt"
archivo_ordenado = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\Facturacion Ordenada.txt"
with open(arch, "r") as archivo , open(archivo_ordenado, "a") as file:
    lectura = archivo.readlines()
    lectura.sort()
    for i in lectura:
        file.write(i)
    next(archivo, None)
    for linea in archivo:
        linea = linea.rstrip()
        print(linea)
        separador = ";"
        lista = linea.split(separador)
        año = lista[0]
        fact_anual = 0
        media = 0
        for i in range(1, 5):
            fact_anual += int(lista[i])
        media = (fact_anual/12).__round__(2)
        print(f"En el año {año}, la facturación anual fue de: {fact_anual} y la media de: {media}")

    arch and file.close()


