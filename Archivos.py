# n = int(input("Ingrese el número de tabla que desea imprimir: "))
f = open("tablas.txt", "a")
arch = open(r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\PRUEBAS.txt", "a+")


# archivo = open(rf"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\TABLAS de {n}.txt", "x")


def tablas(n):
    for i in range(11):
        print(f"{n} x {i} = {n * i}")
        f.write(f"{n} x {i} = {n * i}")
        arch.write(f"{n} x {i} = {n * i} \n")
        archivo.write(f"{n} x {i} = {n * i} \n")
    f.close()
    arch.close()
    archivo.close()


# tablas(n)

print(arch.read())


def imprimi_linea_archivo():
    linea = []
    x = int(input("Ingrese el número de la tabla en la que desea imprimir: "))
    archive = open(fr"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\TABLAS de {x}", "a+")
    y = int(input(f"Ingrese el número de linea que desea imprimir de la tabla del {x}: "))
    for i in archive.readlines():
        if i == y-1:
            print(f"{i}")
    print(linea)
    archive.close()


imprimi_linea_archivo()
