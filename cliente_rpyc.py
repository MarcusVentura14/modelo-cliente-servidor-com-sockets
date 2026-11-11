import rpyc
import sys

HOST = '127.0.0.1'
PORTA = 12345

def start_client():
    try:
        # Estabelece conexão RPC
        conn = rpyc.connect(HOST, PORTA)
        
        print("=== BEM-VINDO AO SISTEMA DE RESERVAS ===")
        nome = input("Por favor, digite o seu nome: ")
        
        while True:
            print("\n--- MENU ---")
            print("1. Visualizar Mapa de Assentos")
            print("2. Reservar um Assento")
            print("3. Sair")
            
            opcao = input("Escolha uma opção 1,2 ou 3: ")
            
            if opcao == '1':
                # Chama o método remoto listar_assentos
                mapa = conn.root.listar_assentos()
                print("\n--- STATUS DOS ASSENTOS ---")
                for assento, status in mapa.items():
                    print(f"[{assento}] : {status}")
                    
            elif opcao == '2':
                assento = input("\nDigite o número do assento que deseja (ex: A1): ")
                # Chama o método remoto reservar_assento
                sucesso, mensagem = conn.root.reservar_assento(nome, assento)
                
                # Exibe o resultado da tentativa
                if sucesso:
                    print(f"{mensagem}")
                else:
                    print(f"{mensagem}")
                    
            elif opcao == '3':
                print("Saindo do sistema. Até logo!")
                break
            else:
                print("Opção inválida.")
                
    except ConnectionRefusedError:
        print("[ERRO] Não foi possível conectar. O servidor está rodando?")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    start_client()