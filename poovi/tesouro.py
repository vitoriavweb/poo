class tesouro:

    IPCA = 5.78 / 100
    SELIC = 12.25 / 100

    def __init__(self, valor, taxa):
        self.valor = valor
        self.taxa = taxa

    def rendimento(self):
        return self.valor * ( 1 + self.taxa)
    
t1 = tesouro(100, 50 / 100)
t2 = tesouro(100, tesouro.IPCA)
t3 = tesouro(100, tesouro.SELIC)

tesouro.IPCA = 1 / 100

print(t1.rendimento())
print(t2.rendimento_ipca())
print(t3.rendimento())