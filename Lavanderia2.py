import itertools

class Lavanderia2:
    
    def __init__(self):
        self.prendas = []
        self.incompatibilidades = {}
        self.combinaciones = {}
        
    def __contains__(self, prenda):
        return prenda.id in [prenda.id for prenda in self.prendas] 

    def guardar_incompatibilidad(self, prenda, prenda_incompatible):
        if prenda not in self.incompatibilidades:
            self.incompatibilidades[prenda] = set()
        self.incompatibilidades[prenda].add(prenda_incompatible)
        
    def _obtener_combinaciones_de_lavados(self):
        self.prendas.sort(key=lambda prenda: prenda.tiempo_lavado, reverse=True)
        prendas = set([prenda.id for prenda in self.prendas])
        for i, prenda in enumerate(self.prendas):
            if(prenda.id in prendas):
                incompatibilidades = self.incompatibilidades.get(prenda.id, set())
                compatibles = prendas.difference(incompatibilidades)
                self.combinaciones[i] = set()
                self.combinaciones[i] = self.combinaciones[i].union({prenda.id})
                self.combinaciones[i] = self.combinaciones[i].union(compatibles)
                prendas = prendas.difference(compatibles)
                prendas = prendas.difference({prenda.id})


    def combinaciones_optimas(self):
        self._obtener_combinaciones_de_lavados()
    
    def print_combinaciones(self):
        for i, combinacion in enumerate(self.combinaciones.keys()):
            prendas = self.combinaciones[combinacion]
            for prenda in prendas:
                print(prenda, i)
