class Libros:
    def __init__(self):
        self.titulo = str
        self.autor = str
        self.cantidad = int
        self.prestados = int
        self.registro = []

    # Setter y getter por atributo
    def set_titulo(self, titulo):
        self.titulo = titulo

    def get_titulo(self):
        titulo = self.titulo
        return titulo

    def set_autor(self, autor):
        self.autor = autor

    def get_autor(self):
        autor = self.autor
        return autor

    def set_cantidad(self, cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        cantidad = self.cantidad
        return cantidad

    def set_prestado(self, id_prestado):
        for libro in self.registro:
            if libro[0] == str(id_prestado):
                libro[4] = int(libro[4]) + 1
                libro[3] = int(libro[3]) - 1
                break

    def get_prestados(self):
        prestados = self.prestados
        return prestados

    # Se obtienen los registros plasmados en el archivo
    def get_registros(self):
        registro = []
        with open("Recursos/libros.txt", "r") as file:
            for line in file:
                line = line.rstrip().split(sep=";")
                registro.append(line)
        self.registro = registro

    # Se obtiene el nombre y la cantidad disponible de cada libro
    def get_disponibilidad(self):
        disponibilidad = []
        for libro in self.registro:
            carga = []
            carga.append(libro[1])
            carga.append(libro[3])
            disponibilidad.append(carga)
        return disponibilidad

    # Se obtiene el nombre del libro con su id
    def get_listado_libros(self):
        listado = []
        for list in self.registro:
            carga = []
            carga.append(list[0])
            carga.append(list[1])
            listado.append(carga)
        return listado

    # Actualiza los registros del archivo
    def actualiazar_registros(self):
        with open("Recursos/libros.txt", "w") as file:
            for line in self.registro:
                file.write(f"{line[0]};{line[1]};{line[2]};{line[3]};{line[4]}\n")

    # Registra la devolución de un libro
    def set_devolucion(self, id_libro):
        for libro in self.registro:
            if libro[0] == str(id_libro):
                libro[3] = int(libro[3]) + 1
                libro[4] = int(libro[4]) - 1
                break
