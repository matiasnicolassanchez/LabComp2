
class Materias:
    # Metodo que trae el listado completo de materias desde el archivo
    def get_materias(self):
        materias = []
        with open("../Recursos/materias.txt", "r+") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                materias.append(line)
        return materias

    # Metodo que obtiene las materias correlativas de cada materia
    def get_correlatividades(self, materia):
        materias = []
        with open("../Recursos/materias.txt", "r") as file:
            for line in file:
                line = line.rstrip().split()
                if line[0] == str(materia):
                    if line[2] == "0":
                        print(f"La materia {line[1]} no posee correlatividades. Usted puede inscribirse".upper())
                        break
                    else:
                        for i in range(2, len(line)):
                            materias.append(line[i])
        return materias
