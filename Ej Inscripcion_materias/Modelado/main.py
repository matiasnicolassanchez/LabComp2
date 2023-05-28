from self import self
from vistas import Vistas
from alumno import Alumno
from verificaciones import Verificaciones
from materias import Materias

Vistas.set_msj_bienvenida(self)
salida = 1
while salida == 1:
    # Se imprime el menu principal
    opcion_elegida1 = Vistas.menu_principal(self)
    # Se comienzaa evaluar la opcion del menu principal elegida por el usuario
    if opcion_elegida1 == 1:
        # Se registra el nuevo usuario
        usuario = Alumno(Vistas.set_legajo(self), Vistas.set_nombre(self))
        usuario.reg_alumno()
        # Se imprime el segundo menu
        opcion_elegida2 = Vistas.segundo_menu(self)
        # Se evalua la opcion elegida por el usuario para continuar
        cargando, salida = Verificaciones.evaluacion_opcion_elegida(self, opcion=opcion_elegida2)
        # Se cargan materias aprobadas hasta que el usuario decida terminar
        while cargando == 1:
            Vistas.mostrar_materias(self, Materias.get_materias(self), usuario.get_materias_cargadas())
            usuario.set_materias_aprobadas(Vistas.set_materia_aprobada(self))
            usuario.reg_materias_aprobadas()
            print(usuario.materias_aprobadas)
            # Se muestra el tercer menu para que el usuario decida continuar cargando materias aprobadas o no
            opcion_elegida3 = Vistas.tercer_menu(self)
            cargando, salida = Verificaciones.evaluacion_opcion_elegida(self, opcion=opcion_elegida3)
    if opcion_elegida1 == 2:
        # En esta opcion se consulta si es posible que el usuario se inscriba a ciertas materias o no
        legajo = Vistas.set_legajo(self)
        # Se verifica que el legajo este registrado para obtener las materias aprobadas que posee
        bandera = Verificaciones.ver_legajo_existente(self, legajo)
        if bandera is True:
            # Se crea el objeto alumno con los datos obtenido de los archivos a traves del legajo
            nombre = Alumno.get_nombre_alumno(self, legajo=legajo)
            usuario = Alumno(legajo=legajo, nombre_apellido=nombre)
            usuario.set_materias_aprobadas(usuario.get_materias_registradas())
            consultando = 1
            # El usuario consulta todas las materias que desee hasta que decida salir
            while consultando == 1:
                # Se muestra el listado de todas las materias de la carrera, excepto las que ya esta aprobadas
                Vistas.mostrar_materias(self, materias=Materias.get_materias(self),
                                        materias_cargadas=Alumno.get_materias_registradas(self))
                materia_inscribir = Vistas.get_materias_inscribir(self)
                # Se verifica que el usuario cumpla con las condiciones de correlatividad para poder inscribirse
                bandera = Verificaciones.ver_materia_inscribir(self, materia_inscribir)
                Vistas.msj_inscribirse(self, bandera=bandera)
                opcion_elegida4 = Vistas.cuarto_menu(self)
                consultando, salida = Verificaciones.evaluacion_opcion_elegida(self, opcion=opcion_elegida4)
        else:
            # Si el legajo no esta registrado se muestra un msj y se envia al usuario al menu principal
            Vistas.set_msj_err_ver_legajo(self)
    if opcion_elegida1 == 3:
        # En esta sección el usuario consulta su estado en el sistema a traves del legajo
        legajo = Vistas.set_legajo(self)
        # Se comprueba que el legajo este registrado
        bandera = Verificaciones.ver_legajo_existente(self, legajo)
        if bandera is True:
            # El legajo esta registrado asique se obtienen los datos y se crea el objeto alumno
            nombre = Alumno.get_nombre_alumno(self, legajo=legajo)
            usuario = Alumno(legajo=legajo, nombre_apellido=nombre)
            usuario.set_materias_aprobadas(usuario.get_materias_registradas())
            Vistas.get_estado_usuario(self, estudiante=usuario)
        else:
            # Si no esta registrado en el archivo se emite msj de error y se envia al menu principal
            Vistas.set_msj_err_ver_legajo(self)
    if opcion_elegida1 == 4:
        # En esta sección el usuario consulta su estado en el sistema a traves del legajo
        legajo = Vistas.set_legajo(self)
        # Se comprueba que el legajo este registrado
        bandera = Verificaciones.ver_legajo_existente(self, legajo)
        if bandera is True:
            # El legajo esta registrado asique se obtienen los datos y se crea el objeto alumno
            nombre = Alumno.get_nombre_alumno(self, legajo=legajo)
            usuario = Alumno(legajo=legajo, nombre_apellido=nombre)
            cargando_aprobadas = 1
            # Se cargan las materias aprobadas hasta que el usuario decida salir
            while cargando_aprobadas == 1:
                # Se imprimen todas las materias de la carrera menos las ya cargadas como aprobadas
                Vistas.mostrar_materias(self, materias=Materias.get_materias(self),
                                        materias_cargadas=Alumno.get_materias_registradas(self))
                materia_cargar = Vistas.set_materia_aprobada(self)
                # Se verifica que el usuario cumpla con las correlatividades para cargar una materia como aprobada
                bandera = Verificaciones.ver_materia_inscribir(self, materia=materia_cargar)
                Vistas.msj_inscribirse(self, bandera=bandera)
                if bandera is True:
                    usuario.act_materias_aprobadas(materia_cargar)
                opcion_elegida5 = Vistas.quinto_menu(self)
                cargando_aprobadas, salida = Verificaciones.evaluacion_opcion_elegida(self, opcion=opcion_elegida5)
        else:
            # Si no esta registrado en el archivo se emite msj de error y se envia al menu principal
            Vistas.set_msj_err_ver_legajo(self)
    if opcion_elegida1 == 5:
        salida = 0
