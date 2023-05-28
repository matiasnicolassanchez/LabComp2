class Alumno:
    def __init__(self, nombre, legajo):
        self.nombre = nombre
        self.legajo = legajo
        self.examenes = []

    def __str__(self):
        return f"{self.nombre} - Legajo:{self.legajo}"

    def add_examen(self, examen):
        self.examenes.append(examen)

    def get_examenes(self):
        for exam in self.examenes:
            print(exam)
    def get_promedio(self):
        suma = 0
        for exam in self.examenes:
            suma += exam.get_nota()
        prom = suma / len(self.examenes)
        return prom

