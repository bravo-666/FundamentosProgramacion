'''
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados
Celsius.
c = grados celcius
f = grados fahrenheit
r = respuesta
'''
f = input("Introduce los grados Fahrenheit: ")
f = int(f)
c = (f - 32) / 1.8
print("La temperatura en grados Celcius es:", c)
