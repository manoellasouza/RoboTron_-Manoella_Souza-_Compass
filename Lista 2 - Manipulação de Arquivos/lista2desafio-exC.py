# C) Listar todos os dados de todos os elementos inseridos.

import pandas as pd

arquivo = pd.read_csv("elementos.csv", encoding="UTF-8", sep=",")

print(arquivo)