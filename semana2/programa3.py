"""
       Programa3
       Nombre: Armando CS
       Fecha: 24/01/2023
       Descripcion: Print y Operaciones Aritmétcas
"""
numero1 = 10  # Se le asigna el valor 10 a numero 1
numero2 = 5  # Se le asigna el valor 5 a numero 2
print(numero1 + numero2)  # Imprime el resultado de la suma de numero 1 y numero2 
print("{} + {}".format(numero1 , numero2))  # Imprime literalmente la numero 1 + numero 2
print("{} + {} = {}".format(numero1 , numero2 , (numero1 + numero2)))  # Imprime la operacion de las variables y el resultado de esta

numero3 = 5  # Se le asigna el valor 5 a numero 3
numero4 = 10  # Se le asigna el valor 10 a numero 4
print(numero3 * numero4)
print("{} * {}".format(numero3 , numero4))
print("{} = {} * {}".format((numero3 * numero4) , numero3 , numero4))

variable1 = "El resultado de dividir"   # Variable que almacena una cadena de caracteres. STR
variable2 = "es"   # Variable que almacena una cadena de caracteres. STR
numero5 = 10  # Se le asigna el valor 10 a numero 5
numero6 = 5  # Se le asigna el valor 5 a numero 6
print(numero5 / numero6)  # Imprime el resultado de la division de numero 5 y numero 6
print("{} / {}".format(numero5 , numero6))  # Imprime el formato de la operacion entre numero 5 y numero 6
print("{} {} / {} {} {}".format(variable1 , numero5 , numero6 , variable2 , (numero5 / numero6)))  # Imprime el formato de la operacion de las variables junto con su respectivo resultado