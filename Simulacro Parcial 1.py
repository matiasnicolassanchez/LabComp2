from datetime import datetime


def calc_costo(categoria):
    costo_peaje = 0
    if categoria == 1:
        costo_peaje = 100
    if categoria == 2:
        costo_peaje = 150
    if categoria == 3:
        costo_peaje = 300
    if categoria == 4:
        costo_peaje = 500
    return costo_peaje


def reg_paso_vehiculo(vector, matriz_alm):
    matriz = matriz_alm
    with open(archivo_registro, "a") as arch:
        arch.write(
            f"{vector[0]},{vector[1]},{vector[2]},{vector[3]},{vector[4]} \n")
        print(f"El vehiculo ha sido cargado CORRECTAMENTE")
    matriz.append(vector)
    return matriz


def reg_cierre_peaje():
    with open(archivo_registro, "a") as arch:
        arch.write("¡¡ CIERRE DE PEAJE !! \n")
    print("¡¡ REGISTRO DE VEHICULOS CERRADO !!")
    cambio_var_trabajando = 0
    return cambio_var_trabajando


def ver_vehiculo_reg(patente):
    paso = 0
    with open(archivo_registro, "r") as arch:
        for line in arch:
            # print(line)
            linea = line.split(",")
            # print(linea)
            if patente == linea[0]:
                print(f"El vehiculo de patente {patente}, ya ha abonado en el dia de hoy, EL PEAJE ES SIN COSTO")
                paso = 1
                break
    return paso


def imprimir_ticket(cant_autos, dinero):
    print(f"El cierre de jornada registra que pasaron {cant_autos} autos y una recaudación total de ${dinero}")


archivo_registro = r"D:\Usuario\Desktop\MATIAS\UTN\Tec. en Programacion\Lab de Computación II\REG_PEAJE.txt"
matriz_almacenamiento = []
vector_carga = []
cat = int
valor_peaje = int
var_trabajando = 1
now = datetime.now()
fecha = now.date()
hora = now.time()
cont_autos = 0
recaudacion: [float] = 0

while var_trabajando != 0:
    cont_autos += 1
    vector_carga = []
    print("Ingrese CLOSE DAY, en el campo de PATENTE, si desea cerrar el dia de trabajo")
    patente_veh = input("Ingrese la patente(SIN ESPACIOS) del vehiculo: ").lower()
    if len(patente_veh) == 7 or len(patente_veh) == 6:
        vehiculo_paso = ver_vehiculo_reg(patente_veh)
        vector_carga.append(patente_veh)
        vector_carga.append(f"{fecha.day}/{fecha.month}/{fecha.year}")
        vector_carga.append(f"{hora.hour}:{hora.minute}:{hora.second}")
        if vehiculo_paso == 0:
            print("EL VEHICULO NO ESTA REGISTRADO EN EL DIA DE HOY, DEBE ABONAR")
            try:
                cat = int(input("Ingrese la categoria a la que pertenece el vehiculo: "))
                while cat > 4 or cat < 1 or cat == str:
                    print("¡¡ EL VALOR INGRESADO ESTA FUERA DEL RANGO DE CATEGORIAS !!\n")
                    cat = int(input("Ingrese la categoria a la que pertenece el vehiculo: "))
            except ValueError:
                while cat < 1 or cat > 4 or cat == str:
                    print("¡¡ EL VALOR INGRESADO NO PERTENECE A UNA CATEGORIA !!\n")
                    cat = int(input("POR FAVOR INGRESE NUEVAMENTE LA CATEGORIA: "))
            valor_peaje = calc_costo(cat)
            recaudacion += valor_peaje
            print(f"El costo del peaje es de ${valor_peaje}")
            vector_carga.append(cat)
            vector_carga.append(valor_peaje)
            matriz_almacenamiento = reg_paso_vehiculo(vector_carga, matriz_almacenamiento)
            # print(matriz_almacenamiento)
    elif patente_veh == "close day":
        var_trabajando = reg_cierre_peaje()
        imprimir_ticket(cont_autos, recaudacion)
    else:
        print("LA PATENTE O EL FORMATO SON INCORRECTOS. Intente nuevamente")
        continue
