from Modelado.pago import Pago


class Efectivo(Pago):
    def __init__(self, monto):
        super.__init__(monto)