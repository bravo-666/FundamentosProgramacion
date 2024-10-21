'''
Dado un número de dos cifras, diseñe un algoritmo que permita obtener el
número invertido
'''
n1 = int(input("Introduce una cantidad de dos cifras: "))
d = n1//10
u = n1%10

r = abs(u*10+d) 
print("El numero invertido es: ",r)

