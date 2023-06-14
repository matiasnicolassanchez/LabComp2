import datetime

from self import self


class Agenda:

    def __init__(self):
        self._fecha_reservada = str
        self._titular_reserva = str
        self._registros_agenda = []

    def __str__(self):
        return f"FECHA RESERVADA: {self.__fecha_reservada}, NOMBRE DEL TITULAR DE RESERVA: {self.__titular_reserva}"

    def set_registros(self, agenda):
        objeto = Agenda()
        for line in agenda:
            objeto.__fecha_reservada = line[0]
            objeto.__titular_reserva = line[1]
            self._registros_agenda.append(objeto)

    def set_nueva_reserva(self, fecha, titular):
        objeto = Agenda()
        objeto.__fecha_reservada = fecha
        objeto.__titular_reserva = titular
        self._registros_agenda.append(objeto)
        self.actualizar_registros(fecha, titular)

    @staticmethod
    def verificar_existencia_archivo():
        try:
            with open("Resources/agenda.txt", "r"):
                pass
        except FileNotFoundError:
            with open("Resources/agenda.txt", "x"):
                pass

    @staticmethod
    def actualizar_registros(fecha, titular):
        with open("Resources/agenda.txt", "a") as file:
            file.write(f"{fecha};{titular}\n")

    def get_reserva(self, fecha):
        fecha_cercana = fecha
        fechas = self.obtener_fechas()
        for line in fechas:
            if line == fecha:
                while True:
                    dia = int(fecha[0:2])
                    mes = int(fecha[3:5])
                    año = int(fecha[6:9])
                    if dia == 30:
                        dia = 1
                        mes = mes + 1
                    if mes == 12:
                        mes = 1
                        año = año + 1
                    else:
                        dia = dia + 1
                    fecha_cercana = f"{dia}-{mes}-{año}"
                    for registro in fechas:
                        if registro == fecha_cercana:
                            pass
                        else:
                            break
                    break
                break
        return fecha_cercana

    def obtener_fechas(self):
        fechas = []
        for i in self._registros_agenda:
            fecha = i.__fecha_reservada
            fechas.append(fecha)
        return fechas
