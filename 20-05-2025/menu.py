while True:
    try:
        numero_uno = int(input("Ingrese el primer número:"))
        numero_dos = int(input("Ingrese el segundo número:"))

        if numero_uno < 0 or numero_dos < 0:
            print("No puede ingresar numeros negativos.")
            continue
        break
    except ValueError:
        print("Solo puede ingresar numeros enteros.")
        continue



while True:
    print("-----MENU-----")
    print("[1] - Sumar")
    print("[2] - Restar")
    print("[3] - Multiplicar")
    print("[4] - Salir")
    try:
        opcion = int(input("Ingrese una opcion:"))
    except ValueError:
        print("Solo se aceptan numeros enteros.")
        continue

    if opcion == 1:
        print("El resultado de la suma es: ", numero_dos + numero_uno)
    elif opcion == 2:
        print("El resultado de la resta es: ", numero_dos - numero_uno)
    elif opcion == 3:
        print("El resultado de la multiplicación es: ", numero_dos * numero_uno)
    elif opcion == 4:
        print("Saliendoooo!!!!!!!!")
        break
    else:
        print("La opcion igresada no es valida. Debe ser la opcion 1,2,3 o 4")