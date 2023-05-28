class Servicio():
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def __str__(self):
        return f"dj: ${self.precio}"


dj = Servicio("Dj", 15000)
decoracion = Servicio("Decoración", 10000)
cotillon = Servicio("Cotillon", 13000)
maquina_humo = Servicio("Maquina de humo", 5000)
maquillaje = Servicio("Maquillaje", 3500)
musica_vivo = Servicio("Musica en vivo", 50000)
locutor = Servicio("Locutor", 4000)
fotografo = Servicio("Fotografo", 15000)
cathering = Servicio("Catering", 60000)
bara_movil = Servicio("Barra movil", 12000)

print(dj)