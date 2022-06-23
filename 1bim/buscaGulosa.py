import time

origem = 0
destino = 12

arvore1 =  {
	0 : [(1,1),(2,3)],
	1 : [(3,0),(4,2)],
	2 : [(5,4),(6,4)],
	3 : [],
	4 : [],
	5 : [],
	6 : []
}

arvore2 =  {
	0 : [(1,4),(2,3)],
	1 : [(3,5),(4,5)],
	2 : [(5,1),(6,2)],
	3 : [(7,6), (8,6)],
	4 : [(9,6), (10,6)],
	5 : [(11,2), (12,1)],
	6 : [(13,4), (14,4)],
	7 : [],
	8 : [],
	9 : [],
	10 : [],
	11 : [],
	12 : [],
	13 : [],
	14 : []
}

arvore3 =  {
	0 : [(1,4),(2,3)],
	1 : [(3,5),(4,5)],
	2 : [(5,1),(6,2)],
	3 : [(7,6), (8,6)],
	4 : [(9,6), (10,6)],
	5 : [(11,2), (12,0)],
	6 : [(13,4), (14,4)],
	7 : [(15,7), (16,7)],
	8 : [(17,7), (18,7)],
	9 : [(19,7), (20,7)],
	10 : [(21,7), (22,7)],
	11 : [(23,3), (24,3)],
	12 : [(25,1), (26,1)],
	13 : [(27,5), (28,5)],
	14 : [(29,5), (30,5)],
	15 : [],
	16 : [],
	17 : [],
	18 : [],
	19 : [],
	20 : [],
	21 : [],
	22 : [],
	23 : [],
	24 : [],
	25 : [],
	26 : [],
	27 : [],
	28 : [],
	29 : [],
	30 : []
}





def buscaGulosa(graph, node, search):
	nodoAtual = node
	caminho = []
	caminho.append(nodoAtual)
	distancia = 0
	while len(set([nodoVizinho for (nodoVizinho, distance) in graph.get(nodoAtual, [])]).difference(set(caminho))) > 0:
		vizinhoProximo = None
		menorDistancia = None
		for vizinho, vizinhoDistancia in graph[nodoAtual]:
			if vizinho != nodoAtual and vizinho not in caminho:
				if menorDistancia is not None:
					if menorDistancia > vizinhoDistancia:
						menorDistancia = vizinhoDistancia
						vizinhoProximo = vizinho
				else:
					menorDistancia = vizinhoDistancia
					vizinhoProximo = vizinho
		vizinhoMaisProximo = (vizinhoProximo, menorDistancia)
		nodoAtual = vizinhoMaisProximo[0]
		caminho.append(nodoAtual)
		distancia += vizinhoMaisProximo[1]
		if nodoAtual == search:
			fim = time.time()
			print("Caminho percorrido: %s" %caminho)
			print("Distância percorrida: %d" %distancia)
			print("Tempo de execução %fs" %(fim - inicio))
			return 0

inicio = time.time()
buscaGulosa(arvore3, origem, destino)