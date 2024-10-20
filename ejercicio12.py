'''
Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos
puntos en el plano. Calcula y muestra la distancia entre ellos.

'''

x1 = input("Introduce la coordenada x1: ")
x1 = int(x1)
y1 = input("Introduce la coordenada y1: ")
y1 = int(y1)
x2 = input("Introduce la coordenada x2: ")
x2 = int(x2)
y2 = input("Introduce la coordenada y2: ")
y2 = int(y2)

d = ((x2 - x1)**2 + (y2 - y1)**2)**(1/2)
print("La distancia es de: ",d)

''' float== para numeros decimales, negativos, etc'''