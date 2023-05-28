from alumno import Alumno
from materias import Materias
from verificaciones import Verificaciones


class Vistas:

    # Metodo para emitir msj de bienvenida al iniciar el sistema
    def set_msj_bienvenida(self):
        print("¡¡ BIENENIDO AL SISTEMA DE INSCRIPCIÓN DE CURSADO DE LA TECNICATURA EN PROGRAMACIÓN !!")

    # Metodo que emite el menu principal del sistema
    def menu_principal(self):
        try:
            op_menu1 = int(input(
                "MENU:\n1.-Registrarme\n2.-Consultar si puedo inscribirme a cursar\n3.-Consultar mi estado\n4.-Cargar "
                "nueva materia aprobada\n5.-Salir\nINGRESE EL NÚMERO DE LA ACTIVIDAD QUE DESEA REALIZAR: "))
            op_menu1 = Verificaciones.ver_entrada_menu(self, op_menu1, 5)
            retorno = op_menu1
        except ValueError:
            op_menu1 = int(input(
                "MENU:\n1.-Registrarme\n2.-Consultar si puedo inscribirme a cursar\n3.-Consultar mi estado\n4.-Cargar "
                "nueva materia aprobada\n5.-Salir\nINGRESE EL NÚMERO DE LA ACTIVIDAD QUE DESEA REALIZAR: "))
            retorno = Verificaciones.ver_entrada_menu(self, entrada=op_menu1, limite_opciones=5)
        return retorno

    # Metodo que emite el menu dentro de la sección de registrarse
    def segundo_menu(self):
        try:
            op_menu2 = int(input(
                "A CONTINUACIÓN DESEA:\n1.-Cargar materias aprobadas\n2.-Ir al menu principal\n3.-Salir\nINGRESE EL NÚMERO DE OPCIÓN ELEJIDA: "))
            op_menu2 = Verificaciones.ver_entrada_menu(self, op_menu2, 3)
        except ValueError:
            op_menu2 = int(input(
                "A CONTINUACIÓN DESEA:\n1.-Cargar materias aprobadas\n2.-Ir al menu principal\n3.-Salir\nINGRESE EL NÚMERO DE OPCIÓN ELEJIDA: "))
            op_menu2 = Verificaciones.ver_entrada_menu(self, entrada=op_menu2, limite_opciones=3)
        return op_menu2

    # Metodo que emite el menu dentro de la sección donde se cargan las materias aprobadas
    def tercer_menu(self):
        try:
            op_menu3 = int(input(
                "DESEA SEGUIR CARGANDO MATERIAS APROBADAS?\n1.-Seguir cargando\n2.-Ir al menu principal\n3.-Salir\nINGRESE EL NÚMERO DE LA OPCIÓN ELEJIDA: "))
            op_menu3 = Verificaciones.ver_entrada_menu(self, op_menu3, 3)
        except ValueError:
            op_menu3 = Verificaciones.ver_entrada_menu(self, op_menu3, 3)
        return op_menu3

    # Metodo que emite el menu dentro de la sección de consulta sobre materias
    def cuarto_menu(self):
        try:
            op_menu4 = int(input(
                "COMO DESEA CONTINUAR?\n1.-Seguir consultando materias\n2.-Menu principal\n3.-Salir\nINGRESE EL VALOR CORRESPONDIENTE A LA OPCIÓN ELEGIDA: "))
            op_menu4 = Verificaciones.ver_entrada_menu(self, op_menu4, 3)
        except ValueError:
            op_menu4 = Verificaciones.ver_entrada_menu(self, op_menu4, 3)
        return op_menu4

    # Metodo que emite el menu dentro de la seccion donde se cargan materias aprobadas
    def quinto_menu(self):
        try:
            op_menu5 = int(input(
                "COMO DESEA CONTINUAR?\n1.-Seguir cargando materias aprobadas\n2.-Menu principal\n3.-Salir\nINGRESE EL VALOR CORRESPONDIENTE A LA OPCIÓN ELEGIDA: "))
            op_menu5 = Verificaciones.ver_entrada_menu(self, op_menu5, 3)
        except ValueError:
            op_menu5 = Verificaciones.ver_entrada_menu(self, op_menu5, 3)
        return op_menu5

    # Metodo que muestra las materias por indice y nombre
    def mostrar_materias_aprobadas(self, materias):
        materias_total = Materias.get_materias(self)
        for materia in materias_total:
            print("LAS MATERIAS QUE USTED AH APROBADO SON:")
            if materia[0] in materias:
                print(f"{materia[0]}.-{materia[1]}".upper())

    # Metodo que muestra las materias de la carrera excepto las que ya estan cargadas como aprobadas
    def mostrar_materias(self, materias, materias_cargadas):
        materias = materias
        materias_cargadas = materias_cargadas
        for line in materias:
            if line[0] in materias_cargadas:
                pass
            else:
                print(f"{line[0]}.-{line[1]}")

    # Metodo que solicita al usuario que ingrese su legajo
    def set_legajo(self):
        self.legajo = input("INGRESE SU LEGAJO: ")
        return self.legajo

    # Metodo que solicita al usuario que ingrese su nombre
    def set_nombre(self):
        self.nombre_apellido = input("INGRESE SU NOMBRE: ")
        return self.nombre_apellido


    # Metodo que solicita al usuario que ingrese la materia que desea cargar como aprobada
    def set_materia_aprobada(self):
        try:
            materia = int(input("INGRESE LA MATERIA QUE HA REGULARIZADO: "))
            materia = Verificaciones.ver_entrada_menu(self, materia, 20)
        except ValueError:
            materia = Verificaciones.ver_entrada_menu(self, materia, 20)
        return materia

    # Metodo que solicita al usuario
    def get_materias_inscribir(self):
        try:
            materia_inscribir = int(input("INGRESE EL NÚMERO CORRESPONDIENTE A LA MATERIA QUE DESEA INSCRIBIRSE: "))
            materia_inscribir = Verificaciones.ver_entrada_menu(self, materia_inscribir, 20)
        except ValueError:
            materia_inscribir = Verificaciones.ver_entrada_menu(self, materia_inscribir, 20)
        return materia_inscribir

    # Metodo que emite
    def msj_inscribirse(self, bandera):
        if bandera is True:
            print("¡¡ Usted puede inscribirse a la materia elegida !!".upper())
        else:
            print("¡¡ Usted no puede inscribirse a la materia que desea !!".upper())

    # Metodo que muestra los datos cargados del usuario
    def get_estado_usuario(self, estudiante):
        print(Alumno.__str__(estudiante))

    # Metodo que emite msj cuando el legajo no esta registrado aun
    def set_msj_err_ver_legajo(self):
        print("¡¡ El legajo que usted ha ingresado no se encuentra registrado !!".upper())

    # Metodo que emite msj cuando la materia que se desea cargar como aprobada no responde la correlatividad
    def set_msj_err_carga_materias(self):
        print(
            "¡¡ La materia que usted desea cargar no cumple con las condiciones de correlatividades con las materias registradas !!".upper())
