"""
	Ejemplo de lenguaje python
	author: @daniel-alejandro-t
"""

import sys

salidaSuma = 0
salidaMultiplicacion = 0

#Sepide los valores
dato1 = input("Ingrese el valor 1")

dato2 = input("Ingrese el valor 2")

#Se realiza el casting y las operaciones
salidaSuma = int(dato1) + int(dato2)
salidaMultiplicacion = int(dato1) * int(dato2)

#salida:
print("La suma es :	%d \nLa multiplicacion es:	%d" % (salidaSuma, salidaMultiplicacion))