import random

class PottsModel:
    def __init__(self, L, q=3):
        self.L = L
        self.q = q  # Número de estados
        self.red = [[random.randint(0, q-1) for _ in range(L)] for _ in range(L)]

    def energia(self):
        # Cálculo de energía para el modelo de Potts
        energia_total = 0
        for i in range(self.L):
            for j in range(self.L):
                espin = self.red[i][j]
                vecinos = [
                    self.red[(i + 1) % self.L][j],
                    self.red[i][(j + 1) % self.L],
                    self.red[(i - 1) % self.L][j],
                    self.red[i][(j - 1) % self.L]
                ]
                energia_total -= sum(1 for vecino in vecinos if vecino == espin)
        return energia_total
