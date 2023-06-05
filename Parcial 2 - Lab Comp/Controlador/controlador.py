from Modelado.libros import Libros
from Vista.vista import Vista


class Controller:
    def __init__(self):
        self.vista = Vista()
        self.libros = Libros()

    # Controla las entradas del usuario por el menu
    def menu_principal(self):
        while True:
            entrada_menu = self.vista.menu_principal()
            if entrada_menu == 1:
                Controller.consultar_disponibilidad(self)
                pass
            if entrada_menu == 2:
                Controller.registrar_prestamo(self)
            if entrada_menu == 3:
                Controller.registrar_devolucion(self)

    # Lleva a cabo la primera opción del menu que es mostrar la disponibilidad de los libros
    def consultar_disponibilidad(self):
        Libros.get_registros(self)
        disponibles = Libros.get_disponibilidad(self)
        Vista.mostrar_disponibilidad(self, disponibles)

    # Lleva a cabo la segunda opción del menu que es registrar el prestamo de un libro
    def registrar_prestamo(self):
        self.libros.get_registros()
        lista = self.libros.get_listado_libros()
        libro_prestado = self.vista.mostrar_listado_libros(lista)
        self.libros.set_prestado(libro_prestado)
        self.libros.actualiazar_registros()
        self.vista.mostrar_disponibilidad(self.libros.get_disponibilidad())

    # Lleva a cabo la tercera opción del menu que es registrar la devolución de un libro
    def registrar_devolucion(self):
        self.libros.get_registros()
        lista = self.libros.get_listado_libros()
        libro_devuelto = self.vista.mostrar_listado_libros(lista)
        self.libros.set_devolucion(libro_devuelto)
        self.libros.actualiazar_registros()
        self.vista.mostrar_disponibilidad(self.libros.get_disponibilidad())

