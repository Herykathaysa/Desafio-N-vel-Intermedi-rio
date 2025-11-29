class Personagem:
    def __init__(self, nome, vida_total):
        self.nome = nome
        self.vida_total = vida_total
        self.vida_atual = vida_total
        self.pocoes = 0

personagem1 = Personagem('Aroudo, 100, 120')

    def exibir_status(self):
        print(f"Status de {self.nome}:")
        print(f"  Vida: {self.vida_atual}/{self.vida_total}")
        print(f"  Poções no inventário: {self.pocoes}\n")