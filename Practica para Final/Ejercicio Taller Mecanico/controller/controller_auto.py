from model.auto import Auto
from view.view_auto import View

class Controller:
    def __init__(self):
        self.model = Auto()
        self.view = View()

    def controller_gral(self):
        self.verificar_archivo(self)
        while True:
            self.model.obtener_registros()
            eleccion = self.view.menu_principal
            if eleccion == 1:
                old_km, date_service, patente, bandera = self.model.consultar_patente(self.view.get_patente())
                self.view.mostrar_datos(old_km, date_service, patente, bandera)
                pass
            elif eleccion == 2:
                pass
            elif eleccion == 3:
                patente, km, date = self.view.pedir_datos()
                self.model.
            elif eleccion == 4:
                break

    @staticmethod
    def verificar_archivo(self):
        try:
            with open("Resources/registros.txt", "r") as file:
                pass
        except FileNotFoundError:
            with open("Resources/registros.txt", "x") as file:
                pass

