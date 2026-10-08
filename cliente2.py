# cliente_reverso.py
import socket

# Configurações de conexão (devem corresponder ao servidor)
HOST = '127.0.0.1'
PORT = 8000

def start_client():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((HOST, PORT))
        
        # A string solicitada na atividade
        mensagem = "Olá, Mundo Distribuído"
        print(f"ENVIANDO: '{mensagem}'")
        
        # Envia a string em formato de bytes
        client.send(mensagem.encode('utf-8'))
        
        # Aguarda a resposta do servidor
        resposta = client.recv(1024).decode('utf-8')
        
        print(f"RESPOSTA DO SERVIDOR: '{resposta}'")
        
    except ConnectionRefusedError:
        print("[ERRO] A conexão foi recusada. Verifique se o servidor está rodando na porta 8000.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")
    finally:
        client.close()

if __name__ == "__main__":
    start_client()