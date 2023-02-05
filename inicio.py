
# Programa de Python program
# 1. Lee todas combinaciones historicas de un archivo, una combinacion un linea
# 2. De cada linea se obtiene 6C2 = 15 combs 
# 3. Se almacenan las combs de 2. en mydic{} sin repeticion para saber que cuanto ha caido
# 4. Creamos un umbral para escoger 80% del centro de todas las combs
# 5. combinations of given length

from itertools import combinations
import csv
from operator import delitem
import random
import re
import string
from tkinter.filedialog import SaveFileDialog


inicial49 = {}  # Dict de todos los 49 número iniciados a 1. {'03': 1}
cur_tuplas = {}  # Dict de tuplas (2, 3, 4, 5 o 6) extraidas de list6win con las veces que han caido. ('02','21','45'): 6
tuplasneeded = {} # Dict con las tuplas necesarias para jugar por ejemplo una ('04', '20', '45'):5
cuantos_cada_uno = {} # Dict con los 49 escogidos y cuantas veces aparece en las tuplas
dict49 = {} # Dict clave:valor donde la clave es un # del 1 al 49 y el valor las veces que aparece en mywins[]
list6win = [] # Lista de las combinaciones historicas ganadoras, tuplas de 6 de todos los años.
izvrani = [] # Lista de las combinaciones creadas para jugar
mywins = [] # Lista de las combinaciones que se van a jugar, tuplas de 6 #s.
arr25 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y']
arr17 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q']
file17C2 = "combLetras-17C2.csv"
file25C3 = "combLetras-25C3.csv"
rr =  3



#   Regresa el número que falta para completar los 49 en total
def reiniciar():
    inicial49.clear()
    cuantos_cada_uno.clear()
    dict49.clear()
    list6win.clear()
    izvrani.clear()
    mywins.clear()



#   Este metodo llena el dict inicial49
#   Convierte los 49 en cadenas. En caso de ser menor que 10, agrega un cero de prefijo '07'
#   Regresa el número que falta para completar los 49 en total
def iniciar49():
    tmp_tuple = []
    for tpl in tuplasneeded.keys():
        for un in tpl:
             tmp_tuple.append(un)
    for x in range(1,50):
        if x < 10:
            num = '0' + str(x)
        else:
            num = str(x)
        inicial49[num] = 1
    for x1 in inicial49.keys():
        flag = True
        for x2 in tmp_tuple:
            if x1 == x2:
                flag = False
                break
        if flag:
            print("\n     El número a agregar es: " + x1)
            return x1


#   Este metodo busca en todas las combinaciones encontradas si hay alguna que tenga algun numero 2 veces.
#   Convierte los 49 en cadenas. En caso de ser menor que 10, agrega un cero de prefijo '07'
#   Regresa el número que falta para completar los 49 en total
def doblesfuera():
    contar_cada_uno(izvrani)
    a_ver = izvrani[:]
    for v in range(0, len(a_ver)):
        res = list(set(a_ver[v]))
        while len(res) != 6:
            nn = int(random.randint(1, 49))
            new_num = '0' + str(nn) if nn < 10 else str(nn)
            res.append(new_num) 
            res.sort()    
            print("\n     Hay una tupla con números dobles " )
            if len(res) == 6:
                izvrani[v] = res


#   Contamos los 49 en cada tupla para saber cuantas veces aparece
def contar_cada_uno(escogidas):
    for tpl in escogidas:
        for t in tpl:
            if t in cuantos_cada_uno:
                cuantos_cada_uno[t] += 1
            else:
                cuantos_cada_uno[t] = 1



