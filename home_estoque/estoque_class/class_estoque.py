class estoque:
    def __init__(self):
        self.itens = {}

    def adicionar_item(self, nome, quantidade):
        if nome in self.itens:
            self.itens[nome] += quantidade
        else:
            self.itens[nome] = quantidade

    def remover_item(self, nome, quantidade):
        if nome in self.itens:
            if self.itens[nome] >= quantidade:
                self.itens[nome] -= quantidade
                if self.itens[nome] == 0:
                    del self.itens[nome]
            else:
                print("Quantidade insuficiente no estoque.")
        else:
            print("Item não encontrado no estoque.")

    def ver_estoque(self):
        return self.itens