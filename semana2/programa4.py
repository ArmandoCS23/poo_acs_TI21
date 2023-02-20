"""
       Programa4
       Nombre: Armando CS
       Fecha: 26/01/2023
       Descripcion: Acceso a variables por posición y nombre
"""
numero1 = 10   # Se le asigna el valor 10 a numero 1
numero2 = 5   # Se le asigna el valor 5 a numero 2
print("{} + {} = {}".format(numero1, numero2 , numero1 + numero2))
print("{n1} + {n2} = {suma}".format(n1 = numero1, n2 = numero2, suma = numero1 + numero2))  # Imprime la operacion de las variables junto con su resultado
print("{n2} + {n2} = {n2}".format(n1 = numero1, n2 = numero2, suma = numero1 + numero2))  # Imprime las variables n2
print("{numero1} + {numero2} = {suma}".format(numero1 = numero1, numero2 = numero2, suma = numero1 + numero2))  # Imprime de igual manera que la linea 10 la operacion