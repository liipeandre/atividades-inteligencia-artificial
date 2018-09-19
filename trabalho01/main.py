from networkx import MultiDiGraph
from outros.operacoes_grafo import imprime_caminho
from algoritmos.busca_largura import busca_largura
from algoritmos.busca_profundidade import busca_profundidade
from algoritmos.busca_custo_uniforme import busca_custo_uniforme

def main():
    # crio o grafo para o problema com o nodo inicial
    grafo = MultiDiGraph(estado_inicial={"A":[1, 2, 3, 4, 5],\
                                         "B":[],\
                                         "C":[],\
                                         "chave": 1,\
                                         "acao": "Estado Inicial", \
                                         "custo_caminho": 1})

    # aplico o algoritmo de busca (escolher um deles).
    #caminho = busca_largura(grafo)
    #caminho = busca_profundidade(grafo)
    caminho = busca_custo_uniforme(grafo)

    # imprimo o resultado em tela
    imprime_caminho(caminho)

if __name__ == "__main__":
    main()