try:
    print(resultado=10 / 0)
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


def suma_num_positivos(num1, num2):
    if num1 <= 0 or num2 <= 0:
        raise Exception("ValueError: SOLO SE DEBEN INGRESAR VALORES POSITIVOS")
    else:
        return num1 + num2


n1 = 8
n2 = 0

try:
    print(suma_num_positivos(n1, n2))
except Exception as err:
    print(err.__str__())
