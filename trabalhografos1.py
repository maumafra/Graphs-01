#Aluno: Maurício Mafra Monnerat

#Para definir o grafo, basta alterar a variável "graph" no final do programa.

def start(graph):
  if not validateGraph(graph):
    return print("Grafo inválido! Informe uma Matriz de Adjacência não nula e de tamanho N x N!")
  returnMsg = "Este grafo é "
  returnMsg += tipoDoGrafo(graph)
  print(returnMsg)

def validateGraph(graph):
  if not isinstance(graph, list) or len(graph) == 0:
    return False
  size = len(graph)
  for rowIdx in range(size):
    if not isinstance(graph[rowIdx], list) or len(graph[rowIdx]) != size:
      return False
  return True

def tipoDoGrafo(graph):
  graphType = ""
  isSymmetric = True
  isSimple = True
  isRegular = True
  isComplete = True
  isNull = True
  isBipartite = True

  #Conjunto de vértices para analisar se é bipartido, será colocado +1 no para um conjunto e -1 para o outro
  verticesSet = [0] * len(graph)

  rowsSum = [0] * len(graph)
  columnsSum = [0] * len(graph)
  for rowIdx in range(len(graph)):
    for columnIdx in range(len(graph[rowIdx])):
      rowsSum[rowIdx] += graph[rowIdx][columnIdx]
      columnsSum[columnIdx] += graph[rowIdx][columnIdx]
      isSymmetric = isSymmetric and checkSymmetry(graph[rowIdx][columnIdx], graph[columnIdx][rowIdx])
      isSimple = isSimple and not hasLoop(graph, rowIdx, columnIdx) and not hasParallelEdges(graph[rowIdx][columnIdx])
      isBipartite = isBipartite and checkBipartite(verticesSet, graph, rowIdx, columnIdx) and not hasLoop(graph, rowIdx, columnIdx)
  
  isRegular = checkRegularity(rowsSum, columnsSum, isSymmetric)
  isComplete = checkComplete(rowsSum, graph) and isSimple
  isNull = checkNull(rowsSum)
  
  if isSymmetric:
    graphType += "não-dirigido (provavelmente)"
  else:
    graphType += "dirigido"
  if isSimple:
    graphType += ", simples"
  else:
    graphType += ", multigrafo"
  if isRegular:
    graphType += ", regular"
  if isComplete:
    graphType += ", completo"
  if isNull:
    graphType += ", nulo"
  if isBipartite:
    graphType += ", bipartido"
  return graphType+"."

def checkSymmetry(element, oppositeElem):
  return element == oppositeElem

def hasLoop(graph, rowIdx, columnIdx):
  return rowIdx == columnIdx and graph[rowIdx][columnIdx] > 0

def hasParallelEdges(element):
  return element > 1

def checkRegularity(rowsSum, columnsSum, isSymmetric):
  firstRowSum = rowsSum[0]
  if isSymmetric:
    return all(firstRowSum == rowSum for rowSum in rowsSum)
  else:
    firstColumnSum = columnsSum[0]
    return all(firstRowSum == rowSum for rowSum in rowsSum) and all(firstColumnSum == columnSum for columnSum in columnsSum)
  
def checkComplete(rowsSum, graph):
  return all(len(graph) -1 == rowSum for rowSum in rowsSum) 

def checkNull(rowsSum):
  return sum(rowsSum) == 0

def checkBipartite(verticesSet, graph, rowIdx, columnIdx):
  if(graph[rowIdx][columnIdx] == 0):
    return True
  #Se o vértice da linha ainda não está em um conjunto
  if(verticesSet[rowIdx] == 0):
    #Se o vértice da coluna ainda não está em um conjunto
    if(verticesSet[columnIdx] == 0):
      #Coloca o vértice da linha no conjunto 1 e o vértice da coluna no conjunto -1
      verticesSet[rowIdx] = 1
      verticesSet[columnIdx] = -1
    #Se o vértice da coluna está em um conjunto
    else:
      #Coloca o vértice da linha no outro conjunto
      verticesSet[rowIdx] = verticesSet[columnIdx]*(-1)
  #Se o vértice da linha já está em um conjunto
  else:
    #Se o vértice da coluna ainda não está em um conjunto
    if(verticesSet[columnIdx] == 0):
      #Coloca o vértice da coluna no outro conjunto
      verticesSet[columnIdx] = verticesSet[rowIdx]*(-1)
    #Se os dois vértices já estão em algum conjunto
    else:
      #É bipartido caso a soma dos dois conjuntos for igual a zero ( (+1) + (-1) = 0 )
      return verticesSet[columnIdx] + verticesSet[rowIdx] == 0
  return True


#Defina o grafo aqui:
graph = [
    [0,1,1,1],
    [1,0,0,0],
    [1,0,0,1],
    [1,0,1,0]]

#Grafos de teste que eu usei:
directedGraph = [
    [0,0,1,1],
    [1,0,0,0],
    [0,0,0,1],
    [0,0,0,0]]
  
dircetedRegularGraph = [
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1],
    [1,0,0,0]]


invalidGraph1 = 0 #Teste para ver se cai resulta em grafo inválido
invalidGraph2 = [] #Teste para ver se cai resulta em grafo inválido
invalidGraph3 = [0] #Teste para ver se cai resulta em grafo inválido

graph4 = [[1]]

#Starta o prgrama
start(dircetedRegularGraph)
