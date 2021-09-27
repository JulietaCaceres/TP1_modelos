class Prenda:
    def __init__(self, id_prenda, tiempo_lavado):
        self.id = id_prenda
        self.tiempo_lavado = tiempo_lavado
    
    def __repr__(self):
        return str(self.id)
