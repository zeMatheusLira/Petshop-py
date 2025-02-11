import json
import os

def carregar_dados(arquivo):
    if not os.path.exists("dados"):
        os.makedirs("dados")
    caminho = os.path.join("dados", arquivo)
    try:
        with open(caminho, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_dados(arquivo, dados):
    caminho = os.path.join("dados", arquivo)
    with open(caminho, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)