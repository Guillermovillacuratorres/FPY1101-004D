#Sin argumentos - sin retorno
def sumar():
    """Suma dos numeros"""
    print(1+2)
sumar()

#Con argumentos - sin retorno
def sumar(n1:int,n2:int,nombre:str="Juan"):
    """Suma dos numeros enteros"""
    print(n1+n2," " + nombre)
sumar(n2=50,n1=90,nombre="Pedro")


#Sin argumentos - con retorno
def multiplicar():
    """Multiplica dos numeros enteros"""
    return 10*90

multi = multiplicar()

print(multi)
print(50+50)


#Con argumento - con retorno
def multiplicar(n1:int,n2:str)-> str:
    """Multiplica dos numeros enteros"""
    return n1 * n2

print(multiplicar(10,'10'))
