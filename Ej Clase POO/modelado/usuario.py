class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo

    def get_nombre(self):
        return self.nombre

    def get_correo(self):
        return self.correo

    def get_info_usuario(self):
        return {"nombre": self.get_nombre(), "correo": self.get_correo()}
