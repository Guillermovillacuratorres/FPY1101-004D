datos = {
    "productos":
    [
        {
            "id_producto":1,
            "nombre":"parlante",
            "precio":500,
            "cantidad":10
        },
        {
            "id_producto":2,
            "nombre":"audifonos",
            "precio":790,
            "cantidad":59
        }
    ]
}



while True:
    print("1 - Agregar producto")
    print("2 - Listar producto")
    print("3 - Editar producto")
    print("4 - Eliminar producto")
    print("5 - Salir")

    opcion = int(input("Ingrese una opcion: "))

    if opcion == 1:
        id_producto = int(input("Ingrese el id del producto: "))
        nombre = input("Ingrese el nombre del producto: ")
        precio = int(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad del producto: "))

        producto_agregar = {
                                "id_producto":id_producto,
                                "nombre":nombre,
                                "precio":precio,
                                "cantidad":cantidad
                            }
        
        datos["productos"].append(producto_agregar)
        print("Producto agregado correctamente!!!!!!!!")

    elif opcion == 2:
        for i in datos["productos"]:
            print(f"NOMBRE: {i["nombre"]} - PRECIO:{i["precio"]} - CANTIDAD{i["cantidad"]}")

    elif opcion == 3:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if id_producto == i["id_producto"]:
                nombre = input("Ingrese el nombre del producto: ")
                precio = int(input("Ingrese el precio del producto: "))
                cantidad = int(input("Ingrese la cantidad del producto: "))
                i["nombre"] = nombre
                i["cantidad"] = cantidad
                i["precio"] = precio
                print("Producto actualizado exitosamente!!!")

    elif opcion == 4:
        id_producto = int(input("Ingrese el id del producto: "))
        for i in datos["productos"]:
            if i["id_producto"] == id_producto:
                datos["productos"].remove(i)
                print("producto eliminado correctamente!")
    else: 
        print("opcion no valida!")
print(datos["productos"][1]["nombre"])