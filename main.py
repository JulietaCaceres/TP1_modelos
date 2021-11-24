import pandas as pd
from Lavanderia2 import Lavanderia2
from prendas import Prenda

if __name__=="__main__":
    prendas = []
    lavanderia = Lavanderia2()
    data = pd.read_csv("https://modelosuno.okapii.com/Problemas/segundo_problema.txt", delimiter=" ", skiprows=11, header=None)
    for row in data.values:
        if 'e' == row[0]:
            prenda1 = Prenda(row[1])
            prenda2 = Prenda(row[2])
            lavanderia.prendas[row[1]] = prenda1
            lavanderia.prendas[row[2]] = prenda2
            lavanderia.guardar_incompatibilidad(prenda1, prenda2)
            lavanderia.guardar_incompatibilidad(prenda2, prenda1)
        elif 'n' == row[0]:
            lavanderia.prendas[row[1]].tiempo_lavado = row[2]
    lavanderia.combinaciones_optimas()
    lavanderia.print_combinaciones()