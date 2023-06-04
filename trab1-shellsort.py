#Importa bibliotecas
import math
import time
import timeit

# Em C / C++
# ./test < ENTRADA.TXT > SAIDA.TXT
# fopen("ENTRADA.TXT")

# Calcula o tempo EM MILISSEGUNDOS para a execução de uma função [func]
def executionTime(func):
    #guarda tempo de início da execução
    start_time = time.time_ns()
    start_time1 = timeit.default_timer()
   

    #executa função
    func

    #guarda tempo de fim da execução 
    end_time = time.time_ns()
    end_time1 = timeit.default_timer()
    
    #retorna a diferença entre tempo de início e fim (tempo total de execução da função)
    #obs.: converte para milissegundos (ms)
    return (end_time1-start_time1)* 1000.0
  
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
        numsStr.pop(0)     # tira o primeiro elemento

        for numero in numsStr:
            temp.append(int(numero))  

        entradas.append(temp)

        #fecha arquivo
        arq.close()

    #retorna um array com todos os arrays de entrada do arquivo
    return entradas

# Escreve resultado

def writeFile(arquivo, conteudo):

    with open(arquivo, 'a') as arq:
        linhas = arq.writelines(str(conteudo))
        arq.close()


## FUNCAO PARA REMOVER O PRIMEIRO ELEMENTO DO VETOR (LINHA) E CONFERIR SE CORRESPONDE AO TAMANHO CORRETO DO VETOR
def checkLength(arr):
  return arr.pop(0) == len(arr) # remove e confere se o primeiro elemento == a length


listaComTamanho = [5, 1, 2, 3, 4, 5]
checkLength(listaComTamanho)


# EXERCICIO 1 - SHELLSORT
### ---- SHELL GAPS ---- Função para calcular as divisões "h" para o Shell Sort
def shellGap(arr):
  #usa log2 para calcular quantas vezes precisa dividir a lista ao meio
  n = math.floor(math.log2(len(arr)))
  n -= 1 
  arr = []

  #calcula lista de potências de dois para usar no shell short
  while n >= 0:
    arr.append(2**n)
    n -= 1

  #retorna a lista que foi calculada
  return arr

### ---- KNUTH GAPS ---- Função para calcular as divisões "h" para o Knuth Sort
def knuthGap(arr):
  n = len(arr)
  arr = []
  i = 1
  gap = 1

  while gap < n:
    arr.insert(0,gap)
    i += 1
    gap = (3 ** i - 1) // 2
  
  return arr

### ---- CIURA GAPS ---- Função para calcular as divisões "h" para o Ciura Sort
def ciuraGap(arr):
  #print("tamanho lista: " + str(len(arr)))
  sequenciaCiura = [701, 301, 132, 57, 23, 10, 4, 1]
  n = len(arr)
  arr = []
  gap = 1
  
  if n > 701:
    arr = sequenciaCiura.copy()
    while n > arr[0]:
      #print(arr[0])
      gap = math.floor(arr[0] * 2.25)
      #print(gap)
      arr.insert(0, gap)

  else:
    for x in sequenciaCiura:
      if x < n:
        arr.append(x)

  
  return arr


### ---- GENERIC SORT ---- Função que usa as divisões calculadas para implementar um algoritmo "genérico" de Shell Sort
##

def genericShellSort(alist, gapsSequence, sequenceType): # FUNCAO GENERICA PARA ORDENAR

    #Inclui o parâmetro 'sequenceType' que aceita os valores 1, 2 e 3 pra gente poder passar qual tipo de sequência é para imprimir do lado do 'SEQ='
    sequencia = ''
    match sequenceType:
      case 1:
        sequencia = 'SHELL'
      case 2: 
        sequencia = 'KNUTH'
      case 3:
        sequencia = 'CIURA'
      case _:
        sequencia = '???'

    sublistcount = gapsSequence[0]

    print(*alist, "SEQ=" + str(sequencia))

    #Junta todo o alist e o 'SEQ=' em uma única string para passar para a função writeFile
    string_to_write = ' '.join(map(str, alist)) + " SEQ=" + str(sequencia) + '\n'
    writeFile('/Users/i576263/Desktop/CPD2023-1/saida1.txt', string_to_write)

    
    while len(gapsSequence) > 0:

      gapsSequence.pop(0)   # pops first element (que ele ja selecionou)

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      print(*alist, "INCR=", sublistcount)
      
      string_to_write = ' '.join(map(str, alist)) + " INCR=" + str(sublistcount) + '\n'
      writeFile('/Users/i576263/Desktop/CPD2023-1/saida1.txt', string_to_write)

      if len(gapsSequence) > 0:   # CONFERE NOVAMENTE SE NAO ESGOTOU O ARRAY DE GAPS
        sublistcount = gapsSequence[0]  # seleciona o que ficou em primeiro

