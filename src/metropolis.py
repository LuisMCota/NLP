import random
import math
from ising import IsingModel
from potts import PottsModel

class Metropolis:
    def __init__(self, modelo, temperatura):
        self.modelo = modelo
        self.temperatura = temperatura

    def paso(self):
        L = self.modelo.L
        i, j = random.randint(0, L - 1), random.randint(0, L - 1)
        
        # Cambio de espín o estado en el sitio (i, j)
        energia_inicial = self.modelo.energia()
        estado_anterior = self.modelo.red[i][j]
        
        # Cambiar espín (Ising) o estado aleatorio (Potts)
        if isinstance(self.modelo, IsingModel):
            self.modelo.red[i][j] *= -1  # Cambiar espín
        elif isinstance(self.modelo, PottsModel):
            nuevo_estado = (estado_anterior + random.randint(1, self.modelo.q - 1)) % self.modelo.q
            self.modelo.red[i][j] = nuevo_estado
        
        energia_final = self.modelo.energia()
        delta_e = energia_final - energia_inicial

        # Criterio de Metropolis
        if delta_e > 0 and random.random() >= math.exp(-delta_e / self.temperatura):
            # Rechazar el cambio
            self.modelo.red[i][j] = estado_anterior
