#Uma pista de Kart permite 5 voltas para cada um de 6 corredores. Faça um programa que os tempos (em
#segundos) de cada volta de cada corredor e guarde as informações em uma matriz. Ao final, o programa deve
#informar:
#a. De quem foi a melhor volta da prova, e em que volta
#b. Classificação final em ordem (1o. o campeão)


#Defino o número de corredores e voltas
corredores = 6
voltas = 5

#Inicio a matriz
matriz = [0] * corredores
for corredor in range(len(matriz)):
    matriz[corredor] = [0] * voltas
    print(matriz[corredor])

#Inicio o preenchimento da matriz
for corredor in range(len(matriz)):
    print(f"Corredor {corredor + 1}")
    for volta in range(len(matriz[corredor])):
        matriz[corredor][volta] = float(input(f"Digite o tempo que o corredor {corredor + 1} demorou na {volta + 1}º volta (EM SEGUNDOS): "))
# posso atribuir "matriz[corredor][volta]" a uma variável, para fins didáticos não utilizei isso, mas é interesante. 

#A melhor volta
melhorTempo = float('inf')  # Inicialize com um valor infinito para garantir que qualquer tempo na matriz seja menor do que o valor inicial
melhorCorredor = -1
melhorVolta = -1

for corredor in range(len(matriz)):
    for volta in range(len(matriz[corredor])):
        if matriz[corredor][volta] < melhorTempo:
            melhorTempo = matriz[corredor][volta]
            melhorCorredor = corredor
            melhorVolta = volta
    
print(f"A melhor volta foi do corredor {melhorCorredor + 1} na volta {melhorVolta + 1}, que atingiu o menor tempo possível, {melhorTempo} segundos.")

#Classificação final
classificacaoFinal = [] #novo array pra adicionar a nova lista ordenada 
for corredor in range(len(matriz)):
    tempo_total = sum(matriz[corredor]) #realiza o somatório total do tempo de volta de cada corredor
    classificacaoFinal.append((corredor + 1, tempo_total)) #adiciona o corredo mais o tempo total do mesmo no array classificacaoFinal

classificacaoFinal.sort(key=lambda x: x[1])  # Ordena com base no tempo total

print("Classificação final:")
for posicao, (corredor, tempo_total) in enumerate(classificacaoFinal):
    print(f"{posicao + 1}º lugar: Corredor {corredor} - Tempo Total: {tempo_total} segundos")