#   Primero lee todos las combinaciones historicas de todoSHeader.csv y las carga en list2win
#   Llena el dict cur_tuplas con rr, si rr = 3 (07, 11, 25):9 de todas las existentes
def leerviejos():
    counter = 1
    with open('./historicos/todoSHeader.csv', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            list6win.append(row)
            comblinea = combinations(row, rr)
            for el in comblinea:
                if el in cur_tuplas.keys():
                    cur_tuplas.update({el:cur_tuplas.get(el) + 1})
                else:
                    cur_tuplas[el] = 1
            counter = counter + 1
    file.close()



#   Primero carga list6win y cur_tuplas con el primer metodo
#   Extrae las tuplas necesarias con numeros no repetidos para llegar a 49 numeros
#   Llena las cur_tuplas dict con las tuplas actuales ya sean 2, 3, 4, 5
def iniciar():
    leerviejos() #   Carga list6win y cur_tuplas con el primer metodo
    # contar = 1
    #while contar < 11:
    extuplas()   # crea las tuplas sin repeticion hasta < 49 numeros
    llenar49()       # completa el numero de tuplas para abarcar todos los 49 numeros
    molde = creamolde()  # crea todas las tuplas posibles dependiendo de cuantoas son 17C3 = 136
    llenamolde(molde)  # crea todas las tuplas con numeros basados en el molde anterior
    probarlists()  # verifica que no hayan tuplas que han caido anteriormente de rango 6
    quitartuplas()  # quita aquellas tuplas que han caido anteriormente
    # reiniciar()



# 1.  Toma un dict con todas las tuplas de cuantos veces ha caido c/u de ellos.
# 2.  Extrae las tuplas necesarias con numeros no repetidos para llegar a 49 numeros
# 3.  Llena el dict de tuplas basado en el numero no repetidos para forma 24 x 2 = 4. 
# 4.  Si es 3: 16 x 3 = 48.
def extuplas():
    mayor = max(cur_tuplas.values())
    menor = min(cur_tuplas.values())
    top = mayor - (mayor - menor)*0.1
    inf = menor + (mayor - menor)*0.1
    l = list(cur_tuplas.items())
    random.shuffle(l)
    random.shuffle(l)
    a_d = dict(l)
    for key, value in a_d.items():
        if value  < top and value > inf:
            if ver(key):
                tuplasneeded[key] = value
    print("     Al llenar las tuplas necesarias, la longitud es: " + str(len(tuplasneeded)))
    print("     Números escogidos hasta ahora: " + str(len(tuplasneeded)*rr))
    print("     Las triadas escogidas son: " + str(tuplasneeded))


# 1. Crea un dict temporal del tipo '#' = 1 donde # es un numero entre 1 y 49.
# 2. Verifica que numero falta de todas las tuplas = 48 para completar los 49.
# 3. Busca un par ('#', num) numero que falta con otro y lo agrega al dict de tuplasneeded.
def llenar49():
    ss = iniciar49()
    for ky, value in cur_tuplas.items():
        for un in ky:
            if ss == un:
                tuplasneeded[ky] = value
                print("     La última triada escogida es: " + str(ky) + ": " + str(value))
                return ss



# 1. Toma las claves de un dictorinario y luego verifica si ambos valores ya estan en la list 49
# 2. Si ninguno de los valores de la clave estan en la lista 49 los agregar.
# 3. Crea las tuplas diferentes de los numeros del 1 hasta el 49. Un numero queda fuera.
def ver(k):
    band = True
    for x in k:
        if x in dict49.keys():
            band = False
            return band
    if band:
        for y in k:
            dict49[y] = 1
    return band



# 1. Crea un dict temporal del tipo 'A' = (#, #) donde # es un numero entre 1 y 49.
# 2. Pasa las claves que son los 25 pares numeros como valor al nuevo dict creado.
# 3. Se crea el dict 'A' : ('#', '#') que se usara en la plantilla de creacion 2300.
def creamolde():
    t_d =  {}
    x = 0
    for ky in tuplasneeded:
        t_d[arr17[x]] = ky
        x = x + 1
    return t_d
           

# 1. Lee la plantilla de 2300 triadas de 25C3 [A', 'B', 'C'] desde un archivo.
# 2. Une los pares A, B y C para formar una combinacón de 6 numeros que forma un lista.
# 3. Llena la lista izvrani que contiene [[#, #, #, #, #, #], [C2],[C3] ...] lo que se va a jugar
# 4. Guarda las combinaciones de 6 numeros en un dict (A, B C): [#, #, #, #, #, #].
def llenamolde(molde):
    dic_letras_tupla = {}
    with open('./plantillas/' + file17C2, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            tmp = molde[row[0]] + molde[row[1]] # + molde[row[2]]
            t = sorted(tmp)
            izvrani.append(t)
            dic_letras_tupla[tuple(row)] = t
    f.close()
    doblesfuera()
    print("     La longitud del número de las escogidas es: " + str(len(izvrani)))



# 1. Se crean dos lista de listas de numeros ol1 y ol2 (las que han caido historicas = 3526).
# 2. Compara las dos lista para sacar las unicas de las izvrani y ponerlas en la lista mywins
def probarlists():
    for l1 in list6win:
        l1.sort()
        for l2 in izvrani:
            l2.sort()
            if(l1==l2):
               print("     Hay alguna tupla que ya ha caido!!")
    print("     La longitud de izvrani es: " + str(len(izvrani)))
    salida(izvrani) # Vamos a imprimir las combinaciones izvrani




# 1. Abre un archivo de las combis caidas ya sean 2, 3, 4, y 5 y cuantas veces han caido
# 2. Devuelve un set cargado con los todos los elementos leidos del archivo.
def abrefile(t_s):
    listcaidos = []
    with open('./Todoposible/cuantos-' + str(t_s)+ '-Hay.csv', 'r') as arch:
        reader = csv.reader(arch, delimiter=':')
        for row in reader:
            new_str = ''.join(row[0])
            res = re.sub("['(,)]","",new_str)
            listcaidos.append(res)
    arch.close()
    return set(listcaidos)


# 1. Abre un archivo de las combis caidas ya sean 2, 3, 4, y 5 y los cuantas veces han caido.
# 2. Compara las tuplas con las escogidas para quitar aquellas que ya han caido.
# 3. Obtiene una lista con tuplas que no han caido.
def quitartuplas():
    listcaidos = []
    listimprimir = []
    for x in range(5,1,-1):
        setcaidos = abrefile(x)
        for el in mywins:
            flag = True
            comblinea = combinations(el, x)
            for un in comblinea:
                uno = sorted(un)
                uno = tuple(uno)
                if uno in setcaidos:
                    flag = False
                    break
            if flag:
                listimprimir.append(el)
    t_l = listostring(listimprimir)
    print("\n\n     Longitud de la lista antes de limpiar: " + str(len(t_l)))
    at_l = list(dict.fromkeys(t_l))
    print("\n     Longitud de la lista despues de limpiar: " + str(len(at_l)))
    print("\n\n     Ya fuera")
    print("\n\n")


def listostring(a_l):
    ot_l = []
    for item in a_l:
        num = ''
        for un in item:
            ot_s = ' '
            if un < 10:
                ot_s = '0' + str(un)
            else:
                ot_s = str(un)
            num += ' ' + ot_s
        ot_l.append(num.strip())
    return ot_l


# 1. Este metodo imprime las combinaciones para jugar.
# 2. Primero imprime los bloques de los 5x8 y luego el restante 
def salida(a_l):
    random.shuffle(a_l)
    random.shuffle(a_l)
    vueltas = len(a_l)//40
    cols = 0
    n_fila = 1
    grupos = 0
    print('\n\n')
    for n in range(0, len(a_l)):
        if cols < 5:
            res = re.sub("[^a-zA-Z0-9 ]","",str(a_l[n]))
            print(str(n_fila) + ":  " + res, end="     ")
            cols = cols + 1
        if cols == 5:
            cols = 0
            n_fila = n_fila + 1
            print('')
        if n_fila == 9 and grupos < vueltas:
            cols = 0
            n_fila = 1
            grupos = grupos + 1
            print('\n')
        if grupos == vueltas:
            break
    ot_cols = (len(a_l) - 40*vueltas)//8
    inicio = len(a_l) - (len(a_l) - 40*vueltas)
    for m in range(inicio, len(a_l)):
        if cols < ot_cols:
            res = re.sub("[^a-zA-Z0-9 ]","",str(a_l[m]))
            print(str(n_fila) + ":  " + res, end="     ")
            cols = cols + 1
        if cols == ot_cols:
            cols = 0
            n_fila = n_fila + 1
            print('')
    print('\n\n')
        


if __name__ == '__main__':
    #iniciar49()
    iniciar()
    