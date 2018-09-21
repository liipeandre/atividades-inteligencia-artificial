from networkx import MultiDiGraph

# operacoes para o grafo.
def nao_borda_e_nao_explorado(nodo_novo, borda, explorado):
    ''' Verifica se o nodo está em borda ou em explorado '''
    for nodo_borda in borda:
        for nodo_explorado in explorado:
            if comparar_nodos(nodo_novo, nodo_borda) or comparar_nodos(nodo_novo, nodo_explorado):
                return False
    return True

def inserir_nodo_grafo(grafo: MultiDiGraph, chave: int, nodo: dict, nodo_novo: dict):
    grafo.add_node(chave,\
                   posicao_labirinto=nodo_novo["posicao_labirinto"],\
                   chave=chave,\
                   acao=nodo_novo["acao"],\
                   custo_caminho=nodo_novo["custo_caminho"])

    if nodo is not None:
        grafo.add_edge(nodo["chave"], chave)


def comparar_nodos(nodo1:dict, nodo2: dict):
    ''' Compara dois nodos pelas posicoes SOMENTE'''
    return nodo1["posicao_labirinto"] == nodo2["posicao_labirinto"]

def imprime_caminho(caminho):
    ''' Imprime o caminho em tela '''
    contador = 1
    for item in list(reversed(caminho)):
        print(f'{str(contador):4s}= Posicao no Labirinto: {str(item["posicao_labirinto"]):10s}   Acao: {item["acao"]}')
        contador += 1