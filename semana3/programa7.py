"""
       Programa7
       Nombre: Armando CS
       Fecha: 31/01/2023
       Descripcion: Área y Perímetro de un Círculo y un Cuadrado
"""
print("Iniciemos con el area de un circulo")
print("Ingresa el radio")
R = input("Radio: ")
area = 3.14 * int(R)**2
print("El área de un círculo de",R,"de radio es",area)
print()
print("Ahora pasemos con su perímetro")
print("Ingrese el radio nuevamente")
R = input("Radio: ")
perimetro = 2 * 3.14 * int(R)
print("El perímetro de un círculo de",R,"de radio es",perimetro)
print()
print("Ahora pasaremos con el area de un cuadrado")
print("Ingrese los lados del cuadrado")
l = input("Lado : ")
area = int(l) * int(l) 
print("El área de un cuadrado con",l,"de lado es",area)
print()
print("Ahora toca calcular su perímetro")
print("Ingrese de nuevamente su lado")
l = input("Lado : ")
perimetro = int(l) + int(l) + int(l) + int(l)
print("El perímetro de un cuadrado con",l,"de lado es",perimetro)