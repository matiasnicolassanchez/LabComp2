from math import pi


def saludo(nombre):
    print(f"Hola {nombre}")

def fact(i):
    resultado = 1
    for i in range(1, i+1):
        resultado = resultado * i
    return resultado

def calc_iva(monto, iva=21):
    monto_final = monto + (monto * (iva/100))
    return monto_final


def area_circ(diam):
    area = ((diam/2)**2)*pi
    return area

def vol_circ(d, h):
    vol = area_circ(d) * h
    return vol

nombre = input("Ingrese su nombre: ")
saludo(nombre)



print(fact(int(input("Ingrese un numero: "))))

monto = int(input("Ingrese el monto de la factura: "))
iva = int(input("Ingrese el porcentaje de iva que desea aplicar: "))
print(calc_iva(monto))

print(area_circ(int(input("Ingrese el diametro de su circulo: "))))

print(vol_circ(int(input("Ingrese el diametro de su cilindro: ")), int(input("Ingrese la altura de su cilindro: "))))