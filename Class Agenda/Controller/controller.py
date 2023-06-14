from Modeler.agenda import Agenda
from View.views import Vistas


class Controlador:

    def __init__(self):
        self.agenda = Agenda()
        self.vista = Vistas()

    def inicializador(self):
        self.agenda.verificar_existencia_archivo()
        registros = []
        with open("Resources/agenda.txt", "r") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                registros.append(line)
        self.agenda.set_registros(registros)

    def registrar_nueva_reserva(self):
        fecha, titular = self.vista.nueva_reserva()
        self.agenda.set_nueva_reserva(fecha, titular)

    def obtener_registros_agenda(self):
        agenda = self.agenda.obtener_fechas()
        return agenda

    def consultar_fecha(self):
        fecha = self.vista.pedir_fecha()
        fecha_retorno = self.agenda.get_reserva(fecha)
        print(fecha_retorno)

