import itertools

class Lavanderia2:
    
    def __init__(self):
        self.prendas = {}
        self.incompatibilidades = {}
        self.combinaciones = {}
        
    def __contains__(self, prenda):
        return prenda.id in [prenda.id for prenda in self.prendas] 

    def guardar_incompatibilidad(self, prenda, prenda_incompatible):
        if prenda not in self.incompatibilidades:
            self.incompatibilidades[prenda] = set()
        self.incompatibilidades[prenda].add(prenda_incompatible)
        
    def _obtener_combinaciones_de_lavados(self):
        prendas = list(self.prendas.values())
        prendas.sort(key=lambda prenda: prenda.tiempo_lavado, reverse=True)
        prendas_set = set(prendas)
        for i, prenda in enumerate(prendas):
            if(prenda in prendas_set):
                incompatibilidades = self.incompatibilidades.get(prenda.id, set())
                compatibles = prendas_set.difference(incompatibilidades)
                compatibles_list = list(compatibles)
                compatibles_list.sort(key=lambda prenda: prenda.tiempo_lavado, reverse=True)
                for compatible in compatibles_list:
                    if((compatible in compatibles) and (prenda not in self.incompatibilidades[compatible])):
                        compatibles = compatibles.difference(self.incompatibilidades[compatible])
                    elif ((prenda in self.incompatibilidades[compatible]) and (compatible in compatibles)):
                        compatibles.remove(compatible)
                self.combinaciones[i] = set()
                self.combinaciones[i] = self.combinaciones[i].union({prenda})
                self.combinaciones[i] = self.combinaciones[i].union(compatibles)
                prendas_set = prendas_set.difference(compatibles)
                prendas_set = prendas_set.difference({prenda})


    def combinaciones_optimas(self):
        self._obtener_combinaciones_de_lavados()
    
    def print_combinaciones(self):
        prenda_id = []
        for key in self.combinaciones.keys():
            prendas = self.combinaciones[key]
            for prenda in prendas:
                if(not prenda in prenda_id):
                    prenda_id.append(prenda)
                    print(prenda, key)
