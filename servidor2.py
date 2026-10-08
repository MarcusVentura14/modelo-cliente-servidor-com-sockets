# servidor_reverso.py
import socket
import threading

# Configurações do servidor
HOST = '127.0.0.1'
PORT = 8000        # Nova porta especificada na atividade

def handle_client(client_socket, address):
    """Função executada em uma thread separada para cada cliente."""
    print(f"[NOVA CONEXÃO] Cliente {address} conectado.")
    try:
        # Aguarda a string do cliente
        # Recebe até 1024 bytes e converte para texto
        mensagem_recebida = client_socket.recv(1024).decode('utf-8')
        
        if mensagem_recebida:
            print(f"[RECEBIDO] De {address}: '{mensagem_recebida}'")
            
            # Reverte a string em Python usando fatiamento (slicing) [::-1]
            mensagem_revertida = mensagem_recebida[::-1]
            
            # Envia a string revertida de volta ao cliente
            client_socket.send(mensagem_revertida.encode('utf-8'))
            print(f"[ENVIADO] Para {address}: '{mensagem_revertida}'")
            
    except Exception as e:
        print(f"[ERRO] Problema na conexão com {address}: {e}")
    finally:
        # Encerra a conexão
        client_socket.close()
        print(f"[DESCONECTADO] Cliente {address} desconectado.\n")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    
    server.listen(5)
    print(f"[INICIANDO] Servidor de Reversão escutando em {HOST}:{PORT}")
    
    while True:
        client_socket, address = server.accept()
        
        # Cria a thread para lidar com o novo cliente
        client_thread = threading.Thread(target=handle_client, args=(client_socket, address))
        client_thread.start()
        print(f"[THREADS ATIVAS] {threading.active_count() - 1}")

if __name__ == "__main__":
    start_server()