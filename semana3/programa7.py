"""
       Programa7
       Nombre: Armando CS
       Fecha: 31/01/2023
       Descripcion: Área y Perímetro de un Círculo y un Cuadrado
"""
print("Iniciemos con el area de un circulo")  # Imprime una cadea de caracteres tipo .str
print("Ingresa el radio")  # Imprime una cadea de caracteres tipo .str
R = input("Radio: ")  # Permite asignarle un valor a R
area = 3.14 * int(R)**2  # La variable area se le asigna una operacion con la variable r junto con variables tipo .int
print("El área de un círculo de",R,"de radio es",area)  # Imprime una cadena de caracteres tipo . str junto con las anteriores variables
print()  # Imprime un espacio
print("Ahora pasemos con su perímetro")  # Imprime una cadea de caracteres tipo .str
print("Ingrese el radio nuevamente")  # Imprime una cadea de caracteres tipo .str
R = input("Radio: ")  # Permite asignarle un valor a r
perimetro = 2 * 3.14 * int(R)  # a la variable perimetro se le asigna la operacion multiplicacion de la variable R junto con dos variables tipo .int 
print("El perímetro de un círculo de",R,"de radio es",perimetro)  # Imprime una cadena de caracteres tipo . str junto con las anteriores variables
print()  # Imprime un espacio
print("Ahora pasaremos con el area de un cuadrado")  # Imprime una cadea de caracteres tipo .str
print("Ingrese los lados del cuadrado")  # Imprime una cadea de caracteres tipo .str
l = input("Lado: ")  # Permite asignarle un valor a l
area = int(l) * int(l)  # A la variable area se le asigna la operacion multiplicacion de la variable l
print("El área de un cuadrado con",l,"de lado es",area)  # Imprime una cadena de caracteres tipo . str junto con las anteriores variables
print()  # Imprime un espacio
print("Ahora toca calcular su perímetro")  # Imprime una cadea de caracteres tipo .str
print("Ingrese de nuevamente su lado")  # Imprime una cadea de caracteres tipo .str
l = input("Lado: ")  # Permite asignarle un valor a l
perimetro = int(l) + int(l) + int(l) + int(l)  # a la variable perimetro se le asigna la operacion suma de la variable l
print("El perímetro de un cuadrado con",l,"de lado es",perimetro)  # Imprime una cadena de caracteres tipo . str junto con las anteriores variables