import socket
import threading

HOST = '127.0.0.1'
PORT = 5555

# Lista para armazenar as conexões de todos os clientes ativos
clientes = []

def broadcast(mensagem, cliente_remetente):
    for cliente in clientes:
        if cliente != cliente_remetente:
            try:
                cliente.send(mensagem)
            except:
                # Se der erro ao enviara mensagem, assume que o cliente caiu e remove da lista
                cliente.close()
                if cliente in clientes:
                    clientes.remove(cliente)

def handle_client(cliente, endereco):
    print(f"[NOVA CONEXÃO] {endereco} conectado.")
    while True:
        try:
            # Fica aguardando mensagens deste cliente
            mensagem = cliente.recv(1024)
            if mensagem:
                # Se recebeu algo, espalha para os outros
                print(f"[{endereco}] enviou uma mensagem.")
                broadcast(mensagem, cliente)
            else:
                break
        except:
            break
    
    # Se sair do loop, o cliente desconectou. Removemos e fechamos.
    if cliente in clientes:
        clientes.remove(cliente)
    cliente.close()
    print(f"[DESCONECTADO] {endereco} saiu do chat.")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"[INICIANDO] Servidor de Chat rodando em {HOST}:{PORT}")
    
    while True:
        # Aceita novos clientes
        cliente, endereco = server.accept()
        
        # Adiciona o novo cliente à lista de transmissão
        clientes.append(cliente)
        
        # Cria uma thread para ouvir esse cliente
        thread = threading.Thread(target=handle_client, args=(cliente, endereco))
        thread.start()

if __name__ == "__main__":
    start_server()