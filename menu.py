import archivos



def option1():
    archivos.writefinalfile()


def option2():
    archivos.iniciar()


def salir():
    print('\n')
    print("          Saliendo ......")
    print("")
    print("          That is all folks!\n\n")


#  Creando el menu y las opciones

def initial_menu():
    flag = True
    while flag:  
        print("\n") 
        print("          MAIN MENU")
        print("")
        print("       1. Load all new combinations so far.")  
        print("       2. Choose the base of combinations (2 or 3).") 
        print("       3. Exit") 
        print("")
        choice = int(input("          Enter the Choice: "))  
    
        if choice == 1:
            option1()
        elif choice == 2:
            option2()  
        elif choice == 3:  
            flag = False
            salir()
        else:  
            print("       Oops! Incorrect Choice, try again")


# Initial Code - Here is where everything starts
if __name__ == '__main__':
    # Imprimiendo el encabezado inicial 
    print("\n\n")
    print("       ***********************************************")  
    print("                WELCOME TO WIN 'LA PRIMITIVA'")  
    print("       ***********************************************")   
    print("")   
    initial_menu()
    
