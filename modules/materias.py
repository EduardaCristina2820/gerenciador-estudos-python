from modules.armazenamento import carregar_dados, salvar_dados


def cadastrar_materia():
    dados = carregar_dados()

    nome = input("Digite o nome da matéria: ").strip()  # Remove espaços extras

    if nome == "":
        print("O nome da matéria não pode ser vazio.")
        return

    if nome in dados["materias"]:
        print("Essa matéria já está cadastrada.")
        return

    try:
        horas = int(input("Digite a meta semanal (horas): "))
        minutos = int(input("Digite a meta semanal (minutos): "))
    except ValueError:
        print("Por favor, digite números válidos.")
        return

    if horas < 0 or minutos < 0 or minutos >= 60:
        print("Horas devem ser >= 0 e minutos entre 0 e 59.")
        return

    dados["materias"][nome] = {     # Cria uma nova chave no dicionário 
        "meta_horas": horas,
        "meta_minutos": minutos,
        "tempo_total_minutos": 0,
        "sessoes": []
    }

    salvar_dados(dados)
    print(f"Matéria '{nome}' cadastrada com sucesso!")
