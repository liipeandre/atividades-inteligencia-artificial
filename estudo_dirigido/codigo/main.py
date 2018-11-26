from estudo_dirigido.codigo.simulated_annealing import simulated_annealing
from estudo_dirigido.codigo.tabu_search import tabu_search
from estudo_dirigido.codigo.problema_mochila import solucao_inicial, Solucao
from time import process_time

def main():
    # gero a solucao inicial
    solucao: Solucao = solucao_inicial(10)

    # roda o algoritmo tabu search e simulated annealing, capturando o tempo de execucao de cada um dos algoritmos
    tempo_inicial_tabu = process_time()
    melhor_solucao_tabu: Solucao = tabu_search(solucao)
    tempo_execucao_tabu = process_time() - tempo_inicial_tabu

    tempo_inicial_simulated = process_time()
    melhor_solucao_simulated: Solucao = simulated_annealing(5000, solucao)
    tempo_execucao_simulated = process_time() - tempo_inicial_simulated

    # grava em arquivo, os testes realizados
    with open("ResultadosTestes.txt", "w") as arquivo:
        arquivo.write(f"Solucao Inicial:\n{str(solucao)},\n\
                        Solucao Tabu Search:\n{str(melhor_solucao_tabu)},\n\
                        Solucao Simulated Annealing:\n{str(melhor_solucao_simulated)},\n\
                        Tempo Execucao Tabu Search: {tempo_execucao_tabu},\n\
                        Tempo Execucao Simulated Annealing: {tempo_execucao_simulated}\n")

if __name__ == '__main__':
    main()