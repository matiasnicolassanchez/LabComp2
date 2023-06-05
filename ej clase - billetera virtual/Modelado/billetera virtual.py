from Modelado.pago import Pago


class BilleteraVirtual(Pago):
    def __init__(self, monto: float, tipo: str, titular: str, cvu: float):
        super.__init__(monto)
        self.tipo = tipo
        self.titular = titular
        self.cvu = cvu
