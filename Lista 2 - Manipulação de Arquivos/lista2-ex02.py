#2- Pegue o arquivo JSON 1 e printe apenas o nome do time vencedor no terminal.
# O colega Paulo me deu a dica de colocar o [0] para poder printar o json em seguida

import json

def retornar_json():
    with open ("partida.json", encoding="utf-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

json_retornado = retornar_json()
partida= json_retornado["copa-do-brasil"][0]

mandante= (partida["placar_mandante"])
visitante= (partida["placar_visitante"])
 
if mandante > visitante:
    print("Vencedor da partida:",partida["time_mandante"]["nome_popular"])
elif visitante > mandante:
    print("Vencedor da partida:",partida["time_visitante"]["nome_popular"])
else:
    print("A partida terminou empatada!")
