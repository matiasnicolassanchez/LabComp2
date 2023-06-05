class Vista:

    # Muestra el menu principal y toma el ingreso del usuario
    def menu_principal(self):
        opcion_menu = 0
        try:
            opcion_menu = int(input("1.-Consultar disponibilidad de libros\n2.-Registrar un prestamo\n3.-Registrar "
                                    "Devolución\nPOR FAVOR INGRESE LA OPCIÓN QUE DESEE: "))
            while 1 > opcion_menu > 3:
                print("¡¡ EL VALOR INGRESADO NO CORRESPONDE A UN VALOR DEL MENU !!")
                opcion_menu = int(input("1.-Consultar disponibilidad de libros\n2.-Registrar un "
                                        "prestamo\n3.-Registrar Devolución\nPOR FAVOR INGRESE LA OPCIÓN QUE DESEE: "))
        except ValueError:
            print("¡¡ EL VALOR INGRESADO NO CORRESPONDE A UN VALOR DEL MENU !!")
            while 1 > opcion_menu > 3 or not isinstance(opcion_menu, int):
                print("¡¡ EL VALOR INGRESADO NO CORRESPONDE A UN VALOR DEL MENU !!")
                opcion_menu = int(input("1.-Consultar disponibilidad de libros\n2.-Registrar un "
                                        "prestamo\n3.-Registrar Devolución\nPOR FAVOR INGRESE LA OPCIÓN QUE DESEE: "))
        return opcion_menu

    # Muestra al usuario el listado de libros con su disponibilidad
    def mostrar_disponibilidad(self, registros):
        print("LOS LIBROS DISPONIBLES SON:")
        for libro in registros:
            print(f"NOMBRE: {libro[0]}, DISPONIBLES: {libro[1]} libros".upper())

    # Muestra al usuario el listado de libros con su id y pide al usuario que ingrese el id del libro
    def mostrar_listado_libros(self, libros):
        for libro in libros:
            print(f"{libro[0]}.-{libro[1]}".upper())
        ingreso = 0
        try:
            ingreso = int(input("INGRESE EL LIBRO QUE DESEA REGISTRAR: "))
            while 1 > libro > len(libros):
                print("¡¡ LA OPCIÓN INGRESADA NO ES UN VALOR DE LA LISTA DE LIBROS !!")
                ingreso = int(input("INGRESE EL LIBRO QUE DESEA REGISTRAR: "))
        except ValueError:
            print("¡¡ LO INGRESADO NO ES CORRECTO, INGRESE UN VALOR CORRESPONDIENTE A UN LIBRO !!")
            while 1 > ingreso > len(libros) or isinstance(ingreso, str):
                print("¡¡ LO INGRESADO NO ES CORRECTO, INGRESE UN VALOR CORRESPONDIENTE A UN LIBRO !!")
                ingreso = int(input("INGRESE EL LIBRO QUE DESEA REGISTRAR: "))
        return ingreso
