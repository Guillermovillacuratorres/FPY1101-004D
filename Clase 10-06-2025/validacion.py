def valida_numero_entero_positivo(mensaje_input:str):
    """Valida que un numero sea entero y positivo."""
    while True:
        try:
            numero = int(input(mensaje_input))
            if numero < 0:
                print("El numero debe ser positivo.")
                continue
        except ValueError:
            print("No puede ingresar caracteres.")
            continue
        return numero
        
#opcion = valida_numero_entero_positivo("Ingrese la opcion:")
#print(opcion)


def valida_texto(mensaje:str):
    """Valida el largo de un texto."""
    while True:
        texto = input(mensaje)
        if len(texto) == 0:
            print("El texto no puede estar vacio.")
            continue
        elif len(texto) > 1:
            print("El texto no puede contener mas de un caracter.")
            continue
        return texto

#valida_texto("Ingrese A o B o C: ")