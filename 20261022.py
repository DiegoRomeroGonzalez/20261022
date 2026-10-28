"""
Función que devuelve el área de un cuadrado
"""
import math
"""
ARG
Dentro de la función metemos la longitud del lado del cuadrado en unidades genéricas
"""

Figuras_validas = ["cuadrado", "círculo"]



def Area_cuadro(lado):
    area = lado**2
    return area




def Area_circulo(radio):
    Area_circulo = math.pi*radio**2
    return Area_circulo




dato = True

while dato:
    figura = input("Figura: ")
    if figura in Figuras_validas:
        if figura == "cuadrado":
            lado = float(input("Introduce las dimensiones del lado "))
            area = Area_cuadro(lado)
            texto_radio_lado = lado
            dato = False
        elif figura == "cícrulo":
            radio = float(input("Introduce el radio "))
            Area_circulo = Area_circulo(radio)
            texto_radio_lado = radio
            dato = False



    else:
        print("Introduce un figura válida.")
    print(f"El área de la figura {figura} de lado {texto_radio_lado} es de area {area}")



