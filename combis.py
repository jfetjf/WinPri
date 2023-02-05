# Programa que imprime todas las combinaciones de
# tamaño r de un arreglo con tamaño n


# La funcion principal imprime todas combinaciones 
# de tamaño r en el arreglo arr[] de tamaño n. Esta
# funcion usa combinationUtil()
def printCombination(arr, n, r, f):
     
    # Un arreglo temporal para guardar todas la combinaciones
    # una por una
    data = [0]*r;
 
    # Imprimimos todas las combinaciones, usando el arreglo 
    # temporal 'data[]'
    combinationUtil(arr, data, 0,
                    n - 1, 0, r, f);
 
# arr[]       ---> Arreglo de entrada
# data[]      ---> Arreglo temporal para guardar la combinacion actual
# start & end ---> Comenzando y terminando los indexes en arr[]
# index       ---> Index actual en data[]
# r           ---> Tamaño de la combinacion que se imprime
def combinationUtil(arr, data, start,
                    end, index, r, f):
    # Combinacion actual lista para imprimir y se imprime
    if (index == r):
        for j in range(r):
            print(data[j], end = " ");
        print();
        f.write(str(data) + "\n")
        return;
 
    # Reemplazar el index con todos los posibles elementos. La condicion
    # "end-i+1 >= r-index" hace posible que incluyendo un elemento en el 
    # index hara que la combinacion con elementos restantes esten en las
    # posiciones restantes
    i = start;
    while(i <= end and end - i + 1 >= r - index):
        data[index] = arr[i];
        combinationUtil(arr, data, i + 1,
                end, index + 1, r, f);
        i += 1;


# Codigo inicial
arr25 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y'];
arr17 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q'];
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 10, 21, 22, 23, 24, 25];
r = 2;
n = len(arr17);
with open('./plantillas/combLetras-17C' + str(r) + '.txt', 'w') as f:
    printCombination(arr17, n, r, f);
f.close()

