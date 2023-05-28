from Modelado.alumno import Alumno
from Modelado.examen import Examen

alumno1 = Alumno("Matias", 15756)
alumno2 = Alumno("Nicolas", 12589)

print(alumno1)
print(type(alumno1))

examen1 = Examen("15-05-23", 8)
examen2 = Examen("15-05-23", 9)
examen3 = Examen("16-07-23", 6)

alumno1.add_examen(examen1)
alumno2.add_examen(examen2)
alumno1.add_examen(examen3)


alumno1.get_examenes()

print(f"Promedio: {alumno2.get_promedio()}")
