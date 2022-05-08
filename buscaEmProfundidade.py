import time

origem = '0'
destino = '3'

dist = 0
testado = set()

def buscaEmProfundidade(testado, graph, node, search):
	global dist
	if node not in testado:
		print (node)
		testado.add(node)
		dist+=1

		if node == search:
			print('Destino Encontrado')
			fim = time.time()
			print('Distância percorrida: %d' %dist)
			print("Tempo de execução: %fs" % (fim - inicio))
		for vizinho in graph[node]:
			buscaEmProfundidade(testado, graph, vizinho, search)

arvore1 =  {
	'0' : ['1','2'],
	'1' : ['3', '4'],
	'2' : ['5', '6'],
	'3' : [],
	'4' : [],
	'5' : [],
	'6' : []
}

arvore2 =  {
	'0' : ['1','2'],
	'1' : ['3', '4'],
	'2' : ['5', '6'],
	'3' : ['7', '8'],
	'4' : ['9', '10'],
	'5' : ['11', '12'],
	'6' : ['13', '14'],
	'7' : [],
	'8' : [],
	'9' : [],
	'10' : [],
	'11' : [],
	'12' : [],
	'13' : [],
	'14' : []
}

arvore3 =  {
	'0' : ['1','2'],
	'1' : ['3', '4'],
	'2' : ['5', '6'],
	'3' : ['7', '8'],
	'4' : ['9', '10'],
	'5' : ['11', '12'],
	'6' : ['13', '14'],
	'7' : ['15', '16'],
	'8' : ['17', '18'],
	'9' : ['19', '20'],
	'10' : ['21', '22'],
	'11' : ['23', '24'],
	'12' : ['25', '26'],
	'13' : ['27', '28'],
	'14' : ['29', '30'],
	'15' : [],
	'16' : [],
	'17' : [],
	'18' : [],
	'19' : [],
	'20' : [],
	'21' : [],
	'22' : [],
	'23' : [],
	'24' : [],
	'25' : [],
	'26' : [],
	'27' : [],
	'28' : [],
	'29' : [],
	'30' : []
}

inicio = time.time()
buscaEmProfundidade(testado, arvore1, origem, destino)

