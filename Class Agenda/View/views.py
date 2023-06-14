
class Vistas:

    def nueva_reserva(self):
        fecha = input("Ingrese la fecha de su evento(dd-mm-aa): ")
        if fecha[2] != "-" or fecha[5] != "-" or len(fecha) != 8:
            while fecha[2] != "-" or fecha[5] != "-" or len(fecha) != 8:
                fecha = input("Ingrese la fecha de su evento(dd-mm-aa): ")
                continue
        titular = input("Ingrese el nombre del titular de la reserva: ")
        return fecha, titular

    def pedir_fecha(self):
        fecha = input("Ingrese la fecha de su evento(dd-mm-aa): ")
        if fecha[2] != "-" or fecha[5] != "-" or len(fecha) != 8:
            while fecha[2] != "-" or fecha[5] != "-" or len(fecha) != 8:
                fecha = input("Ingrese la fecha de su evento(dd-mm-aa): ")
        return fecha

