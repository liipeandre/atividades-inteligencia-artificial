class ControleParada():
    # criterio de parada do tabu search
    numero_iteracoes_sem_melhora = 0
    max_iteracoes_sem_melhora = 100
    melhor_solucao = None

    # critério de parada do simulated annealing
    temperatura_atual = None

    def condicao_parada_tabu(self, solucao_atual):
        # testa se a melhor solucao é pior ou igual a atual
        if self.melhor_solucao is None:
            self.melhor_solucao = solucao_atual
            self.numero_iteracoes_sem_melhora = 0

        if self.melhor_solucao < solucao_atual:
            # atualiza o número de iteracoes
            self.numero_iteracoes_sem_melhora += 1
        else:
            # reseta o contador
            self.numero_iteracoes_sem_melhora = 0

            # atualiza melhor solucao
            self.melhor_solucao = solucao_atual

        # testa condicao de parada
        return self.numero_iteracoes_sem_melhora == self.max_iteracoes_sem_melhora

    def condicao_parada_simulated(self, solucao_atual):
        # testa se a melhor solucao é pior ou igual a atual
        if self.melhor_solucao is None:
            self.melhor_solucao = solucao_atual

        if self.melhor_solucao < solucao_atual:
            # atualiza o número de iteracoes
            self.numero_iteracoes_sem_melhora += 1
        else:
            # reseta o contador
            self.numero_iteracoes_sem_melhora = 0

            # atualiza melhor solucao
            self.melhor_solucao = solucao_atual

        # testa condicao de parada
        return self.numero_iteracoes_sem_melhora == self.max_iteracoes_sem_melhora or self.temperatura_atual == 0