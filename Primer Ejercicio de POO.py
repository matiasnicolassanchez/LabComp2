class Persona:
    def __init__(self, nombre=" ", edad=" ", dni=" "):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni

    def mostrar(self):
        print(self.nombre, self.dni, self.edad)

    def mayor_de_edad(self):
        if int(self.edad) >= 18:
            print(f"{self.nombre} es MAYOR de edad")
        else:
            print(f"{self.nombre} es MENOR de edad")


matias = Persona("Matias", "16", "39026709")
matias.mostrar()
matias.mayor_de_edad()
