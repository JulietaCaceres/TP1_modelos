import itertools

class Lavanderia:
    
    def __init__(self):
        self.prendas = []
        self.incompatibilidades = {}
        self.combinaciones = []
        
    def __contains__(self, prenda):
        return prenda.id in [prenda.id for prenda in self.prendas] 

    def guardar_incompatibilidad(self, prenda, prenda_incompatible):
        if prenda not in self.incompatibilidades:
            self.incompatibilidades[prenda] = []
        self.incompatibilidades[prenda].append(prenda_incompatible)
        
    def _obtener_combinaciones_de_lavados(self):
        for L in range(0, len(self.prendas)+1):
            for subnet in itertools.combinations(self.prendas, L):
                prendas = set(subnet) 
            #{} if len(combinacion_de_prendas) == 0 else {prenda for prenda in combinacion_de_prendas[0]}
                incompatibilidades = set()
            
                for prenda in prendas:
                    incompatibilidades.update(set(self.incompatibilidades.get(prenda.id, [])))
                prendas_id = set([prenda.id for prenda in list(prendas)])
                if (not prendas_id.intersection(incompatibilidades)):
                    self.combinaciones.append(subnet)
         
    def _ordenar_combinaciones_por_tiempo_y_cantidad(self):
        self.combinaciones = sorted(self.combinaciones, key=lambda x:  (len(x),0 if len(x)==0 else max([prenda.tiempo_lavado for prenda in x])) , reverse=True)

    def _obtener_combinacion_optima(self):
        self._ordenar_combinaciones_por_tiempo_y_cantidad()
        combinacion_optima = []
        prendas = set()
        for combinacion in self.combinaciones:
            combinacion_ids = set([prenda.id for prenda in list(combinacion)])
            prendas_id = set([prenda.id for prenda in list(prendas)])
            if (len(prendas_id.intersection(combinacion_ids))==0):
                prendas.update(combinacion)
                combinacion_optima.append(combinacion)
        print("Combinacion Optima: ", combinacion_optima)
        tiempos_optimos = []
        tiempo_total = 0
        for tupla in combinacion_optima:
            tiempos = [prenda.tiempo_lavado for prenda in tupla]
            tiempos_optimos.append(0 if len(tiempos) == 0 else max(tiempos))
            tiempo_total += 0 if len(tiempos) == 0 else max(tiempos)
        print("Tiempos_optimos: ", tiempos_optimos)
        print("Tiempo total: ", tiempo_total)
        for i, combinacion_optima in enumerate(combinacion_optima):
            for prenda in combinacion_optima:
                print(prenda.id, i+1)            

        
                
            
    def combinaciones_optimas(self):
        self._obtener_combinaciones_de_lavados()
        #self._descartar_incompatibilidades()
        self._obtener_combinacion_optima() 
    
    def print_combinaciones(self):
        print(self.combinaciones)