# server.py
import socket
import threading
from datetime import datetime

# Configurações do servidor
HOST = '127.0.0.1'  # Endereço local
PORT = 12345        # Porta de comunicação

def handle_client(client_socket, address):
    """Função executada em uma thread separada para cada cliente."""
    print(f"[NOVA CONEXÃO] Cliente {address} conectado.")
    try:
        # Aguarda a solicitação do cliente
        request = client_socket.recv(1024).decode('utf-8')
        
        if request.strip().upper() == 'HORA':
            # Captura o horário atual e envia ao cliente
            agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
            client_socket.send(agora.encode('utf-8'))
            print(f"[ENVIADO] Horário enviado para {address}.")
    except Exception as e:
        print(f"[ERRO] Problema na conexão com {address}: {e}")
    finally:
        # Encerra a conexão com este cliente específico
        client_socket.close()
        print(f"[DESCONECTADO] Cliente {address} desconectado.\n")

def start_server():
    # Cria o socket do servidor (IPv4, TCP)
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    
    # Coloca o servidor em modo de escuta
    server.listen(5)
    print(f"[INICIANDO] Servidor escutando em {HOST}:{PORT}")
    
    while True:
        # Aceita uma nova conexão
        client_socket, address = server.accept()
        
        # Cria e inicia uma nova thread para o cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        
        # Exibe o número de threads ativas (descontando a thread principal)
        print(f"[THREADS ATIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()