from outros.operacoes_problema import *

def busca_custo_uniforme(grafo: MultiDiGraph):
    nodo = grafo.graph["estado_inicial"]      # seto o nodo inicial como o estado inicial
    inserir_nodo_grafo(grafo, 1, None, nodo)  # adiciona o nodo inicial no grafo

    if teste_objetivo(nodo):            # testo se esse estado é o final (teste objetivo)
        return solucao(grafo, nodo)     # se verdadeiro, retorno o caminho (solucao)

    borda = [nodo]   # borda eh uma FILA ORDENADA PELO CUSTO, de nodos a serem explorados
    explorado = []   # explorado eh uma lista de nodos já explorados
    chave = 2        # id para adicionar novos nodos no grafo
    while True:
        if not borda:   # se borda vazia, retorno lista vazia
            return []
        borda.sort(key=lambda x: x["custo_caminho"]) # ordeno a borda pelo custo do caminho
        nodo = borda.pop(0)     # removo o elemento da borda (que terá o menor custo)
        explorado.append(nodo)  # e adiciono em explorado

        if teste_objetivo(nodo):  # testo se esse estado é o final (teste objetivo)
            return solucao(grafo, nodo)  # se verdadeiro, retorno o caminho (solucao)

        nodos_filhos, chave = acoes(grafo, chave, nodo)  # gero todas as acoes possiveis para esse nodo

        for nodo_novo in nodos_filhos:   # para cada um dos novos nodos
            if nao_borda_e_nao_explorado(nodo_novo, borda, explorado):   # se nao estiver em borda e nem em explorado
                borda.append(nodo_novo)                 # se falso, adiciono o nodo na borda para ser explorado futuramente
            else:
                for nodo_borda in borda.copy():
                    # se existe um caminho mais curto para o nodo gerado e ele já estiver na borda
                    if comparar_nodos(nodo_novo, nodo_borda) and nodo_novo["custo_caminho"] < nodo_borda["custo_caminho"]:
                        del nodo_borda   # removo o pior caminho
                        borda.append(nodo_novo)  # adiciono o melhor