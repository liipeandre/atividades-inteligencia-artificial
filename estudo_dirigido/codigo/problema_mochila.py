from numpy import sum
from random import choice

class Solucao():
    capacidade_limite_mochila = 100
    def __init__(self, solucao=None):
        if solucao is None:
            self.dentro_mochila = []
            self.fora_mochila = []
            self.capacidade_atual_mochila = 0
            self.numero_itens_mochila = 0
        else:
            self.dentro_mochila = solucao.dentro_mochila.copy()
            self.fora_mochila = solucao.fora_mochila.copy()
            self.capacidade_atual_mochila = solucao.capacidade_atual_mochila
            self.numero_itens_mochila = solucao.numero_itens_mochila

    def __lt__(self, other):
        if self is None or other is None:
            return False
        return self.numero_itens_mochila < other.numero_itens_mochila and \
                self.capacidade_atual_mochila < other.capacidade_atual_mochila

    def __le__(self, other):
        if self is None or other is None:
            return False
        return self.numero_itens_mochila <= other.numero_itens_mochila and \
               self.capacidade_atual_mochila <= other.capacidade_atual_mochila

    def __gt__(self, other):
        if self is None or other is None:
            return False
        return self.numero_itens_mochila > other.numero_itens_mochila and \
                self.capacidade_atual_mochila > other.capacidade_atual_mochila

    def __ge__(self, other):
        if self is None or other is None:
            return False
        return self.numero_itens_mochila >= other.numero_itens_mochila and \
               self.capacidade_atual_mochila >= other.capacidade_atual_mochila

    def __sub__(self, other):
        if self is None or other is None:
            return False
        return self.numero_itens_mochila - other.numero_itens_mochila

    def __str__(self):
        return f"dentro mochila: {self.dentro_mochila}\nfora mochila: {self.fora_mochila}\ncapacidade: {self.capacidade_atual_mochila}\nnumero de itens: {self.numero_itens_mochila}"

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

            # atualiza a capacidade da mochila e o número de itens dentro dela
            solucao.capacidade_atual_mochila = sum(solucao.dentro_mochila)
            solucao.numero_itens_mochila = len(solucao.dentro_mochila)

            # insiro a solução na lista de vizinhança
            vizinhanca.append(solucao)

        # solucoes envolvendo a remoção de um elemento da mochila.
        for item in self.dentro_mochila.copy():

            # crio uma nova solucao, baseada na atual.
            solucao = Solucao(self)

            # retiro um item da mochila e coloco fora da mesma.
            solucao.fora_mochila.append(item)
            solucao.dentro_mochila.remove(item)

            # atualiza a capacidade da mochila e o numero de itens dentro dela
            solucao.capacidade_atual_mochila = sum(solucao.dentro_mochila)
            solucao.numero_itens_mochila = len(solucao.dentro_mochila)

            # insiro a solução na lista de vizinhança
            vizinhanca.append(solucao)

        # removo solucoes inválidas (aquelas que estouram o limite da mochila)
        vizinhanca = [vizinho for vizinho in vizinhanca if vizinho.capacidade_atual_mochila <= self.capacidade_limite_mochila]

        # retorno a vizinhanca
        return vizinhanca

def solucao_inicial():
    # gero N itens de 1 até 100
    lista_itens_original = gerar_itens(1)
    lista_itens = lista_itens_original.copy()

    # gero uma solucao inicial aleatoriamente e valida
    while True:
        # crio uma solucao vazia
        solucao = Solucao()

        # escolhe um item da lista de itens
        item_escolhido = choice(lista_itens)

        # adiciona o item dentro da mochila
        solucao.dentro_mochila.append(item_escolhido)

        # atualiza a capacidade da mochila e o numero de itens dentro dela
        solucao.capacidade_atual_mochila = sum(solucao.dentro_mochila)
        solucao.numero_itens_mochila = len(solucao.dentro_mochila)

        # remove o item da lista de itens
        lista_itens.remove(item_escolhido)

        # testo se a solucao é valida
        if solucao.capacidade_atual_mochila <= solucao.capacidade_limite_mochila: break
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