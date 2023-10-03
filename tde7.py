from typing import List

lista_1 = [8, 0, 7]
lista_2 = [4, 5, 6]
lista_3 = [3, 10, 2]

matriz = [lista_1,
          lista_2,
          lista_3]

lista_soma_linha = [None]*3
lista_soma_coluna = [None]*3

x= 0

soma_linha = 0
soma_coluna = 0
soma_diag_pr = 0
soma_col1= 0
soma_col2 = 0
soma_col3 = 0

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=" ")
        soma_linha = soma_linha + matriz[l][c]

        if l == c :
            soma_diag_pr = soma_diag_pr + matriz[l][c]
        
        if c == 0:
            soma_col1 = soma_col1 + matriz[l][c]
        elif c == 1:
            soma_col2 = soma_col2 + matriz[l][c]
        elif c == 2:
            soma_col3 = soma_col3 + matriz[l][c]
        else:
            print('mds')