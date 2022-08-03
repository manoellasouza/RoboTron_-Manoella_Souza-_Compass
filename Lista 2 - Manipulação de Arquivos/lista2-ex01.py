# 1- Baixe o arquivo do link JSON 1, abra ele no vsCode com Python nomeando-o como partida guarde em uma variável e printe o JSON inteiro no terminal.

import json

def retornar_json():
    with open ("partida.json", encoding="utf-8") as json_normal:
        #o load vai carregar o JSON normal e transformar ele em dict:
        json_manipulavel = json.load(json_normal)
        return json_manipulavel
    
json_retornado = retornar_json()

partida=json_retornado
print(partida)
