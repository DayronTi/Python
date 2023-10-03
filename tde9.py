vetor_0 = [0, 10, 30, 5, 12]
vetor_1 = [15, 0, 10, 17, 28]
vetor_2 = [30, 10, 0, 3, 11]
vetor_3 = [5, 17, 3, 0, 80]
vetor_4 = [12, 28, 11, 80, 0]
matriz = [vetor_0, vetor_1, vetor_2, vetor_3, vetor_4]

for l in range(len(matriz)):
    for c in range(len(matriz[l])):
        print(matriz[l][c], end=" ")
    print("")


contador = 0
percurso = []
while True: 
    print("Informe as coordenadas que você deseja:  ")
    posLinha = int(input("Digite a linha da cidade de destino: "))
    posColuna = int(input("Digite a coluna da cidade de destino: "))

    posLinha -= 1
    posColuna -= 1

    distancia = matriz[posLinha][posColuna]
    print(f"A distância entre as cidades é {distancia}")
    print("...")
    
    percurso.append(distancia)
    contador += 1

    if contador >= 6:
        break
    
print(f"O percurso total é {sum(percurso)}")







