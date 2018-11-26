from numpy import sum
from random import choice

class Solucao():
    capacidade_limite_mochila = 100

    def __init__(self, solucao=None):
        if solucao is None:
            self.dentro_mochila = []
            self.fora_mochila = []
        else:
            self.dentro_mochila = solucao.dentro_mochila.copy()
            self.fora_mochila = solucao.fora_mochila.copy()

    def __lt__(self, other):
        if self is None or other is None:
            return False
        return len(self.dentro_mochila) < len(other.dentro_mochila)

    def __le__(self, other):
        if self is None or other is None:
            return False
        return len(self.dentro_mochila) <= len(other.dentro_mochila)

    def __gt__(self, other):
        if self is None or other is None:
            return False
        return len(self.dentro_mochila) > len(other.dentro_mochila)

    def __ge__(self, other):
        if self is None or other is None:
            return False
        return len(self.dentro_mochila) >= len(other.dentro_mochila)

    def __sub__(self, other):
        if self is None or other is None:
            return False
        return len(self.dentro_mochila) - len(other.dentro_mochila)

    def __str__(self):
        return f"Dentro mochila: {self.dentro_mochila}\nFora mochila: {self.fora_mochila}\nCapacidade: {sum(self.dentro_mochila)},\nNumero de itens: {len(self.dentro_mochila)}\n\n"

    def vizinhanca(self):
        # lista vazia de vizinhos
        vizinhanca = []

        # solucoes envolvendo a inserção de um elemento na mochila.
        for item in self.fora_mochila.copy():

            # crio uma nova solucao, baseada na atual.
            solucao = Solucao(self)

            # retiro um item de fora da mochila e coloco dentro da mesma.
            solucao.dentro_mochila.append(item)
            solucao.fora_mochila.remove(item)

            # insiro a solução na lista de vizinhança
            vizinhanca.append(solucao)

        # solucoes envolvendo a remoção de um elemento da mochila.
        for item in self.dentro_mochila.copy():

            # crio uma nova solucao, baseada na atual.
            solucao = Solucao(self)

            # retiro um item da mochila e coloco fora da mesma.
            solucao.fora_mochila.append(item)
            solucao.dentro_mochila.remove(item)

            # insiro a solução na lista de vizinhança
            vizinhanca.append(solucao)

        # removo solucoes inválidas (aquelas que estouram o limite da mochila)
        vizinhanca = [vizinho for vizinho in vizinhanca if sum(vizinho.dentro_mochila) <= self.capacidade_limite_mochila]

        # retorno a vizinhanca
        return vizinhanca

def solucao_inicial(num_elementos):
    # gero N itens de 1 até 100
    lista_itens_original = gerar_itens(num_elementos)
    lista_itens = lista_itens_original.copy()

    # gero uma solucao inicial aleatoriamente e valida
    while True:
        # crio uma solucao vazia
        solucao = Solucao()

        # escolhe um item da lista de itens
        item_escolhido = choice(lista_itens)

        # adiciona o item dentro da mochila
        solucao.dentro_mochila.append(item_escolhido)

        # remove o item da lista de itens
        lista_itens.remove(item_escolhido)

        # testo se a solucao é valida
        if sum(solucao.dentro_mochila) <= solucao.capacidade_limite_mochila: break
        else: lista_itens = lista_itens_original.copy()

    # adiciona os restantes como itens fora da mochila
    solucao.fora_mochila = lista_itens.copy()

    # retorna a solucao inicial gerada.
    return solucao

def gerar_itens(numero_itens_para_gerar: int):
    # crio uma lista de itens de 1 até 100
    tipos_itens = list(range(1, 101))
    numero_itens = [numero_itens_para_gerar] * len(tipos_itens)

    # replico cada item N vezes.
    itens = []
    for numero_item, tipo_item in zip(numero_itens, tipos_itens):
        itens += [tipo_item] * numero_item

    # retorna os itens gerados
    return itens