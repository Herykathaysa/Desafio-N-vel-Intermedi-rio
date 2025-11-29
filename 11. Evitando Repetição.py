class Personagem:
    def __init__(self, nome, vida, ataque, defesa):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa

    def atacar(self, alvo):
        print(f"{self.nome} ataca {alvo.nome}!")

    def defender(self):
        print(f"{self.nome} está se defendendo.")

class Guerreiro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, furia):
        super().__init__(nome, vida, ataque, defesa)
        self.furia = furia

class Mago(Personagem):
    def __init__(self, nome, vida, ataque, defesa, tipo_magia):
        super().__init__(nome, vida, ataque, defesa)
        self.tipo_magia = tipo_magia
    
    def lancar_magia(self):
        print(f"{self.nome} lança uma magia de {self.tipo_magia}.")

class Arqueiro(Personagem):
    def __init__(self, nome, vida, ataque, defesa, precisao):
        super().__init__(nome, vida, ataque, defesa)
        self.precisao = precisao