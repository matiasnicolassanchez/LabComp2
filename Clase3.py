
def media():
    cant_num = int(input("Ingrese la cantidad de números a guardar: "))
    nums = [] * cant_num
    sumatoria = 0
    porcentaje_medio = float
    for i in range(cant_num):
        num = int(input("Ingrese su número a guardar: "))
        sumatoria = sumatoria + num
        nums.append(num)
    porcentaje_medio = sumatoria /2
    return porcentaje_medio

def mean(sample):
    return sum(sample)/len(sample)


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
        list.append(i**2)
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
    return  words

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
        vector_doble.append(i*2)

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
    media = sum(vector)/len(vector)
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



