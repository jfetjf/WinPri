import archivos





def option1():
    archivos.writefinalfile()

def option2():
    archivos.iniciar()


#  Creando el menu y las opciones

def initial_menu():
    flag = True
    while flag:  
        print("\n        MAIN MENU")  
        print("       1. Load all new combinations so far.")  
        print("       2. Choose the base of combinations (2 or 3).")  
        print("       3. Exit")  
        choice = int(input("       Enter the Choice:"))  
    
        if choice == 1:
            option1()
        elif choice == 2:
            option2()  
        elif choice == 3:  
            flag = False
        else:  
            print("       Oops! Incorrect Choice, try again")


# Initial Code - Here is where everything starts
# if __name__ == '__main__':
    initial_menu()
    # leerorigen()
    # writefinalfile()
    # quecuantos()
    print("    That is all folks!!")


















def menu_principal():
    print(' \n')
    opciones = {
        '1': ('   Opción 1', accion1),
        '2': ('   Opción 2', accion2),
        '3': ('   Opción 3', accion3),
        '4': ('   Salir', salir)
    }


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
    print("       That is all folks")
