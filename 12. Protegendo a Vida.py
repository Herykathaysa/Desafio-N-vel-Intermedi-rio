class Personagem:
    def __init__(self, vida_inicial):
        self._vida = self._validar_vida(vida_inicial)

    def _validar_vida(self, valor):
        if valor < 0:
            raise ValueError("A vida não pode ser negativa.")
        return valor

    @property
    def vida(self):
        return self._vida

    @vida.setter
    def vida(self, novo_valor):
        self._vida = self._validar_vida(novo_valor)

p = Personagem(100)
print(p.vida)
try:
    p.vida = -10
except ValueError as e:
    print(e)