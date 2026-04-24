import time
from datetime import datetime
from modules.armazenamento import carregar_dados, salvar_dados


def iniciar_cronometro():
    dados = carregar_dados()
    materias = dados["materias"]

    if not materias:
        print("Nenhuma matéria cadastrada ainda.")
        return

    print("\nMatérias disponíveis:")
    for i, materia in enumerate(materias.keys(), start=1): # Retorna todas as chaves do dicionario enumeradas a partir do 1 
        print(f"{i}. {materia}")

    try:
        escolha = int(input("\nEscolha o número da matéria: "))
    except ValueError:
        print("Entrada inválida.")
        return

    if escolha < 1 or escolha > len(materias):
        print("Número fora do intervalo.")
        return

    nome_materia = list(materias.keys())[escolha - 1] # Pega o nome da matéria escolhida

    input(f"\nPressione ENTER para iniciar o estudo de {nome_materia}...")
    inicio = time.time()  # Hora atual em segundos

    input("Pressione ENTER para finalizar o estudo...")
    fim = time.time()

    duracao_segundos = fim - inicio
    duracao_minutos = int(duracao_segundos // 60)

    agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # Armazena data e hora atual formatada

    sessao = {
        "data": agora,
        "duracao_minutos": duracao_minutos,
        "tipo": "cronometro"
    }

    materias[nome_materia]["tempo_total_minutos"] += duracao_minutos
    materias[nome_materia]["sessoes"].append(sessao)

    salvar_dados(dados)

    print(f"\nSessão registrada! Tempo estudado: {duracao_minutos} minutos.\n")
