from random import randint
from config import \
    ALCANCE_MINIMO_NUMEROS, ALCANCE_MAXIMO_NUMEROS, QUANTIDADE_NUMEROS_SORTEADOS, lista_numeros_sorte


class SorteadorDeDezenas:
    def __init__(self):
        self.lista_aleatoria_faltante = self._sorteia_lista_faltante()

    def run(self):
        self.mostra_lista_sorte()
        self.mostra_quantidade_jogos(self.lista_aleatoria_faltante)
        self.mostra_lista_aleatoria_gerada(self.lista_aleatoria_faltante)
        self.mostra_lista_misturada()

    def _mistura_lista(self):
        lista_sorte = lista_numeros_sorte
        lista_misturada = []
        for s in enumerate(lista_sorte):
            lista_misturada.append(s[1]+self.lista_aleatoria_faltante[s[0]])
        return lista_misturada

    @staticmethod
    def mostra_lista_aleatoria_gerada(lista_sorteado):
        print('--' * 5)
        print('Lista pré sorteada aleatória:')
        for y in lista_sorteado:
            print(y, '\n')

    @staticmethod
    def mostra_quantidade_jogos(lista):
        print('--'*5)
        print('tamanho  :   ', len(lista))

    @staticmethod
    def mostra_lista_sorte():
        lista_sorte = lista_numeros_sorte
        print('--'*5)
        print('Lista da sorte:')
        for y in lista_sorte:
            print(y, '\n')


    @staticmethod
    def mostra_lista_misturada():
        lista_sorte = SorteadorDeDezenas()._mistura_lista()
        print('--'*5)
        print('Lista da Sorteada para você:')
        for y in lista_sorte:
            print(y, '\n')

    def _sorteia_lista_faltante(self):
        lista_aleatoria = []
        for i in lista_numeros_sorte:
            numeros_gerados = self._sorteia_lista_numeros_faltantes(i)
            lista_aleatoria.append(numeros_gerados)
        return lista_aleatoria

    def _sorteia_lista_numeros_faltantes(self, l_sorte):
        lista = []
        for x in range(QUANTIDADE_NUMEROS_SORTEADOS):
            primeiro_da_lista = False
            if len(lista) == 0:
                primeiro_da_lista = True
            lista.append(self._sorteia_numero_faltante(l_sorte, primeiro_da_lista, lista))
        return lista

    def _sorteia_numero_faltante(self, lista_conjunto, primeiro_da_lista, lista_construindo):
        a = int
        while True:
            a = randint(ALCANCE_MINIMO_NUMEROS, ALCANCE_MAXIMO_NUMEROS)
            if self._seleciona_inexistente(a, lista_conjunto) and \
                    primeiro_da_lista or \
                    self._seleciona_inexistente(a, lista_conjunto) and \
                    self._seleciona_inexistente(a, lista_construindo):
                break
        return a

    @staticmethod
    def _seleciona_inexistente(numero, lista):
        if numero not in lista:
            return True


if __name__ == '__main__':
    SorteadorDeDezenas().run()
