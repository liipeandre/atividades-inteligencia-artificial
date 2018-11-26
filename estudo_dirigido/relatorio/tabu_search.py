from os import system
from estudo_dirigido.codigo.problema_mochila import *
from estudo_dirigido.codigo.controle_parada import *

def tabu_search():
    # escolher uma solução inicial (que será a atual), existente no espaço de busca, dada uma regra definida.
    solucao_atual = solucao_inicial()

    # define uma lista tabu vazia.
    lista_tabu = []

    # enquanto não atingo a condição de parada.
    while not condicao_parada_tabu(solucao_atual):

        # seleciona os vizinhos melhores que a melhor solução.
        for vizinho in solucao_atual.vizinhanca():
            if vizinho >= solucao_atual:
                lista_tabu.append(vizinho)

        # ordena pelo valor da solução e escolhe a melhor solução das encontradas.
        lista_tabu.sort(reverse=True)
        solucao_atual = lista_tabu.pop(0) if lista_tabu else solucao_atual
    return solucao_atual
	
	
	
	
	
