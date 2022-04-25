class congruencial_mult:
    def __init__(self, seed):
        self.seed = seed
        self.seed = (self.seed * (7**5)) % ((2**31) -1)
    def generar(self):
        num_gen = self.seed / ((2 ** 31) -1)
        self.seed = (self.seed * (7 ** 5)) % ((2 ** 31) -1)
        return num_gen
