"""
	Problema 1
	author: @daniel-alejandro-t
"""

'''
	Se desea realizar un programa que permita calcular el valor mensual a pagar a un trabajador; así
como también el valor de su descuento al Seguro Social (10% del total a pagar). El sueldo mensual
del trabajador se obtienen mediante una multiplicación simple entre el número de horas (100), por
el costo hora oficial.
'''

#Pedir por teclado el numero de horas y costo/hora
numeroHoras = input("Ingrese el numero de horas trabajadas")
costoHora = input("Ingrese el costo/hora")

#Se realiza el calculo y el casting a cada dato
salario = float(numeroHoras) * float(costoHora)

#Se calcula el seguro
seguro = float(salario) / 100 * 10

#se resta el seguro del sueldo
salario -= seguro
#Se devuelve el salario
print("El empleado ha trabajo " , numeroHoras , " horas, a " , costoHora , "$/hora /n")
print("Se pagara " ,  salario , "$ + " , seguro , "$ del seguro")