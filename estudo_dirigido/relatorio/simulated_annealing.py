from math import exp
from random import random
from os import system
from estudo_dirigido.codigo.problema_mochila import *
from estudo_dirigido.codigo.controle_parada import *

def atualiza_temperatura():
    ControleParada.temperatura_atual -= 1

def simulated_annealing(temperatura_inicial):
    # escolher uma solução inicial e uma global(que será a atual), existentes no espaço de busca, dada uma regra definida.
    solucao_atual  = solucao_inicial()
    melhor_solucao = solucao_atual

    # defino a temperatura inicial
    temperatura_atual = temperatura_inicial

    # enquanto não atingo a condição de parada.
    while not condicao_parada(solucao_atual):

        # seleciona os vizinhos melhores que a solucao_atual.
        for vizinho in solucao_atual.vizinhanca():

            # se o vizinho for melhor ou igual à solução atual, faço ele a solução atual.
            if vizinho >= solucao_atual:
                solucao_atual = vizinho

                # se o vizinho for melhor que a melhor solução, faço ele a melhor solução
                if vizinho >= melhor_solucao:
                    melhor_solucao = vizinho

            # se o resultado da equação for maior que o valor sorteado, faço ele a solução atual.
            # quanto maior a temperatura, maior a chance dele escolher uma solução ruim como solução atual.
            # isso serve para realizar a busca em seus vizinhos, para "pular" os mínimos/máximos locais,
            # visando atingir o mínimo/máximo global.
            elif exp((solucao_atual - vizinho) / temperatura_atual) > random():
                solucao_atual = vizinho

        # calcula a temperatura
        atualiza_temperatura(temperatura_atual)
    return melhor_solucao
	
	
	
	
	
	
	
