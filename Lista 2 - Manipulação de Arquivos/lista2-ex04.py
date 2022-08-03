#4- No JSON 1 printe todas as chaves e valores do time visitante

import json

def retornar_json():
    with open ("partida.json", encoding="utf-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel

json_retornado = retornar_json()
print(json_retornado["copa-do-brasil"][0]["time_visitante"])