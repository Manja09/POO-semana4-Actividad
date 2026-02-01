def menu():
    print("Menu")
    print("1. Saludar")
    print("2. Salir")
    opcion = input("Seleccione una opcion: ")
    return opcion

while True:
    choise = menu()
    if choise == "1":
        print("Hola! Estas usando una CLI en python.")
    elif choise == "2":
        break
    else:
        print("Opcion no valida")