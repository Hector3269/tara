def menu(opcion):
    opciones = {
        1: "Opción 1: Ver informacion",
        2: "Opción 2: Realizar proceso de registro",
        3: "Opción 3: Salir"
    }
    return opciones.get(opcion, "Opcion no valida")
 
 
print("Seleccione una opcion:")
print("1. Ver información de los jugadores para conoserlos ")
print("2. Realizar proceso de registro para conoser a tu idolo  ")
print("3. Salir")
 
try:
    opcion_usuario = int(input("Ingresa tu opcion: "))
    resultado = menu(opcion_usuario)
    print(resultado)
 
    if opcion_usuario == 1:
        print("Incripciones abiertas desde el 5 de enero para conoser a tu idolo")
    elif opcion_usuario == 2:
        print("Registrarse")
    elif opcion_usuario == 3:
        print("Saliendo del programa...")
    else:
        print("Por favor, elige una opción válida.")
 
except ValueError:
    print("Por favor, ingresa un número válido.")