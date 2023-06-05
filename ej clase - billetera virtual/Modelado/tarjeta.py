from Modelado.pago import Pago


class Tarjeta(Pago):
    def __init__(self, monto: float, tipo: str, titular: str, numero: float, codigo: int, vencimiento: str):
        super.__init__(monto)
        self.tipo = tipo
        self.titular = titular
        self.numero = numero
        self.codigo = codigo
        self.vencimiento = vencimiento
