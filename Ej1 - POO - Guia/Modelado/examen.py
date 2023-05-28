class Examen:
    def __init__(self, fecha, nota):
        self.fecha = fecha
        self.nota = nota

    def __str__(self):
        return f"fecha:{self.fecha} - nota:{self.nota}"

    def get_nota(self):
        return self.nota


