def media():
    cant_num = int(input("Ingrese la cantidad de números a guardar: "))
    nums = [] * cant_num
    sumatoria = 0
    porcentaje_medio = float
    for i in range(cant_num):
        num = int(input("Ingrese su número a guardar: "))
        sumatoria = sumatoria + num
        nums.append(num)
    porcentaje_medio = sumatoria / 2
    return porcentaje_medio


def mean(sample):
    return sum(sample) / len(sample)


# print(media())


def cuadrados():
    cant_num = int(input("Ingrese la cantidad de números que va a cargar: "))
    numeros = [] * cant_num
    num_cuadrados = []
    for i in range(cant_num):
        num = int(input("Ingrese su número: "))
        numeros.append(num)
    for i in range(cant_num):
        cuadrado = numeros[i] ** 2
        num_cuadrados.append(cuadrado)
    print(num_cuadrados)


def square(sample):
    list = []
    for i in sample:
        list.append(i ** 2)
    return list


# cuadrados()

# Funcion que cuenta la cantidad de veces que se repite cada palabra de un texto
def count_words(text):
    text = text.split()
    words = {}
    for i in text:
        if i in words:
            words[i] += 1
        else:
            words[i] = 1
    return words


# Funcion que encuentra la palabra que se repite mayormente en un texto
def most_repeated(words):
    max_word = ""
    max_freq = 0
    for word, freq in words.items():
        if freq > max_freq:
            max_word = word
            max_freq = freq
    return max_word, max_freq


text = "Como quieres que te quiera si el que quiero que me quiera no me quiere como quiero".upper()

# print(count_words(text))
# print(most_repeated(count_words(text)))

# diccionario = {}
# diccionario["jose"] = 34
# diccionario["gabriel"] = 21
# diccionario["maria"] = 35

vector = []
vector_doble = []


def ingresar_vector():
    for i in range(5):
        vector.append(int(input("Ingrese un número: ")))


def duplicar_vector(vector):
    for i in vector:
        vector_doble.append(i * 2)


def imprimir_valor(vector1, vector2):
    print(vector1)
    print(vector2)


# ingresar_vector()
# duplicar_vector(vector)
# imprimir_valor(vector, vector_doble)


alturas = []
altura_media = float


def ingresar_alturas():
    cant_alum = int(input("Ingrese la cantidad de alumnos: "))
    for i in range(cant_alum):
        alturas.append(float(input("Ingrese la altura en metros de su alumno: ")))


def media_alturas(vector):
    media = sum(vector) / len(vector)
    return media


def mayor_media(vector):
    cont = 0
    for i in vector:
        if i > media_alturas(vector):
            cont += 1
    return cont


def menor_media(vector):
    cont = 0
    for i in vector:
        if i < media_alturas(vector):
            cont += 1
    return cont


# ingresar_alturas()
# print(f"La altura media de sus alumnos es de: {media_alturas(alturas).__round__(2)}m")
# print(f"En su curso hay {mayor_media(alturas)} alumnos con altura mayor a la media")
# print(f"En su curso hay {menor_media(alturas)} alumnos con altura menor a la media")



def cargar_elementos(n):
    almacenamiento = [None] * n
    cont = 0
    while cont < n:
        posicion = int(input("Ingrese la posicion entre en la que desea almacenar su elemento: "))
        if almacenamiento[posicion] is None:
            valor = int(input(f"Ingrese el valor que desea guardar en la posicion {posicion}: "))
            almacenamiento[posicion] = valor
            print(f"!!!El valor {valor} ah sido guardado CORRECTAMENTE en la posición {posicion}¡¡¡")
            cont += 1
        else:
            print(f"!!!La posicion {posicion} YA SE ENCUENTRA CARGADA CON UN VALOR¡¡¡")
    if cont == n:
        print(f"Su almacenamiento de {cant_elementos} elementos se ha LLENADO COMPLETAMENTE")

# cant_elementos = int(input("Ingrese la cantidad de elementos que va a almacenar: "))
# cargar_elementos(cant_elementos)



def sum_matrices3x3():
    matriz_1 = [[int() for ind0 in range(3)] for ind1 in range(3)]
    matriz_2 = [[int() for ind0 in range(3)] for ind1 in range(3)]
    matriz_3 = [[int() for ind0 in range(3)] for ind1 in range(3)]
    cont = 0
    print("¡¡ COMENCEMOS A CARGAR LA PRIMER MATRIZ DE 3x3 QUE DESEA SUMAR !!")
    for i in range(3):
        for j in range(3):
            matriz_1[i][j] = int(input(f"Ingrese el elemento que desea cargar en la ubicación {i + 1}{j + 1}: "))
    print("¡¡ LA PRIMER MATRIZ HA SIDO CARGADA CORRECTAMENTE !!\n ¡¡ COMENCEMOS A CARGAR LA SEGUNDA MATRIZ DE 3x3 QUE "
          "DESEA SUMAR !!")
    for i in range(3):
        for j in range(3):
            matriz_2[i][j] = int(input(f" Ingrese el elemento que desea cargar en la ubicacion {i + 1}{j + 1}: "))
    print("¡¡ LA SEGUNDA MATRIZ HA SIDO CARGADA CORRECTAMENTE !! \n La MATRIZ 1:")
    for i in range(3):
        for j in range(3):
            matriz_1[i][j]
            print(" ", matriz_1[i][j], end="")
        print(" ")
    print(" SE SUMA CON LA MATRIZ 2:")
    for i in range(3):
        for j in range(3):
            matriz_2[i][j]
            print(" ", matriz_2[i][j], end="")
        print(" ")
    print("Y LA MATRIZ RESULTANTE DE ESTA SUMA ES:")
    for i in range(3):
        for j in range(3):
            matriz_3[i][j] = (matriz_1[i][j]) + (matriz_2[i][j])
            print(" ", matriz_3[i][j], end="")
        print(" ")

# sum_matrices3x3()

def quiniela():
    num_montos = [[int() for ind0 in range(2)] for ind1 in range(31)]
    print("¡¡ Carguemos los números ganadores y sus montos pagados !!")
    for i in range(31):
        for j in range(2):
            num_montos[i][j] =
