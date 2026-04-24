def mostrar_menu():
    print("=== Gerenciador de Estudos ===")
    print("1. Cadastrar matéria")
    print("2. Iniciar estudo com cronômetro")
    print("3. Iniciar sessão de pomodoro")
    print("4. Ver progresso por matéria")
    print("5. Gerar relatório semanal")
    print("0. Sair\n")
    
from modules.materias import cadastrar_materia
from modules.sessoes import iniciar_cronometro
def main():
    while True:
        mostrar_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_materia()
            
        elif opcao == "2":
            iniciar_cronometro()
        
        elif opcao == "3":
            print("Sessão pomodoro (em breve)")
        
        elif opcao == "4":
            print ("Progresso por matéria (em breve)")
            
        elif opcao == "5":
            print("Relatório semanal (em breve)")
            
        elif opcao == "0":
            print("Saindo do programa. Até mais :) ")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()