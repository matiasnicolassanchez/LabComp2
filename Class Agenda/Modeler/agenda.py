import datetime

from self import self


class Agenda:

    def __init__(self):
        self.__fecha_reservada = str
        self.__titular_reserva = str
        self.__registros_agenda = []

    def __str__(self):
        return f"FECHA RESERVADA: {self.__fecha_reservada}, NOMBRE DEL TITULAR DE RESERVA: {self.__titular_reserva}"

    def set_registros(self, agenda):
        objeto = Agenda()
        for line in agenda:
            objeto.__fecha_reservada = line[0]
            objeto.__titular_reserva = line[1]
            self.__registros_agenda.append(objeto)

    def set_nueva_reserva(self, fecha, titular):
        objeto = Agenda()
        objeto.__fecha_reservada = fecha
        objeto.__titular_reserva = titular
        self.__registros_agenda.append(objeto)

    @staticmethod
    def verificar_existencia_archivo():
        try:
            with open("Resources/agenda.txt", "r"):
                pass
        except FileNotFoundError:
            with open("Resources/agenda.txt", "x"):
                pass

    def actualizar_registros(self):
        with open("Resources/agenda.txt", "a") as file
            for line in self.__registros_agenda:
                file.write(f"{line[0]};{line[1]}\n")


    def get_reserva(self, fecha):
        for line in self.registros_agenda:
            if line[0] == fecha:
                disponibilidad = False
                while True:
                    dia = int(fecha[0:2])
                    mes = int(fecha[3:5])
                    año = fecha[6:9]
                    if dia == 30:
                        dia = 1
                        mes = mes + 1
                    else:
                        dia = str(dia + 1)
                    fecha_cercana = f"{dia}/{mes}/{año}"
                    for registro in self.registros_agenda:
                        if registro[0] == fecha_cercana:
                            pass
                        else:
                            break
                    break
                break
            else:
                disponibilidad = True
                fecha_cercana = fecha
                break
        return disponibilidad, fecha_cercana


