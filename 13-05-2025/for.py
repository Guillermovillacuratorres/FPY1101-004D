"""multiplo = int(input("Ingrese la cantidad de multiplos:"))
tabla = int(input("Ingrese la tabla de multiplicar:"))

for i in range(multiplo):
    print(f"{i+1} X {tabla} = {(i+1)*tabla}")
"""

#10 * ancho
#20 * largo

for i in range(10):
    for j in range(20):
        print("*", end="")
    print("*")
