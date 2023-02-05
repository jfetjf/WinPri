
# Este programa de Python crea los archivos de todas
# las posibles combinaciones que existen en una longitud
# dada. Por ejemplo en el archivo: Comb-49C2.csv se 
# guardan todas posibles combinaciones posibles 49C2
# de igual manera para 49C3, 49C4, 49C5 y 49C6 

from itertools import combinations
import csv
from csv import reader

mydict = {}
pares = {}
pareja = {}
list49 = []
arch1="Primitiva-1985a2012.csv"
arch2="Primitiva-2013a2022.csv"
pathfile = "./historicos/deWeb/"


# 1. Esta función lee las combinaciones históricas de dos archivos y los une para formar
# 2. una lista que contienes todas las combinaciones históricas, regresando esta lista
# 3. Lee los valores de la combinaciones de las copias de los archivos de la web
# 4. El formato a leer es CSV tal y como se dan en la Web. No se usa Headers.
def leerorigen():
    origen1 = pathfile + arch1
    origen2 = pathfile + arch2
    archivos =  [origen2, origen1]
    listafinal = []
    for file in archivos:
        with open(file, mode='r') as csv_file:
            csv_reader = reader(csv_file)
            for row in csv_reader:
                tmplist = []
                for num in range(1,7):
                    tmplist.append(row[num]) 
                listafinal.append(tmplist)
        csv_file.close()
    return listafinal


# 1. Esta función toma la lista que contiene todas las combinaciones históricas.
# 2. Luego las escribe en un archivo que se usará posteriormente
# 3. El archivo se llama allNoheader.csv
def writefinalfile():
    arch = "./historicos/todoSHeader.csv"
    data=leerorigen()
    with open(arch, 'w+', newline ='') as f:
        writer = csv.writer(f)
        writer.writerows(data)
    f.close()


# 1. Crea platillas para todas las compinaciones posibles: 49C2, 49C3, 49C4, 49C5 y 49C6
# 2. Guarda las combinaciones en los archivos con el mismo nombre: "Comb-49C6.csv"
# 3. Los archivos como son plantillas se crean solo una vez.
def iniciar():
    list49 = []
    for y in range(1,50):
        list49.append(y)
    for x in range(2,7):
        comb = combinations(list49, x)
        arch = "Comb-49C" + str(x) + ".csv"
        textfile = open(arch,"w")
        for element in comb:
            textfile.write(' '.join(str(s) for s in element) + '\n')
        textfile.close()



# 1. Lee todas las compinaciones historicas: 49C6 de allNoheader.csv
# 2. De c/u 49C6 extrae 6C2, 6C3, 6C4 y 6C5, los pone en un temp_dict: para contar cuantos hay
# 2. Guarda las combinaciones de c/u en los archivos con el mismo nombre: "cuantos-r-Hay.csv"
def quecuantos():
    tmp_list = leerorigen()
    for x in range(2,7):
        tmp_dict = {}
        for l in tmp_list:
            comblinea = combinations(l, x)
            for el in comblinea:
                if el in tmp_dict.keys():
                    tmp_dict.update({el:tmp_dict.get(el) + 1})
                else:
                    tmp_dict[el] = 1
            ar = "./Todoposible/cuantos-" + str(x) + "-Hay.csv"
            with open(ar,"w") as txtfl:
                for key, value in tmp_dict.items():
                    txtfl.write('%s:%s\n' % (key, value))
            txtfl.close()
        tmp_dict.clear()




# Initial Code - Here is where everything starts
# if __name__ == '__main__':
    # iniciar()
    # leerorigen()
    # writefinalfile()
    # quecuantos()
    # print("    That is all folks")