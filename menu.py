import archivos



def option1():
    archivos.iniciar()


def option2():
    archivos.writefinalfile()


def option3():
    archivos.quecuantos()


def option4():
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
        print("       1. Create all possible Combinations 49C2, 49C3, 49C4,")
        print("          49C5 and 49C6. We do this just once. Save in files.")
        print("       2. Update all Drawings so far. Result saved to files.")    
        print("       3. Count all 2, 3, 4, 5 and 6s drawings so far.") 
        print("          We update this after each Drawing. Save in files.") 
        print("       4. Choose the base of combinations (2 or 3).") 
        print("       5. Exit") 
        print("")
        choice = int(input("          Enter the Choice: "))  
    
        if choice == 1:
            option1()
        elif choice == 2:
            option2()
        if choice == 3:
            option1()
        elif choice == 4:
            option2()   
        elif choice == 5:  
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
    
