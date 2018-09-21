from networkx import MultiDiGraph
from trabalho02.outros.operacoes_grafo import *
from math import sqrt

def carregar_labirinto(nome_arquivo):
    labirinto = []
    with open(nome_arquivo, "r") as arquivo:
        linhas_lidas = arquivo.readlines()
        for linha in linhas_lidas:
            labirinto.append(list(\
                "1" + linha.replace("-", "1")\
                           .replace("+", "1")\
                           .replace("|", "1")\
                           .replace("E", " ")\
                           .replace("S", " ")\
                           .replace("\n", "1")))
    return labirinto

def teste_objetivo(grafo: MultiDiGraph, nodo: dict):
    ''' Teste se o objetivo foi atingido '''
    return nodo["posicao_labirinto"]["x"] == grafo.graph["estado_final"]["posicao_final"]["x"] and \
           nodo["posicao_labirinto"]["y"] == grafo.graph["estado_final"]["posicao_final"]["y"]

def mover_cima(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"posicao_labirinto": {"x": x - 1, "y": y}, \
                 "chave": 1, \
                 "acao": "Mover Cima", \
                 "custo_caminho": 1}
    return nodo_novo

def mover_baixo(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"posicao_labirinto": {"x": x + 1, "y": y}, \
                 "chave": 1, \
                 "acao": "Mover Baixo", \
                 "custo_caminho": 1}
    return nodo_novo

def mover_esquerda(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"posicao_labirinto": {"x": x, "y": y - 1}, \
                 "chave": 1, \
                 "acao": "Mover Esquerda", \
                 "custo_caminho": 1}
    return nodo_novo

def mover_direita(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"posicao_labirinto": {"x": x, "y": y + 1}, \
                 "chave": 1, \
                 "acao": "Mover Direita", \
                 "custo_caminho": 1}
    return nodo_novo

def acoes(grafo: MultiDiGraph, chave: int, nodo: dict):
    ''' Aplica todas as ações para o nodo e verifica se as ações são válidas, além de inseri-los no grafo '''

    # aplico todas as ações possíveis
    nodos_filhos = [nodo_filho for nodo_filho in [mover_cima(nodo), \
                                                  mover_baixo(nodo), \
                                                  mover_esquerda(nodo), \
                                                  mover_direita(nodo)]\
                    if estado_valido(grafo, nodo_filho)]

    # insiro-os no grafo
    for nodo_novo in nodos_filhos:
        nodo_novo["chave"] = chave
        inserir_nodo_grafo(grafo, chave, nodo, nodo_novo)
        chave += 1

    # retorno os que restaram
    return nodos_filhos, chave

def estado_valido(grafo: MultiDiGraph, nodo: dict):
    ''' Verifica se o estado é válido '''
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # se as coordenadas estão fora do alcance do labirinto ou se a casa é parede, o estado inválido
    max_linhas = len(grafo.graph["estado_inicial"]["labirinto"])
    max_colunas = len(grafo.graph["estado_inicial"]["labirinto"][x])
    if x < 0 or x >= max_linhas or \
         y < 0 or y >= max_colunas or \
         grafo.graph["estado_inicial"]["labirinto"][x][y] == "1":
        return False
    return True

def solucao(grafo: MultiDiGraph, nodo: dict):
    ''' Faz o backtracking do nodo final até o nodo inicial '''
    caminho = []        # caminho percorrido até aqui
    nodo_atual = nodo   # nodo atual
    while nodo_atual["posicao_labirinto"] != grafo.graph["estado_inicial"]["posicao_labirinto"]:  # enquanto o nodo não for o nodo inicial
        caminho += [nodo_atual]                                             # adiciono o nodo em caminho
        pai = [pai for pai in grafo.predecessors(nodo_atual["chave"])]      # busco o pai no grafo
        nodo_atual = grafo.nodes[pai[0]]    # nodo atual se torna o pai
                                            # [0], pois a função grafo.predecessors pode retornar mais de um pai
                                            # mas como cada nodo possui um id ÚNICO, cada nodo terá um único pai (árvore B)

    caminho.append(nodo_atual)              # no final, adiciono o nodo inicial.
    return caminho                          # retorno o caminho

def calcular_heuristica(grafo:MultiDiGraph, nodo: dict):
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # aplicando heurística
    return abs(grafo.graph["estado_final"]["posicao_final"]["x"] - x) + abs(grafo.graph["estado_final"]["posicao_final"]["y"] - y)