def gapInsertionSort(alist,start,gap):  # CHAMA O INSERTION SORT 
    for i in range(start+gap,len(alist),gap):

        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position]=alist[position-gap]
            position = position-gap

        alist[position]=currentvalue

# FUNCAO MAIN

#Lê arquivos de entradas fornecidos:

#Lê arquivo "entrada1.txt"
listasExercicio1 = readFile('/Users/i576263/Desktop/CPD2023-1/entrada1.txt')

#Lê arquivo "entrada1.txt"
listasExercicio2 = readFile('/Users/i576263/Desktop/CPD2023-1/entrada2.txt')

# Lista de teste
listaTeste = [100000,26,93,17,77,31,44,55,20, 3]

listaTesteEnunciado = [16, 14, 12, 1, 8, 4, 9, 6, 15, 13, 11, 2, 7, 3, 10, 5]

# EXERCICIO 1
#Iteração entre listas lidas do arquivo 'entrada1.txt'

i = 1
for lista in listasExercicio1:
  print('\n ----------- LISTA NÚMERO ' + str(i) + ':')
  print(lista)
  i += 1
  print('\n\t### Shell gaps: ')
  print('\t' + str(shellGap(lista)))
  genericShellSort(lista.copy(), shellGap(lista), 1)
  print('\n\t### Knuth gaps: ')
  print('\t' + str(knuthGap(lista)))
  genericShellSort(lista.copy(), knuthGap(lista), 2)
  print('\n\t### Ciura gaps: ')
  print('\t' + str(ciuraGap(lista)))
  genericShellSort(lista.copy(), ciuraGap(lista), 3)



# EXERCICIO 2 - TESTES DE ESCALA
#ENTRADA 2
#SAIDA 2 = TEMPO EM MILISEGUNDOS 
#NOME DA SEQUENCIA, TAMANHO DO VETOR DE ENTRADA, TEMPO EM MILISEGUNDOS, DESCRICAO DO PROCESSADOR


  ### ---- GENERIC SORT 2 ---- Função que usa as divisões calculadas para implementar um algoritmo "genérico" de Shell Sort
##

def genericShellSort2(alist, gapsSequence, sequenceType): # FUNCAO GENERICA PARA ORDENAR

    #Inclui o parâmetro 'sequenceType' que aceita os valores 1, 2 e 3 pra gente poder passar qual tipo de sequência é para imprimir do lado do 'SEQ='
    sequencia = ''
    match sequenceType:
      case 1:
        sequencia = 'SHELL'
      case 2: 
        sequencia = 'KNUTH'
      case 3:
        sequencia = 'CIURA'
      case _:
        sequencia = '???'

    sublistcount = gapsSequence[0]

    #print(*alist, "SEQ=" + str(sequencia))

    #Junta todo o alist e o 'SEQ=' em uma única string para passar para a função writeFile
    #string_to_write = ' '.join(map(str, alist)) + " SEQ=" + str(sequencia) + '\n'
    #writeFile('/content/saida1.txt', string_to_write)

    
    while len(gapsSequence) > 0:

      gapsSequence.pop(0)   # pops first element (que ele ja selecionou)

      for startposition in range(sublistcount):
        gapInsertionSort(alist,startposition,sublistcount)

      #print(*alist, "INCR=", sublistcount)
      
      #string_to_write = ' '.join(map(str, alist)) + " INCR=" + str(sublistcount) + '\n'
      #writeFile('/content/saida1.txt', string_to_write)

      if len(gapsSequence) > 0:   # CONFERE NOVAMENTE SE NAO ESGOTOU O ARRAY DE GAPS
        sublistcount = gapsSequence[0]  # seleciona o que ficou em primeiro


# EXERCICIO 2
# Exemplo: 'SHELL,' + str(arr[0]) + ',' + str(executionTime(func)) +  'processador Intel i5'
for lista2 in listasExercicio2: 
  string_to_write = 'SHELL,' + str(len(lista2)) + ', ' + str(executionTime(genericShellSort2(lista2.copy(), shellGap(lista2), 1))) + ', INFORMACAO DO PROCESSADOR\n'
  writeFile('/Users/i576263/Desktop/CPD2023-1/saida2.txt', string_to_write)

  string_to_write = 'KNUTH,' + str(len(lista2)) + ', ' + str(executionTime(genericShellSort2(lista2.copy(), knuthGap(lista2), 2))) + ', INFORMACAO DO PROCESSADOR\n'
  writeFile('/Users/i576263/Desktop/CPD2023-1/saida2.txt', string_to_write)

  string_to_write = 'CIURA,' + str(len(lista2)) + ', ' + str(executionTime(genericShellSort2(lista2.copy(), ciuraGap(lista2), 3))) + ', INFORMACAO DO PROCESSADOR\n'
  writeFile('/Users/i576263/Desktop/CPD2023-1/saida2.txt', string_to_write)



