class View:

    @staticmethod
    def get_patente():
        patente = input("Ingrese la patente del vehiculo: ").upper()
        return patente

    def menu_principal(self):
        opcion = input("TALLER MECÁNICO\n1.-Consultar una patente\n2.-Consultar Bonificación\nPOR FAVOR INGRESE LA "
                       "OPCIÓN QUE DESEA: ")
        return opcion

