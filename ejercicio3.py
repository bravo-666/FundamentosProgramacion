import math 
a = input("Escribe el valor de cateto A: ")
a = int (a)
b = input ("Escribe el valor del cateto B: ")
b = int(b)
c = (a * a + b * b) ** (1/2)
c = math.sqrt (a * a + b * b)
print("El valor  de la hipotenusa: ", c)
