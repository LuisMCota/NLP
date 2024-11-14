class IsingModel:
    def __init__(self, L, h=0.0, j=1.0):
        self.L = L
        self.h = h  # Campo magnético
        self.j = j  # Interacción entre espines
        self.red = [[1 if (i + j) % 2 == 0 else -1 for i in range(L)] for j in range(L)]  # Inicialización

    def energia(self):
        # Cálculo de energía total (simplificado)
        energia_total = 0
        for i in range(self.L):
            for j in range(self.L):
                # Considera vecinos y calcula la interacción
                espin = self.red[i][j]
                vecinos = [
                    self.red[(i + 1) % self.L][j],
                    self.red[i][(j + 1) % self.L],
                    self.red[(i - 1) % self.L][j],
                    self.red[i][(j - 1) % self.L]
                ]
                energia_total -= self.j * espin * sum(vecinos)
                energia_total -= self.h * espin
        return energia_total
