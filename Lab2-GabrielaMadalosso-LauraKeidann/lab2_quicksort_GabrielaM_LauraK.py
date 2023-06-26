# -*- coding: utf-8 -*-

# LABORATORIO 2 - QUICKSORT
# ALUNAS:
# GABRIELA MADALOSSO
# LAURA KEIDANN RODRIGUES DA SILVA


#Importa bibliotecas
import math
import time
import timeit   #para usar no mac
import random # para gerar valor aleatorio
import statistics # para calcular a mediana

#1. Escolha 1 (Mediana de 3): Particionador deve ser a mediana entre o primeiro, ultimo e elemento na posicao
# media de cada sub-vetor (media entre o ındice do primeiro e ultimo elemento, arrendodada para baixo); ´
# 2. Escolha 2 (Aleatorio): Particionador sera um elemento aleatorio do sub-vetor

# 1) definir qual sera o particionador
# 2) colocar o particicionador na primeira posicao do sub-vetor, trocando com o elemento atualmente na primeira posicao.
# 3) implementar o algoritmo de Quicksort usando o primeiro elemento como particionador.

# Duas estrategias de particionamento sao implementadas:
# 1. Particionamento 1 (Lomuto)
# 2. Particionamento 2 (Hoare)

# Para todas as quatro combinacoes (escolha x particionamento), testamos cada uma das versoes do algoritmo com o
# arquivo entrada-quicksort.txt, contendo vetores aleatorios de tamanho 100, 1000, 10000, 100000 e 1000000.
# O programa deve le os vetores de um arquivo da entrada padrao, e gravaa resultados na saida padrao
# A entrada padrao eh redirecionada para o arquivo  entrada-quicksort.txt, contendo varios vetores a serem ordenados.
# Cada vetor eh descrito em 1 linha.
# O primeiro numero da linha descreve o tamanho n do vetor, seguido por n numeros do vetor.

# Leitura de arquivo txt

def readFile(arquivo):
    linhas, entradas, numsComQtd = [], [], []

    #abre arquivo
    with open(arquivo, 'r') as arq:
        #lê linhas do arquivo
        linhas = arq.readlines()

    for linha in linhas:
        temp = []
        numsStr = linha.split()
        numsStr.pop(0)

        for numero in numsStr:
            temp.append(int(numero))

        entradas.append(temp)

        #fecha arquivo
        arq.close()

    #retorna um array com todos os arrays de entrada do arquivo
    return entradas

# Escreve resultado no arquivo

def writeFile(arquivo, conteudo):

    with open(arquivo, 'a') as arq:
        linhas = arq.writelines(str(conteudo))
        arq.close()

# ESCOLHA 1 - MEDIANA DE 3

# FUNCAO PARA CALCULAR A MEDIANA ENTRE 3 ELEMENTOS (PRIMEIRO, MEIO E ULTIMO)
def medianaDe3(lista):

    indice = 0
    tamanho = len(lista)

    # Pega o primeiro e o ultimo elemento
    primeiro = lista[0]
    ultimo = lista[-1]

    # Seleciona o elemento do meio
    indiceMeio = math.floor(tamanho/2)
    meio = lista[indiceMeio]

    # Calcula a mediana dos 3 elementos selecionados
    mediana = statistics.median([primeiro, meio, ultimo]);

    # Retorna a posicao do elemento mediano
    if mediana == primeiro:
        indice = 0

    elif mediana == meio:
        indice = indiceMeio

    else:
        indice = tamanho - 1

    # retorna o indice da mediana
    return int(indice)

# ESCOLHA 2 - ELEMENTO ALEATORIO

# funcao para selecionar um elemento aleatorio da lista
def aleatorio(lista):
    from random import randrange
    indice = randrange(len(lista))
    # retorna o indice do elemento aleatorio
    return (indice)

# PARTICIONAMENTO 1
# PARTICIONAMENTO LOMUTO

def particionamentoLomuto(lista, esq, dir):

    global numSwaps

    pivo = lista[esq]
    indice = esq + 1 #indice do menor

    i = esq + 1
    while (i <= dir):
        # se o elemento atual for menor ou igual ao pivo
        if lista[i] < pivo:
            # troca de posicao
            lista[i], lista[indice] = lista[indice], lista[i] # swap
            indice+=1 # incrementa o indice do menor elemento
            numSwaps += 1

        i+=1

    # troca de posicao
    lista[esq], lista[indice-1] = lista[indice-1], lista[esq]

    return (indice-1)

# PARTICIONAMENTO 2
# PARTICIONAMENTO HOARE

def particionamentoHoare(lista, esq, dir):

    global numSwaps

    pivo = lista[esq] # recebe o primeiro elemento
    i, j = esq, dir # i = esq e j = dir

    while (i<j):
      # vai da direita para a esquerda
      while(lista[j] > pivo and i < j):
        j-=1 # decrementa j
      lista[i] = lista[j]; #troca
      numSwaps += 1

      # vai da esquerda para a direita
      while(lista[i] <= pivo and i < j):
        i+=1 #incrementa i
      lista[j] = lista[i]; #troca
      numSwaps += 1

    lista[j] = pivo
    return i;

# FUNCAO DO QUICKSORT

