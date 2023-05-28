class VistaUsuario:

    def solicitar_nombre_usuario(self):
        return input("Ingrese el nombre del usuario: ")

    def solicitar_correo_usuario(self):
        return input("Ingrese el correo del usuario: ")

    def mostrar_informacion(self, data):
        print("INFORMACIÓN DEL USUARIO")
        print(f"Nombre: {data['nombre']} - correo: {data['correo']}")
