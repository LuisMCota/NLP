from src.ising import IsingModel
from src.potts import PottsModel
from src.metropolis import Metropolis

class Simulacion:
    def __init__(self, L, modelo, temperatura, ciclos, campo_h=0.0):
        self.L = L
        self.temperatura = temperatura
        self.ciclos = ciclos
        self.campo_h = campo_h
        
        # Inicializar el modelo seleccionado
        if modelo == "Ising":
            self.modelo = IsingModel(L, h=campo_h)
        elif modelo == "Potts":
            self.modelo = PottsModel(L)
        else:
            raise ValueError("Modelo desconocido. Elija 'Ising' o 'Potts'.")

        # Crear una instancia del algoritmo de Metropolis
        self.metropolis = Metropolis(self.modelo, temperatura)

    def paso(self):
        # Ejecuta un paso del algoritmo de Metropolis
        self.metropolis.paso()
        # Retorna el estado actual de la energía y magnetización (ajustar según implementación)
        energia = self.modelo.energia()
        magnetizacion = getattr(self.modelo, 'magnetizacion', None)  # Si el modelo tiene magnetización
        return energia, magnetizacion

    def obtener_red(self):
        # Retorna la red de espines para visualización
        return self.modelo.red
