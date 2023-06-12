
class Vistas:

    def nueva_reserva(self):
        fecha = input("Ingrese la fecha de su evento: ")
        titular = input("Ingrese el nombre del titular de la reserva: ")
        return fecha, titular

    def pedir_fecha(self):
        fecha = input("Ingrese la fecha de su evento: ")
        return fecha

