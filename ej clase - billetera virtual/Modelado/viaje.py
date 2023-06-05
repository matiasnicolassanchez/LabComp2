from Modelado.pago import Pago
class Viaje:
    def __init__(self, fecha: str, inicio: str, llegada: str):
        self.__fecha = fecha
        self.inicio = inicio
        self.llegada = llegada
        self.pago = None
        self.cacelado = False

    def reservarViaje(self, pago):
        if not isinstance(pago, Pago):
            return False

    def cancelar_viaje(self):
        self.cacelado = True
        return True


