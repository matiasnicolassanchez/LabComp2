from self import self


class Alumno:
    def __init__(self, legajo, nombre_apellido):
        self.legajo = legajo
        self.nombre_apellido = nombre_apellido
        self.materias_aprobadas = []

    def __str__(self):
        return f"Alumno: {self.nombre_apellido} de Legajo: {self.legajo} y materias aprobadas: {self.materias_aprobadas}"

    # Metodo encargado de registrar un usuario en el archivo
    def reg_alumno(self):
        with open("../Recursos/Reg_Alumnos.txt", "a+") as file:
            file.write(f"{self.legajo};{self.nombre_apellido}\n")
        print("¡¡ SE HA REGISTRADO CORRECTAMENTE !!")

    # Metodo que toma el indice de la materia a cargar como aprobada y la carga en el atributo
    def set_materias_aprobadas(self, materia):
        self.materias_aprobadas.append(materia)

    # Metodo que devuelve la lista de indices de materias aprobadas cargadas en el atributo
    def get_materias_cargadas(self):
        return self.materias_aprobadas

    # Metodo que obtiene las materias aprobadas que tiene registrado un usuario en el archivo
    def get_materias_registradas(self):
        materias_cargadas = []
        with open("../Recursos/Reg_Alumnos.txt", "r") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                if line[0] == self.legajo:
                    for i in range(2, len(line)):
                        materias_cargadas.append(line[i])
        return materias_cargadas

    # Metodo que registra materias aprobadas en el archivo del usuario
    def reg_materias_aprobadas(self):
        respaldo = []
        with open("../Recursos/Reg_Alumnos.txt", "r") as file:
            for line in file:
                alumno = line.rstrip(";").split(sep=";")
                if alumno[0] == self.legajo:
                    for i in self.materias_aprobadas:
                        alumno.append(str(i))
                    respaldo.append(alumno)
                    pass
                else:
                    respaldo.append(alumno)
        with open("../Recursos/Reg_Alumnos.txt", "w+") as file:
            for line in respaldo:
                escritura = ""
                for i in line:
                    if i is line[-1]:
                        i = i.rstrip()
                        escritura = escritura + i + "\n"
                        pass
                    else:
                        i = i.rstrip()
                        escritura = escritura + i + ";"
                file.write(escritura)

    # Metodo que obtiene el nombre del alumno registrado a traves del legajo
    def get_nombre_alumno(self, legajo):
        with open("../Recursos/Reg_Alumnos.txt", "r+") as file:
            nombre = ""
            for line in file:
                line = line.rstrip().split(sep=";")
                if line[0] == legajo:
                    nombre = line[1]
                    break
                else:
                    pass
        return nombre

    # Metodo que actualiza la lista de materias aprobadas registradas en el archivo
    def act_materias_aprobadas(self, materia):
        matriz = []
        with open("../Recursos/Reg_Alumnos.txt", "r") as file:
            for alumno in file:
                alumno = alumno.rstrip().split(sep=";")
                if alumno[0] == self.legajo:
                    alumno.append(materia)
                    matriz.append(alumno)
                    for i in range(2, len(alumno)):
                        self.materias_aprobadas.append(alumno[i])
                else:
                    matriz.append(alumno)
        with open("../Recursos/Reg_Alumnos.txt", "w") as file:
            for line in matriz:
                print(line)
                dato = ""
                for i in line:
                    if i is line[-1]:
                        dato = dato + str(i) + "\n"
                    else:
                        dato = dato + str(i) + ";"
                file.write(dato)
        print("¡¡ Su materia aprobada ha sido cargada correctamente !!".upper())