def quicksort(lista, esq, dir, partitionType):

    global numRecursoes

    # incrementa a cada chamada
    numRecursoes += 1

    if(dir > esq):
        if partitionType == 'LOMUTO':
            indicePivo = particionamentoLomuto(lista, esq, dir)
            # divide a lista no pivo e chama a funcao para a parte da esquerda e da direita
            quicksort(lista, esq, indicePivo-1, 'LOMUTO')
            quicksort(lista, indicePivo+1, dir, 'LOMUTO')


        elif partitionType == 'HOARE':
            indicePivo = particionamentoHoare(lista, esq, dir)
            quicksort(lista, esq, indicePivo-1, 'HOARE')
            quicksort(lista, indicePivo+1, dir, 'HOARE')

# TIPO DE PIVO

def definePivo(lista, tipoPivo):

    if tipoPivo == 'mediana':
        indicePivo = medianaDe3(lista)

    elif tipoPivo == 'aleatorio':
        indicePivo = aleatorio(lista)

    # faz o swap
    lista[0], lista[indicePivo] = lista[indicePivo], lista[0]

#------------ FUNCAO MAIN --------------

# UMA CHAMADA DE FUNCAO PARA CADA TESTE

# strings para o resultado
tam = 'TAMANHO ENTRADA ';
swaps = 'SWAPS ';
recs = 'RECURSOES ';
time = 'TEMPO ';

# PERCORRE CADA UMA DAS LISTAS E CHAMA O TIPO DE QUICKSORT CORRETO

# LOMUTO ALEATORIO

entrada = readFile('/content/entrada-quicksort.txt')
lomutoPivoAleatorio = []
lomutoPivoAleatorio = entrada.copy()

for lista in lomutoPivoAleatorio:

    # Define pivo
    definePivo(lista, 'aleatorio')

    # Zera os contadores
    numRecursoes = 0
    numSwaps = 0
    tempoFunc = 0

    # Inicia a contagem de tempo
    start_time = timeit.default_timer()

    # Chama a quicksort
    quicksort(lista, 0, (len(lista)-1), 'LOMUTO')

    # Encerra a contagem de tempo
    end_time  = timeit.default_timer()

    # Calcula o tempo transcorrido e converte para milissegundos
    result_time  = (end_time - start_time)*1000.00 # para ser miliseconds

    # Concatena os resultados numa string
    resultado = tam + str(len(lista)) + "\n" + swaps + str(numSwaps) + "\n" + recs + str(numRecursoes) + "\n" + time + str(result_time ) + "\n"

    # Escreve no arquivo de saida
    writeFile("/content/stats-aleatorio-lomuto.txt", resultado)

# LOMUTO COM A MEDIANA

entrada = readFile('/content/entrada-quicksort.txt')
lomutoMediana = []
lomutoMediana = entrada.copy()

for lista in lomutoMediana:

    # Define pivo
    definePivo(lista, 'mediana')

    # Zera os contadores
    numRecursos = 0
    numSwaps = 0
    tempoFunc = 0

    # Inicia a contagem de tempo
    start_time = timeit.default_timer()

    # Chama a quicksort
    quicksort(lista, 0, (len(lista)-1), 'LOMUTO')

    # Encerra a contagem de tempo
    end_time  = timeit.default_timer()

    # Calcula o tempo transcorrido e converte para milissegundos
    result_time  = (end_time - start_time)*1000.00

    # Concatena os resultados numa string
    resultado = tam + str(len(lista)) + "\n" + swaps + str(numSwaps) + "\n" + recs + str(numRecursoes) + "\n" + time + str(result_time ) + "\n"

    # Escreve no arquivo de saida
    writeFile("/content/stats-mediana-lomuto.txt", resultado)

# HOARE ALEATORIO


entrada = readFile('/content/entrada-quicksort.txt')
hoareAleatorio = []
hoareAleatorio = entrada.copy()


for lista in hoareAleatorio:

    # Define pivo
    definePivo(lista, 'aleatorio')

    # Zera os contadores
    numRecursoes = 0
    numSwaps = 0
    tempoFunc = 0

    # Inicia a contagem de tempo
    start_time = timeit.default_timer()

    # Chama a quicksort
    quicksort(lista, 0, (len(lista)-1), 'HOARE')

    # Encerra a contagem de tempo
    end_time  = timeit.default_timer()

    # Calcula o tempo transcorrido e converte para milissegundos
    result_time  = (end_time - start_time)*1000.00

    # Concatena os resultados numa string
    resultado = tam + str(len(lista)) + "\n" + swaps + str(numSwaps) + "\n" + recs + str(numRecursoes) + "\n" + time + str(result_time ) + "\n"

    # Escreve no arquivo de saida
    writeFile("/content/stats-aleatorio-hoare.txt", resultado)

# HOARE MEDIANA


entrada = readFile('/content/entrada-quicksort.txt')
hoareMediana = []
hoareMediana = entrada.copy()

for lista in hoareMediana:

    # Define pivo
    definePivo(lista, 'mediana')

    # Zera os contadores
    numRecursoes = 0
    numSwaps = 0
    tempoFunc = 0

    # Inicia a contagem de tempo
    start_time = timeit.default_timer()

    # Chama a quicksort
    quicksort(lista, 0, (len(lista)-1), 'HOARE')

    # Encerra a contagem de tempo
    end_time  = timeit.default_timer()

    # Calcula o tempo transcorrido e converte para milissegundos
    result_time  = (end_time - start_time)*1000.00

    # Concatena os resultados numa string
    resultado = tam + str(len(lista)) + "\n" + swaps + str(numSwaps) + "\n" + recs + str(numRecursoes) + "\n" + time + str(result_time ) + "\n"

    # Escreve no arquivo de saida
    writeFile("/content/stats-mediana-hoare.txt", resultado)
