# client.py
import socket

# Configurações de conexão (devem bater com o servidor)
HOST = '127.0.0.1'
PORT = 12345

def start_client():
    # Cria o socket do cliente (IPv4, TCP)
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # Conecta ao servidor
        client.connect((HOST, PORT))
        
        # Envia a solicitação de horário
        solicitacao = "HORA"
        client.send(solicitacao.encode('utf-8'))
        
        # Aguarda e recebe a resposta (tamanho do buffer de 1024 bytes)
        resposta = client.recv(1024).decode('utf-8')
        print(f"RESPOSTA DO SERVIDOR: O horário atual é {resposta}")
        
    except ConnectionRefusedError:
        print("[ERRO] A conexão foi recusada. Verifique se o servidor está rodando.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")
    finally:
        # O cliente encerra a conexão conforme o requisito
        client.close()

if __name__ == "__main__":
    start_client()