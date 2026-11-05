import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 7000

# Dicionário que guardará o estado: {'Worker_1': 1698765432.10, 'Worker_2': ...}
nos_ativos = {}

def checar_status():
    # verifica quem parou de mandar sinal
    while True:

        tempo_atual = time.time()
        
        # Transformamos em lista para poder deletar itens do dicionário com segurança
        for worker_id in list(nos_ativos.keys()):

            ultimo_sinal = nos_ativos[worker_id]
            
            if tempo_atual - ultimo_sinal > 8:
                print(f"\n[ALERTA] O Nó {worker_id} está OFFLINE!")
                # Deleta o nó do registro para não repetir o alerta infinitamente
                del nos_ativos[worker_id]
                
        # Pausa a checagem por 2 segundos antes de varrer a lista de novo
        time.sleep(2)

def start_monitor():

    servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    servidor.bind((HOST, PORT))
    
    print(f"[INICIANDO] Monitor de Heartbeat rodando em {HOST}:{PORT}")
    
    threading.Thread(target=checar_status, daemon=True).start()
    
    while True:
        try:
            # Recebe o pacote (até 1024 bytes) e o endereço de quem mandou
            mensagem_bytes, endereco = servidor.recvfrom(1024)
            mensagem = mensagem_bytes.decode('utf-8')
            
            # A mensagem esperada é algo como "PING Worker_1"
            if mensagem.startswith("PING"):
                # Separa a string pelo espaço e pega a segunda parte (o ID)
                worker_id = mensagem.split(" ")[1]
                
                # Atualiza/Registra o momento exato em que esse Worker deu sinal
                nos_ativos[worker_id] = time.time()
                print(f"[RECEBIDO] Heartbeat de {worker_id}")
                
        except Exception as e:
            print(f"[ERRO] Falha ao processar pacote: {e}")

if __name__ == "__main__":
    start_monitor()