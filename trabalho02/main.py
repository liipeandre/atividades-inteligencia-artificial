from networkx import MultiDiGraph
from trabalho02.outros.operacoes_grafo import imprime_caminho
from trabalho02.outros.operacoes_problema import carregar_labirinto
from trabalho02.algoritmos.busca_gulosa import busca_gulosa
from trabalho02.algoritmos.busca_a_estrela import busca_a_estrela

def main():
    # carrega o labirinto
    estado_inicial = carregar_labirinto("labirinto/maze01.txt")

    # crio o grafo para o problema com o nodo inicial (modificar posicao final para o maze02.txt)
    grafo = MultiDiGraph(estado_inicial = {"labirinto": estado_inicial.copy(),\
                                         "posicao_labirinto": {"x": 1, "y": 1},\
                                         "chave": 1,\
                                         "acao": "Estado Inicial", \
                                         "custo_caminho": 0},\
                         estado_final = {"posicao_final": {"x": 19, "y": 31}})

    # aplico o algoritmo de busca (escolher um deles).
    caminho = busca_gulosa(grafo)
    #caminho = busca_a_estrela(grafo)

    # imprimo o resultado em tela
    imprime_caminho(caminho)

if __name__ == "__main__":
    main()