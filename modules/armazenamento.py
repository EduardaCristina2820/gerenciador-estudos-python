import json

CAMINHO_DADOS = "dados.json"


def carregar_dados():
    """
    Lê o arquivo JSON e devolve um dicionário Python.
    Se o arquivo não existir ou estiver vazio, cria uma estrutura padrão.
    """
    try:
        with open(CAMINHO_DADOS, "r", encoding="utf-8") as arquivo: # Abre o arquivo em formato de leitura
            return json.load(arquivo) # Lê o JSON e transforma em dicionário Python
    except FileNotFoundError:
        return {"materias": {}}
    except json.JSONDecodeError:
        return {"materias": {}}


def salvar_dados(dados):
    """
    Recebe um dicionário Python e grava no arquivo JSON.
    """
    with open(CAMINHO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(dados, arquivo, indent=4, ensure_ascii=False)  # Dump grava o dicionário como JSON no arquivo
