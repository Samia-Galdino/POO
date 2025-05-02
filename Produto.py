class Produto:
    def _init_(self, nome, preco, estoque):
        self.__nome = nome
        self.__preco = preco
        self.__estoque = estoque

    # Getters
    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_estoque(self):
        return self.__estoque

    # Setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido.")

    def set_estoque(self, estoque):
        if estoque >= 0:
            self.__estoque = estoque
        else:
            print("Estoque inválido.")

    # Métodos de operação
    def vender(self, quantidade):
        if quantidade > 0 and quantidade <= self.__estoque:
            self.__estoque -= quantidade
            print(f"Venda realizada: {quantidade} unidades de {self.__nome}.")
        else:
            print("Quantidade indisponível para venda.")

    def repor(self, quantidade):
        if quantidade > 0:
            self.__estoque += quantidade
            print(f"Foram adicionadas {quantidade} unidades ao estoque de {self.__nome}.")
        else:
            print("Quantidade inválida para reposição.")

    def detalhes(self):
        print(f"Produto: {self._nome} | Preço: R${self.preco:.2f} | Estoque: {self._estoque} unidades")

# Exemplo de uso
produto1 = Produto(nome="Camisa", preco=59.90, estoque=100)

produto1.detalhes()
produto1.vender(3)
produto1.detalhes()
produto1.repor(5)
produto1.detalhes()
