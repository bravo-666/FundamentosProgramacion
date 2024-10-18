'''
Una tienda ofrece un descuento del 15% sobre el total de la compra y un cliente
desea saber cuánto deberá pagar finalmente por su compra.

p = presio
d = descuento
t = total con descuento

'''
p = input("Introduzca el precio de la prenda: $")
p = int(p)
d = p / 100 * 15
t = p - d
print("Descuento: $",d)
print("Precio total con descuento: $",t)
