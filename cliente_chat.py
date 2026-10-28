import socket
import threading
import sys

HOST = '127.0.0.1'
PORT = 5555

def receber_mensagens(cliente):
    while True:
        try:
            mensagem = cliente.recv(1024).decode('utf-8')
            if mensagem:
                print(f"\n{mensagem}")
            else:
                break
        except:
            print("\n[ERRO] Conexão com o servidor perdida.")
            cliente.close()
            break

def start_client():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        cliente.connect((HOST, PORT))
        
        nome = input("Digite o seu nome para entrar no chat: ")
        
        # Avisa ao servidor (e aos outros) que entrou
        msg_entrada = f"--- {nome} entrou no chat! ---"
        cliente.send(msg_entrada.encode('utf-8'))
        
        # Inicia a thread que fica escutando as mensagens do servidor
        thread_receber = threading.Thread(target=receber_mensagens, args=(cliente,), daemon=True)
        thread_receber.start()
        
        print("[CONECTADO] Você pode começar a digitar (digite 'sair' para fechar).\n")
        
        # Loop principal (fica aguardando o usuário digitar)
        while True:
            mensagem_input = input()
            
            if mensagem_input.lower() == 'sair':
                msg_saida = f"--- {nome} saiu do chat. ---"
                cliente.send(msg_saida.encode('utf-8'))
                break
            
            # Formata a mensagem com o nome antes de enviar
            mensagem_formatada = f"[{nome}]: {mensagem_input}"
            cliente.send(mensagem_formatada.encode('utf-8'))
            
    except ConnectionRefusedError:
        print("[ERRO] O servidor não foi encontrado.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")
    finally:
        cliente.close()
        sys.exit()

if __name__ == "__main__":
    start_client()