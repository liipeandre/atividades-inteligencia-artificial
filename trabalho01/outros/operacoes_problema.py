from networkx import MultiDiGraph
from outros.operacoes_grafo import *

def teste_objetivo(nodo: dict):
    ''' Teste se o objetivo foi atingido '''
    return nodo["C"] == [1, 2, 3, 4, 5]

def AtoB(nodo: dict):
    ''' Remove o elemento da pilha A e adiciono em B '''
    novo_nodo = {"A": nodo["A"].copy(),\
                 "B": nodo["B"].copy(),\
                 "C": nodo["C"].copy(),\
                 "acao": "Remocao de A para colocar em B", \
                 "custo_caminho": 1}   # defino um novo nodo

    if novo_nodo["A"]:                       # se pilha não vazia
        elemento = novo_nodo["A"].pop(0)     # removo o elemento do topo da pilha A
        novo_nodo["B"].insert(0, elemento)   # adiciono na pilha B
    else:
        return "invalido"   # se pilha vazia, esta acao é inválida (estado inválido)
    return novo_nodo   # retorno o estado criado

def AtoC(nodo: dict):
    ''' Remove o elemento da pilha A e adiciono em C '''
    novo_nodo = {"A": nodo["A"].copy(),\
                 "B": nodo["B"].copy(),\
                 "C": nodo["C"].copy(),\
                 "acao": "Remocao de A para colocar em C",\
                 "custo_caminho": 1}   # defino um novo nodo

    if novo_nodo["A"]:                       # se pilha não vazia
        elemento = novo_nodo["A"].pop(0)     # removo o elemento do topo da pilha A
        novo_nodo["C"].insert(0, elemento)   # adiciono na pilha C
    else: return "invalido"   # se pilha vazia, esta acao é inválida (estado inválido)
    return novo_nodo   # retorno o estado criado

def BtoA(nodo: dict):
    ''' Remove o elemento da pilha B e adiciono em A '''
    novo_nodo = {"A": nodo["A"].copy(),\
                 "B": nodo["B"].copy(),\
                 "C": nodo["C"].copy(),\
                 "acao": "Remocao de B para colocar em A", \
                 "custo_caminho": 1}   # defino um novo nodo

    if novo_nodo["B"]:                       # se pilha não vazia
        elemento = novo_nodo["B"].pop(0)     # removo o elemento do topo da pilha B
        novo_nodo["A"].insert(0, elemento)   # adiciono na pilha A
    else: return "invalido"   # se pilha vazia, esta acao é inválida (estado inválido)
    return novo_nodo   # retorno o estado criado

def BtoC(nodo: dict):
    ''' Remove o elemento da pilha B e adiciono em C '''
    novo_nodo = {"A": nodo["A"].copy(),\
                 "B": nodo["B"].copy(),\
                 "C": nodo["C"].copy(),\
                 "acao": "Remocao de B para colocar em C", \
                 "custo_caminho": 1}   # defino um novo nodo

    if novo_nodo["B"]:                       # se pilha não vazia
        elemento = novo_nodo["B"].pop(0)     # removo o elemento do topo da pilha B
        novo_nodo["C"].insert(0, elemento)   # adiciono na pilha C
    else: return "invalido"   # se pilha vazia, esta acao é inválida (estado inválido)
    return novo_nodo   # retorno o estado criado

def CtoA(nodo: dict):
    ''' Remove o elemento da pilha C e adiciono em A '''
    novo_nodo = {"A": nodo["A"].copy(),\
                 "B": nodo["B"].copy(),\
                 "C": nodo["C"].copy(),\
                 "acao": "Remocao de C para colocar em A", \
                 "custo_caminho": 1}   # defino um novo nodo

    if novo_nodo["C"]:                       # se pilha não vazia
        elemento = novo_nodo["C"].pop(0)     # removo o elemento do topo da pilha C
        novo_nodo["A"].insert(0, elemento)   # adiciono na pilha A
    else: return "invalido"   # se pilha vazia, esta acao é inválida (estado inválido)
    return novo_nodo   # retorno o estado criado

def CtoB(nodo: dict):
    ''' Remove o elemento da pilha C e adiciono em B '''
    novo_nodo = {"A": nodo["A"].copy(),\
                 "B": nodo["B"].copy(),\
                 "C": nodo["C"].copy(),\
                 "acao": "Remocao de C para colocar em B", \
                 "custo_caminho": 1}   # defino um novo nodo

    if novo_nodo["C"]:                       # se pilha não vazia
        elemento = novo_nodo["C"].pop(0)     # removo o elemento do topo da pilha C
        novo_nodo["B"].insert(0, elemento)   # adiciono na pilha B
    else: return "invalido"   # se pilha vazia, esta acao é inválida (estado inválido)
    return novo_nodo   # retorno o estado criado

def acoes(grafo: MultiDiGraph, chave: int, nodo: dict):
    ''' Aplica todas as ações para o nodo e verifica se as ações são válidas, além de inseri-los no grafo '''

    # aplico todas as ações possíveis
    nodos_filhos = [nodo_filho for nodo_filho in [AtoB(nodo),\
                                                  AtoC(nodo),\
                                                  BtoA(nodo),\
                                                  BtoC(nodo),\
                                                  CtoA(nodo),\
                                                  CtoB(nodo)]\
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

    # testando se os aneis estao em ordem de tamanho
    lista_ordenada_A = sorted(nodo["A"])
    lista_ordenada_B = sorted(nodo["B"])
    lista_ordenada_C = sorted(nodo["C"])
    return lista_ordenada_A == nodo["A"] and lista_ordenada_B == nodo["B"] and lista_ordenada_C == nodo["C"]

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