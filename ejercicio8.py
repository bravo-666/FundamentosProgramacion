'''
Un vendedor recibe un sueldo base más un 10% extra por comisión de sus
ventas, el vendedor desea saber cuánto dinero obtendrá por concepto de
comisiones por las tres ventas que realiza en el mes y el total que recibirá en el mes
tomando en cuenta su sueldo base y comisiones.

sb = sueldo base
v = venta
c = comicion
sf = sueldo final
'''
sb = input("Introduzca el sueldo base: ")
sb = int(sb)
c = sb / 100 * 10
v = c * 3
sf = sb + v 
print("Sueldo base: ", sb)
print("Comicion de una venta: ", c)
print("Comicion por tres ventas: ", v)
print("Sueldo final: ", sf)
