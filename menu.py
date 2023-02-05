import archivos





def option1():
    archivos.cargar()


def option2():
    archivos.cargar()


def mostrar_menu(opciones):
    print('      Seleccione una opción:\n')
    for clave in sorted(opciones):
        print(f' \t{clave}. {opciones[clave][0]}')


def leer_opcion(opciones):
    while (a := input('\n      Opción: ')) not in opciones:
        print('      Opción incorrecta, vuelva a intentarlo.\n\n')
    return a


def ejecutar_opcion(opcion, opciones):
    opciones[opcion][1]()


def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_opcion(opcion, opciones)
        print()




#  Creando las opciones   
while True:  
    print("\n       MAIN MENU")  
    print("       1. Load all new combinations so far.")  
    print("       2. Choose the base of combinations (2 or 3).")  
    print("       3. Exit")  
    choice = int(input("       Enter the Choice:"))  
  
    if choice == 1:
        option1()
    elif choice == 2:
        option2()  
    elif choice == 3:  
        break
    else:  
        print("       Oops! Incorrect Choice, try again") 





















def menu_principal():
    print(' \n')
    opciones = {
        '1': ('   Opción 1', accion1),
        '2': ('   Opción 2', accion2),
        '3': ('   Opción 3', accion3),
        '4': ('   Salir', salir)
    }

    generar_menu(opciones, '4')


def accion1():
    print('\n      Has elegido la opción 1\n\n')


def accion2():
    print('\n      Has elegido la opción 2\n\n')


def accion3():
    print('\n      Has elegido la opción 3\n\n')


def salir():
    print('\n      Saliendo ......\n')

if __name__ == '__main__':
    # Imprimiendo el encabezado inicial  
    print("       ***********************************************")  
    print("                WELCOME TO WIN 'LA PRIMITIVA'")  
    print("       ***********************************************")   
    print("")   
    menu_principal()