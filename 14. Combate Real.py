class Combatente:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        print(f"{self.nome} entrou na batalha com {self.vida} de vida e {self.ataque} de ataque.")

    def atacar(self, alvo):
        dano_causado = self.ataque
        print(f"\n{self.nome} ataca {alvo.nome}!")
        alvo.receber_dano(dano_causado)

    def receber_dano(self, dano):
        self.vida -= dano
        print(f"{self.nome} recebeu {dano} de dano.")
        if self.vida <= 0:
            print(f"{self.nome} foi derrotado!")
            self.vida = 0
        else:
            print(f"Vida atual de {self.nome}: {self.vida}.")

heroi = Combatente("Herói Arrojado", 80, 20)
monstro = Combatente("Monstro Fraco", 30, 5)

heroi.atacar(monstro)
monstro.atacar(heroi)
heroi.atacar(monstro)
monstro.atacar(heroi)
heroi.atacar(monstro)