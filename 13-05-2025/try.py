while True:
    try:
        edad = int (input("Ingrese su edad:"))
        telefono = int (input("Ingrese su edad:"))
        
    except ValueError:
        print(f"Error, puede ingresar solo números")
    else:
        break
    finally:
        print("Finally")

