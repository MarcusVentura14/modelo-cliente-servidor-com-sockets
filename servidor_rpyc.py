import rpyc
from rpyc.utils.server import ThreadedServer
import threading

assentos = {f"A{i}": "Livre" for i in range(1, 11)} # Gera assentos de A1 até A10

# O Lock é para garantir que apenas uma thread possa modificar os assentos por vez
lock_reserva = threading.Lock()

class ServicoReserva(rpyc.Service):
    
    def exposed_listar_assentos(self):
        return assentos.copy()

    def exposed_reservar_assento(self, nome_cliente, assento_desejado):
       
        assento = assento_desejado.upper()

        if assento not in assentos:
            return False, "Assento inexistente. Escolha de A1 a A10."

        with lock_reserva:
            if assentos[assento] == "Livre":
                assentos[assento] = nome_cliente
                return True, f"Sucesso! Assento {assento} reservado para {nome_cliente}."
            else:
                dono_atual = assentos[assento]
                return False, f"Falha. O assento {assento} já está ocupado por {dono_atual}."
        # O 'with lock' libera o cadeado automaticamente ao sair do bloco

def start_server():
    porta = 12345
    server = ThreadedServer(ServicoReserva, port=porta, protocol_config={"allow_public_attrs": True})
    print(f"[INICIANDO] Servidor de Reservas rodando na porta {porta}...")
    server.start()

if __name__ == "__main__":
    start_server()