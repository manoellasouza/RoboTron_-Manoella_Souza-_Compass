#a) Crie uma “aplicação” em loop que tenha uma opção para listar todos os elementos da tabela, porém mostrando apenas uma propriedade do elemento. 

import pandas as pd
arquivo = pd.read_csv("elementos.csv", encoding="UTF-8", sep=",")
res=()

def menu():
    print("--------------------------")
    print("Propriedades dos Elementos")
    print("--------------------------")
    print("1) Símbolo       4) Linha")
    print("2) Nome          5) Coluna")
    print("3) Nº Atômico    6) Estado")
    print(" ")

while res != 0: 
    menu()
    res=(int(input("Digite o número da propriedade desejada para listar os elementos\nou digite 0 para sair: ")))
    print(" ")
    if res == 1:
        print(arquivo["Simbolo"]) 
    elif res == 2: 
        print(arquivo["Nome"])
    elif res == 3:
        print(arquivo["NumeroAtomico"])
    elif res == 4:
        print(arquivo["Linha"])
    elif res == 5:
        print(arquivo["Coluna"])
    elif res == 6:
        print(arquivo["EstadoFisico"])
    print(" ")
    if res == 0:
        print("Obrigada por usar a aplicação!")