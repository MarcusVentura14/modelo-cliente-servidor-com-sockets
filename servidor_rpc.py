import rpyc
from rpyc.utils.server import ThreadedServer
from datetime import datetime

class ServicoHorario(rpyc.Service):
    def on_connect(self, conection):
        print("[CONEXÃO] Novo cliente conectado.")

    def on_disconnect(self, conection):
        print("[DESCONEXÃO] Cliente desconectado.\n")

    def exposed_obter_horario(self):
        print("[REQUISIÇÃO] Cliente solicitou o horário.")
        agora = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return agora

def start_server():
    porta = 12345
    # ThreadedServer já cuida da fila e da criação de threads para cada cliente
    server = ThreadedServer(ServicoHorario, port=porta)
    print(f"[INICIANDO] Servidor RPC rodando na porta {porta}...")
    server.start()

if __name__ == "__main__":
    start_server()