class Prenda:
    def __init__(self, id_prenda):
        self.id = id_prenda
        self.tiempo_lavado = 0
    
    def __repr__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)

    def __eq__(self, other):
        if not isinstance(other, type(self)): return NotImplemented
        return self.id == other.id