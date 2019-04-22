"""
	Ejemplo de lenguaje python
	author: @daniel-alejandro-t
"""

import sys

salidaSuma = int(0)
salidaMultiplicacion = int(0)

variable = sys.argv[0]
dato1 = sys.argv[1]
dato2 = sys.argv[2]

salidaSuma = int(dato1)+int(dato2)
salidaMultiplicacion = int(dato1)*int(dato2)

print("La suma es :	%s" % salidaSuma)
print("La multiplicacion es:	%s" % salidaMultiplicacion)
