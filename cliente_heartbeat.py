import socket
import time

HOST = '127.0.0.1'
PORT = 7000

def start_worker():

    worker_id = input("Digite o ID deste Worker (ex: Worker_1): ")

    cliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    print(f"\n[ATIVO] {worker_id} enviando sinais de Heartbeat a cada 3 segundos...")
    print("(Pressione Ctrl+C para desligar e simular uma falha)\n")
    
    try:
        while True:
            mensagem = f"PING {worker_id}"
            
            # No UDP usamos sendto(), informando a mensagem e o destino de uma vez
            cliente.sendto(mensagem.encode('utf-8'), (HOST, PORT))
            
            print(f"[ENVIADO] {mensagem}")
            
            # Aguarda 3 segundos antes do próximo sinal de heartbeat
            time.sleep(3)
            
    except KeyboardInterrupt:
        print(f"\n[ENCERRADO] {worker_id} foi desligado manualmente.")
    finally:
        cliente.close()

if __name__ == "__main__":
    start_worker()