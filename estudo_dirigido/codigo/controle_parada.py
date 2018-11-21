class ControleParada():
    # criterio de parada do tabu search
    numero_iteracoes_sem_melhora = 0
    max_iteracoes_sem_melhora = 1000
    solucao_anterior = None

    # critério de parada do simulated annealing
    temperatura_atual = None

    def condicao_parada_tabu(self, solucao_atual):
        # testa se a solucao anterior é pior ou igual a atual
        if self.solucao_anterior <= solucao_atual:
            # atualiza o número de iteracoes
            self.numero_iteracoes_sem_melhora += 1
        else:
            # reseta o contador
            self.numero_iteracoes_sem_melhora = 0

        # atualiza solucao anterior
        self.solucao_anterior = solucao_atual

        # testa condicao de parada
        return self.numero_iteracoes_sem_melhora == self.max_iteracoes_sem_melhora or solucao_atual.capacidade_atual_mochila == solucao_atual.capacidade_limite_mochila

    def condicao_parada_simulated(self, solucao_atual):
        return self.temperatura_atual == 0 or solucao_atual.capacidade_atual_mochila == solucao_atual.capacidade_limite_mochila