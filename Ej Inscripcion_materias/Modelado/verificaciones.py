from self import self
from alumno import Alumno
from materias import Materias


class Verificaciones:
    # Metodo que verifica que el legajo este registrado en el archivo
    def ver_legajo_existente(self, legajo):
        with open("../Recursos/Reg_Alumnos.txt", "r+") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                if line[0] == str(legajo):
                    bandera = True
                else:
                    bandera = False
        return bandera

    # Metodo que verifica que el usuario cumpla las condiciones de correlatividades con la materia consultada para
    # inscripcion y para cargarla como aprobada
    def ver_materia_inscribir(self, materia):
        materias_total = Materias.get_materias(self)
        materias_usuario = Alumno.get_materias_registradas(self)
        correlativas = []
        correlativas_usuario = []
        for line in materias_total:
            if line[0] != str(materia):
                pass
            if line[0] == str(materia) and line[2] == "0":
                bandera = True
                break
            if line[0] == str(materia) and line[2] != "0":
                for i in range(2, len(line)):
                    correlativas.append(line[i])
                break
        for i in correlativas:
            if i in materias_usuario:
                correlativas_usuario.append(i)
            else:
                pass
        if len(correlativas_usuario) == len(correlativas):
            bandera = True
        else:
            bandera = False
        return bandera

    # Metodo que evalua la opcion elegida por el usuario de los menus y manipula o no las variables de control
    def evaluacion_opcion_elegida(self, opcion):
        if opcion == 1:
            consultando = 1
            salida = 1
            pass
        if opcion == 2:
            consultando = 0
            salida = 1
            pass
        if opcion == 3:
            consultando = 0
            salida = 0
        return consultando, salida

    def ver_entrada_menu(self, entrada, limite_opciones):
        entrada_verificada = entrada
        while 1 > entrada > limite_opciones and isinstance(entrada, str):
            entrada_verificada = int(input("¡¡ La opción ingresada no corresponde a un elemento del menu !!\nINGRESE NUEVAMENTE UN NÚMERO DE LAS OPCIONES DEL MENU: ".upper()))
        return entrada_verificada

    def ver_solo_numeros(self, entrada):
        entrada_verificada = entrada
        while not isinstance(entrada, int):
            entrada_verificada = int(input("¡¡ Solo se permiten ingresar números !!\nPor favor vuelva a cargar su dato: ".upper()))
        return entrada_verificada



