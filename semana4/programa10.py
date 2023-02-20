"""
       Programa10
       Nombre: Armando CS
       Fecha: 09/02/2023
       Descripcion: Numero mayor o None
"""
def mayor(numero1,numero2):  # define una funcion
    result = None  # la variable result se le asginara None dependiendo de las condiciones
    if numero1 > numero2:  # Condiciona si numero 1 es mayor que numero 2
        result = numero1  # la variable result se le asignara numero 1 si la condicion es verdadera
    elif numero2 > numero1:  # Condiciona si numero 2 es mayor que numero 1
        result = numero2  # la variable result se le asignara numero 2 si la condicion es verdadera
    return result  # si se cumple la condicion anterior, se regresa a result   
print()  # Se imprime un espacio
print(mayor(2,1)) #2
print(mayor(1,2)) #2
print(mayor(2,2)) #None
print(mayor(2,-1)) #2
print(mayor(-1,2)) #2
print(mayor(-1,-1)) #None
print(mayor(-2,-1)) #-1
print(mayor(-1,-2)) #-1