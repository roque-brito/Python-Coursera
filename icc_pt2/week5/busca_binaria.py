# código para executar uma busca binária:

class Buscador:
    def buscador_sequencial(self, lista, x):
        for i in range(len(lista)):
            if lista[i] == x:
                return i
        return False

    def busca_binaria(self, lista, x):
        primeiro = 0
        ultimo = len(lista) - 1

        while primeiro <= ultimo:
            meio = (primeiro + ultimo) // 2

            if lista[meio] == x:
                print(lista[meio])
                return meio
            else:
                if x < lista[meio]:
                    ultimo = meio -1
                else:
                    primeiro = meio +1
            
        return False
