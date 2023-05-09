ruta_registro = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\Resultado Elecciones.txt"
linea = []
matriz = []
cant_total_votos = 0
votos_cand = []
porcentaje: [float] = 0
porcentaje_cand = []
c = float
mayor_porc1 = 0
mayor_porc2 = 0

with open(ruta_registro, "r") as file:
    for line in file:
        linea = line.split(",")
        matriz.append(linea)
        print(linea)

for i in range(7):
    for j in matriz[i]:
        print(" ", j.strip(), end="")
    print(" ")

# Se recorre la matriz para contabilizar la totalidad de los votos contabilizados y tambien se obtienen los votos por candidato
for j in range(1, 5):
    for i in range(2, 7):
        cant_total_votos += int(matriz[i][j])
        if i == 6:
            if j == 1:
                votos_cand.append(cant_total_votos)
                continue
            if j == 2:
                votos_cand.append(cant_total_votos - votos_cand[0])
                continue
            if j == 3:
                votos_cand.append(cant_total_votos - votos_cand[0] - votos_cand[1])
                continue
            if j == 4:
                votos_cand.append(cant_total_votos - votos_cand[0] - votos_cand[1] - votos_cand[2])

print(f"En estas elecciones se contabilizaron un total de {cant_total_votos} votos")
for i in votos_cand:
    porcentaje = ((i/cant_total_votos)*100).__round__(2)
    porcentaje_cand.append(porcentaje)
    print(f"El candidato {(matriz[1][votos_cand.index(i)+1]).strip()} registro un total de {i} votos \nQue "
          f"representan el {porcentaje}%")

for i in


# print(votos_cand_a, votos_cand_b, votos_cand_c, votos_cand_d)

