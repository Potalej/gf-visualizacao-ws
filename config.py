import json

def ler_config (arquivo:str):
    with open(arquivo, 'r') as arq:
        json_obj = json.load(arq)
    return json_obj

configs = ler_config('config.json')