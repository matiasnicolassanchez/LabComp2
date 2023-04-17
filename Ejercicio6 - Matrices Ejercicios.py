def horas_vuelo(matriz):  # Esta función obtiene el total de horas de vuelo por cada tipo de avión
    # Recorro toda la matriz para obtener el tipo de avion y las horas de vuelo para almacenarlo en un diccionario e ir sumando las horas de vuelo de cada tipo de avion
    for y in range(cant_vuelos):
        # En el if compruebo si esta ya registrado el tipo de avion en el diccionario(reg_horas_vuelo) y si es afirmativo, sumo las horas de ese vuelo a las ya cargadas
        if matriz[y][1] in reg_horas_vuelo:
            reg_horas_vuelo[matriz[y][1]] += reg_vuelos[y][2]
        # Si el tipo de avion no esta registrado en el diccionario, lo registro y almaceno las horas de vuelo para empezar a contabilizar
        else:
            reg_horas_vuelo[matriz[y][1]] = matriz[y][2]

    # print(reg_horas_vuelo)
    # En este for trabajo al diccionario como clave:valor, donde el primer valor(clave) es el tipo de avion y el segundo valor(valor) son las horas de vuelo contabilizadas
    for tipo, horas in reg_horas_vuelo.items():
        print(f"El avion de tipo {tipo}, registro un total de horas de vuelo de {horas} horas")


# Esta funcion calcula la altura media por cada tipo de avion
def altura_media(matriz):
    media = float
    for z in range(cant_vuelos):
        if matriz[z][1] in alturas_tipo:
            alturas_tipo[matriz[z][1]] += matriz[z][4]
        else:
            alturas_tipo[matriz[z][1]] = matriz[z][4]
    for tipo, hmax in alturas_tipo.items():
        cant_vuelos_tipo.items()
        vuelos = 0
        for c in range(cant_vuelos):
            if matriz[c][1] == tipo:
                vuelos += 1
        media = (hmax / vuelos).__round__(2)
        print(f"El avion tipo {tipo} registra un altura media de vuelo de {media} metros")


def max_pasajeros_altura(matriz):
    mayor_cant_pasaje, altura = 0, float
    for f in range(cant_vuelos):
        if matriz[f][3] > mayor_cant_pasaje:
            mayor_cant_pasaje = matriz[f][3]
            altura = matriz[f][4]
    print(f"La mayor cantidad de pasajeros que se transportaron fue: {mayor_cant_pasaje} pasajeros "
          f"y se registro una altura maxima de vuelo de: {altura} metros")


def cantpasaje_tipo(matriz):
    for g in range(cant_vuelos):
        if matriz[g][1] in pasaje_tipo:
            pasaje_tipo[matriz[g][1]] += matriz[g][3]
        else:
            pasaje_tipo[matriz[g][1]] = matriz[g][3]
    for tipo, pasaje in pasaje_tipo.items():
        print(f"El tipo de avion {tipo}, registro una cantidad total de pasajeros transportados de {pasaje} pasajeros")


def prom_vuelos(matriz):
    for h in range(cant_vuelos):
        if matriz[h][1] in cant_vuelos_tipo:
            cant_vuelos_tipo[matriz[h][1]] += 1
        else:
            cant_vuelos_tipo[matriz[h][1]] = 1
    for tipo, vuelos in cant_vuelos_tipo.items():
        print(f"El avion tipo {tipo} registra un promedio de vuelos de {(vuelos/cant_vuelos).__round__(2)} vuelos")


# Declaración de variables
cant_vuelos = int(input("Ingrese la cantidad de vuelos que desea registrar: "))
reg_vuelos = [[int() for ind0 in range(5)] for ind1 in range(cant_vuelos)]
reg_horas_vuelo = {}
cant_vuelos_tipo = {}
alturas_tipo = {}
pasaje_tipo = {}
promedio_vuelos_tipo = {}


#  Con este for recorro las filas de la matriz que van a ser cada vuelo que se registre
for i in range(cant_vuelos):
    # Se numeran los vuelos de uno en uno, cada vez que se va a cargar los registros de un vuelo nuevo se le asigna un número de vuelo
    reg_vuelos[i][0] = (i + 1)
    # Con este for recorro las columnas de la matriz que corresponden a cada dato que necesito cargar
    for j in range(1, 5):
        # depende el valor de j entra en un if para pedir lo que corresponde a cada columna de la matriz
        if j == 1:
            reg_vuelos[i][j] = input(f"Ingrese el codigo de avion que realizo el vuelo número {i + 1}: ")
        if j == 2:
            reg_vuelos[i][j] = float(input(f"Ingrese la duración, en horas, del vuelo {i + 1}: "))
        if j == 3:
            reg_vuelos[i][j] = int(
                input(f"Ingrese la cantidad de pasajeros que se transportaron en el vuelo número {i + 1}: "))
        if j == 4:
            reg_vuelos[i][j] = float(
                input(f"Ingrese el valor(en metros) maximo alcanzado en altura durante el vuelo {i + 1}: "))
# Aqui se imprimi la matriz por consola
for i in range(cant_vuelos):
    for j in range(5):
        reg_vuelos[i][j]
        print(" ", reg_vuelos[i][j], end="")
    print(" ")

# Consigna N°1
horas_vuelo(reg_vuelos)

# Consigna N°2
altura_media(reg_vuelos)

# Consigna N°3
max_pasajeros_altura(reg_vuelos)

# consigna N°4
cantpasaje_tipo(reg_vuelos)

# Consigna N°5
prom_vuelos(reg_vuelos)