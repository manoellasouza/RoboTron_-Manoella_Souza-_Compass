# 3- Do JSON 1 Guarde apenas o Nome do Estádio, o Placar e o Status do jogo dentro de variáveis e mostre-as.

import json

def retornar_json():
    with open ("partida.json", encoding="utf-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

json_retornado = retornar_json()

estadio= json_retornado["copa-do-brasil"][0]["estadio"]["nome_popular"]
print(estadio)

placar= json_retornado["copa-do-brasil"][0]["placar"]
print(placar)

status= json_retornado["copa-do-brasil"][0]["status"]
print(status)

