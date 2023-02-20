"""
       Programa6
       Nombre: Armando CS
       Fecha: 30/01/2023
       Descripcion: Área y Perímetro de un Triangulo
"""
print("Ingrese los datos para calcular el perimetro")  # Imprime la cadena de caracteres tipo .str
l1 = input("Lado 1: ")  # Permite asignarle un valor a l1
l2 = input("Lado 2: ")  # Permite asignarle un valor a l2
l3 = input("Lado 3: ")  # Permite asignarle un valor a l3
perimetro = int(l1) + int(l2) + int(l3)  # A la variable perimetro se le asigna la operacion de suma con las variables l1, l2 y l3
print("el resultado del perimetro de un triangulo es: ",perimetro)  # Imprime una cadena de caracteres tipo .str junto con el resultado de la variable perimetro
print()  # Imprime un espacio
print("Ingrese los datos para calcular el área")  # Imprime una cadena de caracteres tipo .str
B = input("Base : ")  # Permite asiganrle un valor a B
H = input("Altura : ")  # Permite asignarle un valor a H
area = int(B) * int(H) / 2  # A la vaiable area de le asigna la operacion de multiplicacion con las variables B y H junto con una divion con el valor entero 2
print("el resultado del área de un triangulo es: ",area)  # Imprime una cadena de caracteres tipo .str junto con el resultado de la variable area