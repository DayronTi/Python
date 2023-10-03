import random

linhas = 3
colunas = 3

matriz = [0] * linhas
for l in range(len(matriz)):
    matriz[l] = [0] * colunas

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        matriz[l][c] = random.randint(1, 100)

for l in range(len(matriz)):
    print(matriz[l])
print(" ")

listaImpares = []
listaColunas = []
listaLinhas = []
somaColunas = 0
somaLinhas = 0
for l in range(len(matriz)):
    for c in range(len(matriz[l])):
      if matriz[l][c]%2 == 0:
        listaImpares.append(matriz[l][c])
        soma = sum(listaImpares)
        print(f'A soma de todos os elementos é: {soma}')
    
      if c == c:
        somaColunas += matriz[l][c]
        print(f'A soma de cada coluna é: {somaColunas}')

      if l == l:
        somaLinhas += matriz[l][c]
        print(f'A soma de cada linha é: {somaLinhas}')
