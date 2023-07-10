from datetime import datetime


class View:

    @staticmethod
    def get_patente():
        while True:
            patente = input("INGRESE LA PATENTE DEL AUTO: ")
            if 6 > len(patente) > 7:
                pass
            else:
                break
        return patente

    @property
    def menu_principal(self):
        while True:
            try:
                opcion = int(
                    input("TALLER MECÁNICO\n1.-Consultar una patente\n2.-Consultar Bonificación\n3.- Cargar Cliente\n4.-Salir\nPOR "
                          "FAVOR INGRESE LA OPCIÓN QUE DESEA: "))
                while 1 > opcion > 4:
                    pass
                else:
                    return opcion
            except ValueError:
                print("LO INGRESADO NO ES CORRECTO ! INTENTELO NUEVAMENTE !")
                pass
        return opcion

    @staticmethod
    def mostrar_datos(old_km, date_service, patente, bandera):
        if not bandera:
            print("¡¡ EL VEHICULO NO ESTA REGISTRADO COMO CLIENTE !!")
        else:
            print(f"El vehiculo de patente:{patente}, registra el ultimo service realizado el dia:{date_service} con {old_km} kilometros")

    def pedir_datos(self):
        for i in range(3):
            if i == 1:
                patente = self.get_patente()
            if i == 2:
                while True:
                    try:
                        km = float(input("Ingrese los kilometros que registra el vehiculo: "))
                    except ValueError:
                        print("LO INGRESADO ES INCORRECTO")
                        pass
                    else:
                        break
            if i == 3:
                date = f'{datetime.day}/{datetime.month}/{datetime.year}'
        return patente, km, date
