try:
    print(resultado=10/0)
except ZeroDivisionError:
    print("NO ES POSIBLE REALIZAR LA DIVISION POR CERO")
try:
    print(resultado=15 + "20")
except TypeError:
    print("NO ES POSIBLE SUMAR UN ENTERO CON UN STRING")
try:
    lista = [1, 2, 3, 4, 5]
    lista[10]
except IndexError:
    print("INDICE DE LISTA FUERA DE RANGO")
try:
    colores = {"rojo": "red", "verde": "green", "negro": "black"}
    colores["blanco"]
except KeyError:
    print("EL VALOR QUE BUSCA NO SE ENCUENTRA")