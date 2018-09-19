from networkx import MultiDiGraph
from outros.operacoes_grafo import *
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
                           .replace("E", "P")\
                           .replace("S", " ")\
                           .replace("\n", "1")))
    return labirinto

def teste_objetivo(nodo: dict):
    ''' Teste se o objetivo foi atingido '''
    return nodo["posicao_labirinto"]["x"] == 61 and nodo["posicao_labirinto"]["y"] == 41

def mover_cima(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"estado_labirinto": nodo["estado_labirinto"].copy(), \
                 "posicao_labirinto": {"x": x, "y": y}, \
                 "chave": 1, \
                 "acao": "Mover Cima", \
                 "custo_caminho": 1}

    # extraindo a posicao atual no labirinto
    x = nodo_novo["posicao_labirinto"]["x"]
    y = nodo_novo["posicao_labirinto"]["y"]

    # se a casa que quero ir for parede (1), a acao é invalida.
    if x <= 0 or nodo_novo["estado_labirinto"][x - 1][y] == "1":
        return "invalido"
    else:
        # faço a troca do conteudo das duas casas
        nodo_novo["estado_labirinto"][x - 1][y], nodo_novo["estado_labirinto"][x][y] = \
        nodo_novo["estado_labirinto"][x][y],     nodo_novo["estado_labirinto"][x - 1][y]

        # atualizo a posicao atual.
        nodo_novo["posicao_labirinto"]["x"] -= 1
        return nodo_novo

def mover_baixo(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"estado_labirinto": nodo["estado_labirinto"].copy(), \
                 "posicao_labirinto": {"x": x, "y": y}, \
                 "chave": 1, \
                 "acao": "Mover Baixo", \
                 "custo_caminho": 1}

    # extraindo a posicao atual no labirinto
    x = nodo_novo["posicao_labirinto"]["x"]
    y = nodo_novo["posicao_labirinto"]["y"]

    # se a casa que quero ir for parede (1), a acao é invalida.
    if x >= len(nodo_novo["estado_labirinto"]) - 1 or nodo_novo["estado_labirinto"][x + 1][y] == "1":
        return "invalido"
    else:
        # faço a troca do conteudo das duas casas
        nodo_novo["estado_labirinto"][x + 1][y], nodo_novo["estado_labirinto"][x][y] = \
        nodo_novo["estado_labirinto"][x][y],     nodo_novo["estado_labirinto"][x + 1][y]

        # atualizo a posicao atual.
        nodo_novo["posicao_labirinto"]["x"] += 1

        return nodo_novo

def mover_esquerda(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"estado_labirinto": nodo["estado_labirinto"].copy(), \
                 "posicao_labirinto": {"x": x, "y": y}, \
                 "chave": 1, \
                 "acao": "Mover Esquerda", \
                 "custo_caminho": 1}

    # extraindo a posicao atual no labirinto
    x = nodo_novo["posicao_labirinto"]["x"]
    y = nodo_novo["posicao_labirinto"]["y"]

    # se a casa que quero ir for parede (1), a acao é invalida.
    if y <= 0 or nodo_novo["estado_labirinto"][x][y - 1] == "1":
        return "invalido"
    else:
        # faço a troca do conteudo das duas casas
        nodo_novo["estado_labirinto"][x][y - 1], nodo_novo["estado_labirinto"][x][y] = \
        nodo_novo["estado_labirinto"][x][y],     nodo_novo["estado_labirinto"][x][y - 1]

        # atualizo a posicao atual.
        nodo_novo["posicao_labirinto"]["y"] -= 1

        return nodo_novo

def mover_direita(nodo: dict):
    # extraindo a posicao atual no labirinto
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # crio um novo estado
    nodo_novo = {"estado_labirinto": nodo["estado_labirinto"].copy(), \
                 "posicao_labirinto": {"x": x, "y": y}, \
                 "chave": 1, \
                 "acao": "Mover Direita", \
                 "custo_caminho": 1}

    # extraindo a posicao atual no labirinto
    x = nodo_novo["posicao_labirinto"]["x"]
    y = nodo_novo["posicao_labirinto"]["y"]

    # se a casa que quero ir for parede (1), a acao é invalida.
    if y >= len(nodo_novo["estado_labirinto"][x]) - 1 or nodo_novo["estado_labirinto"][x][y + 1] == "1":
        return "invalido"
    else:
        # faço a troca do conteudo das duas casas
        nodo_novo["estado_labirinto"][x][y + 1], nodo_novo["estado_labirinto"][x][y] = \
        nodo_novo["estado_labirinto"][x][y],     nodo_novo["estado_labirinto"][x][y + 1]

        # atualizo a posicao atual.
        nodo_novo["posicao_labirinto"]["y"] += 1

        return nodo_novo

def acoes(grafo: MultiDiGraph, chave: int, nodo: dict):
    ''' Aplica todas as ações para o nodo e verifica se as ações são válidas, além de inseri-los no grafo '''

    # aplico todas as ações possíveis
    nodos_filhos = [nodo_filho for nodo_filho in [mover_cima(nodo), \
                                                  mover_baixo(nodo), \
                                                  mover_esquerda(nodo), \
                                                  mover_direita(nodo)]\
                    if estado_valido(nodo_filho)]

    # insiro-os no grafo
    for nodo_novo in nodos_filhos:
        nodo_novo["chave"] = chave
        inserir_nodo_grafo(grafo, chave, nodo, nodo_novo)
        chave += 1

    # retorno os que restaram
    return nodos_filhos, chave

def estado_valido(nodo: dict):
    ''' Verifica se o estado é válido '''

    # se ele ja vier invalido, continua invalido
    if nodo == "invalido":
        return False
    return True

def solucao(grafo: MultiDiGraph, nodo: dict):
    ''' Faz o backtracking do nodo final até o nodo inicial '''
    caminho = []        # caminho percorrido até aqui
    nodo_atual = nodo   # nodo atual
    while nodo_atual != grafo.graph["estado_inicial"]:  # enquanto o nodo não for o nodo inicial
        caminho += [nodo_atual]                                             # adiciono o nodo em caminho
        pai = [pai for pai in grafo.predecessors(nodo_atual["chave"])]      # busco o pai no grafo
        nodo_atual = grafo.nodes[pai[0]]    # nodo atual se torna o pai
                                            # [0], pois a função grafo.predecessors pode retornar mais de um pai
                                            # mas como cada nodo possui um id ÚNICO, cada nodo terá um único pai (árvore B)

    caminho.append(nodo_atual)              # no final, adiciono o nodo inicial.
    return caminho                          # retorno o caminho

def calcular_heuristica(nodo: dict):
    x = nodo["posicao_labirinto"]["x"]
    y = nodo["posicao_labirinto"]["y"]

    # aplicando heurística
    return abs(61 - x) + abs(41 - y)