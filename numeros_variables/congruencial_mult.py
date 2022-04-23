class congruencial_mult:
    def __init__(self, seed, modulo):
        self.seed = seed
        self.seed = (self.seed * (7**5)) % ((2**modulo) -1)
    def generar(self, modulo):
        num_gen = self.seed / ((2 ** modulo) -1)
        self.seed = (self.seed * (7 ** 5)) % ((2 ** modulo) -1)
        return num_gen
