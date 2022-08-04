# 13- Crie mais uma coluna em tempo de execução juntando os dados movie e year.
# O colega Pedro me deu a dica de colocar o .map(str) para concatenar sem desconfigurar a lista ao dar o print

import pandas as pd

arquivo = pd.read_csv("ganhadoresoscar.csv", encoding="UTF-8", sep=",")

arquivo["Movie_Year"] = arquivo["Movie"] + " " + arquivo["Year"].map(str)
print(arquivo["Movie_Year"])
