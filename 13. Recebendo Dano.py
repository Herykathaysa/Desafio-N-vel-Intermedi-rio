class Personagem:
    def __init__(self, nome, vida_total):
        self.nome = nome
        self.vida_total = vida_total
        self.vida_atual = vida_total
        print(f"{self.nome} entrou na batalha com {self.vida_atual} de vida.")

    def receber_dano(self, dano):
        if dano < 0:
            print(f"{self.nome} não pode receber dano negativo.")
            return

        print(f"{self.nome} sofreu {dano} de dano!")

        self.vida_atual = max(0, self.vida_atual - dano)

        if self.vida_atual == 0:
            print(f"{self.nome} foi derrotado!")
        else:
            print(f"Vida restante de {self.nome}: {self.vida_atual}/{self.vida_total}")

heroi = Personagem("Tomy", 100)

print("-" * 50)

heroi.receber_dano(45)

print("-" * 45)

heroi.receber_dano(10)