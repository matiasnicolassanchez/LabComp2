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

    def set_fecha_ultimo_service(self, fecha):
        self.__fecha_ultimo_services = fecha

    def set_autos_clientes(self, auto):
        self.__autos_clientes.append(auto)

    def get_patente(self):
        return self.__patente

    def get_ultimo_kilometros(self):
        return self.__ultimo_kilometraje

    def get_fecha_ultimo_service(self):
        return self.__fecha_ultimo_services

    def new_auto_cliente(self, patente, kilometros, date):
        auto = Auto()
        auto.__set_patente(patente)
        auto.__set_ultimo_kilometraje(kilometros)
        auto.set_fecha_ultimo_service(date)
        self.__autos_clientes.append(auto)

    def obtener_registros(self):
        with open("Resources/registros.txt", "r") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                auto = Auto()
                auto.set_patente(line[0])
                auto.set_ultimo_kilometraje(line[1])
                auto.__fecha_ultimo_services(line[2])
                self.__autos_clientes.append(auto)

    def consultar_patente(self, patente):
        bandera = False
        for i in self.__autos_clientes:
            registro = i.get_patente()
            if registro == patente:
                bandera = True
                old_km = i.get_ultimo_kilometros()
                date_service = i.get_fecha_ultimo_service()
                break
            else:
                old_km, date_service = 0, 0
                pass
        return old_km, date_service, patente, bandera

    def actualizar_registros(self):
        with open("Resources/registros.txt", "w") as file:
            for car in self.__autos_clientes:
                patente = car.get_patente()
                km = car.get_ultimo_kilometros()
                date = car.get_fecha_ultimo_service()
                file.write(f'{patente};{km};{date}\n')
