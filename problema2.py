"""
	Problema 1
	author: @daniel-alejandro-t
"""

'''
	Ingresar por teclado la variables: x,y,z (solo puede usar nextLine()).
En base a las mismas realizar la siguiente operación:
	m = (x+y/z)/(x-y/z)
y finalmente presentar en pantalla el siguiente reporte:
El valor de m, en base a las variables:
x = 10.2
	y = 9.2
		z = 8.2
da como resultado:
	m = ?
'''
#Se ingresa el valor de x, y, z
x = input("Ingrese X: ")
y = input("Ingrese Y: ")
z = input("Ingrese Z: ")

#Se realiza el casting y el calculo de m
m = (float(x)+float(y)/float(z))/(float(x)-float(y)/float(z))

#Salida
print("El valor de m, en base a las variables:")
print(" \nx = " , x)
print("\ty = " , y , "\n\t\tz = " , z)
print("da como resultado:\n\t\t\tm = " , m)