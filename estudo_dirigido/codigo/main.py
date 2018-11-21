from estudo_dirigido.codigo.simulated_annealing import simulated_annealing
from estudo_dirigido.codigo.tabu_search import tabu_search

def main():
    # roda o algoritmo tabu search
    #melhor_solucao = tabu_search()
    melhor_solucao = simulated_annealing(10)

    print(melhor_solucao)

if __name__ == '__main__':
    main()