from Modelado.viaje import Viaje
from Modelado.pago import Pago
from Vistas.vistaViaje import VistaViaje


class Controlador:
    def crear_reserva_viaje(self):
        viaje = Viaje.reservarViaje(self, fecha=VistaViaje.ingresar_fecha(self),
                                    inicio_viaje=VistaViaje.ingresar_inicio_viaje(self),
                                    final_viaje=VistaViaje.ingresar_final_viaje(self))

