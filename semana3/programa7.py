"""
       Programa7
       Nombre: Armando CS
       Fecha: 31/01/2023
       Descripcion: Área y Perímetro de un Círculo y un Cuadrado
"""
print("Iniciemos con el area de un circulo")
print("Ingresa el radio")
R = input("Radio: ")
area = 3.14 * int(R) * int(R)
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
l1 = input("Lado 1: ")
l2 = input("Lado 2: ")
area = int(l1) * int(l2) 
print("El área de un cuadrado con",l1,"de lado es",area)
print()
print("Ahora toca calcular su perímetro")
print("Ingrese de nueva forma sus lados")
l1 = input("Lado 1: ")
l2 = input("Lado 2: ")
l3 = input("Lado 3: ")
l4 = input("Lado 4: ")
perimetro = int(l1) + int(l2) + int(l3) + int(l4)
print("El perímetro de un cuadrado con",l1,"de lado es",perimetro)