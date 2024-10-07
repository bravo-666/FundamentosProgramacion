'''
Programa que calcule el area y el perimetro de un rectangulo a partir de su base y su altura 
    Entrada: 
        base: integer
        altura: interger
    Salidas: 
        perimetro: interger
        area: interger
    Analisis:
        Se requere calcular con las formulas para area y perimetro
'''
print ("Programa y calcula el area y el perimetro de un rectangulo")
Base = input("Base: ")
Base = int(Base)
Altura = input("Altura: ")
Altura = int(Altura)
Area = Base * Altura
Perimetro = Base + Base + Altura + Altura
print ("El area del rectangulo es ", Area)
print ("El perimetro del rectangulo es ", Perimetro)
