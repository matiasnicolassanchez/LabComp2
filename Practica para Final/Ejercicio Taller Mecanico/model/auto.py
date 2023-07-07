
class Auto:
    def __init__(self):
        self.__patente = str
        self.__ultimo_kilometraje = int
        self.__fecha_ultimo_services = str
        self.__autos_clientes = []

    def set_patente(self, patente):
        self.__patente = patente

    def set_ultimo_kilometraje(self, kilometros):
        self.__ultimo_kilometraje = kilometros

    def set_autos_clientes(self, auto):
        self.__autos_clientes.append(auto)

    def new_auto_cliente(self, patente, kilometros):
        auto = Auto()
        auto.__set_patente(patente)
        auto.__set_ultimo_kilometraje(kilometros)

