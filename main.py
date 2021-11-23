import pandas as pd
from Lavanderia2 import Lavanderia2
from prendas import Prenda

if __name__=="__main__":
    prendas = []
    lavanderia = Lavanderia2()
    data = pd.read_csv("https://modelosuno.okapii.com/Problemas/segundo_problema.txt", delimiter=" ", skiprows=11, header=None)

    for row in data.values:
        if 'e' == row[0]:
            lavanderia.guardar_incompatibilidad(row[1], row[2])
        elif 'n' == row[0]:
            prenda = Prenda(row[1], row[2])
            prendas.append(prenda)
        
    lavanderia.prendas.extend(prendas)   
    lavanderia.combinaciones_optimas()
    lavanderia.print_combinaciones()