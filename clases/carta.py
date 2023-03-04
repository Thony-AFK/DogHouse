# Carta.py

class Carta:

    def __new__(cls, *args, **kwargs):
        #print("1. Crea una nueva instancia de Carta.")
        return super().__new__(cls)

    def __init__(self, vida):
        #print("2. Inicializa una nueva instancia de Carta.")
        self.vida = vida
