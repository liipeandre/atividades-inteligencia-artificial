def tabu_search(espaco_busca):
	# escolher uma solução inicial (que será a atual), existente no espaço de busca, dada uma regra definida.
	solucao_atual = solucao_inicial(espaco_busca)
	
	# define uma lista tabu vazia.
	lista_tabu = []
	
	# enquanto não atingo a condição de parada.
	while not condicao_parada(solucao_atual):
	
		# seleciona os vizinhos melhores que a solucao_atual.
		for vizinho in solucao_atual.vizinhanca:
			if vizinho.valor > solucao_atual.valor:
				lista_tabu.append(vizinho)
				
		# ordena pelo valor da solução e escolhe a melhor solução das encontradas.
		lista_tabu.sort(lambda x: x.valor)
		solucao_atual = lista_tabu[0]
		
	return solucao_atual
	
	
	
	
	
	
