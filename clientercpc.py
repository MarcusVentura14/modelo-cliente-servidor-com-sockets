import rpyc

HOST = '127.0.0.1'
PORTA = 12345

def start_client():
    try:
        conection = rpyc.connect(HOST, PORTA)
        resposta = conection.root.obter_horario()
        print(f"RESPOSTA DO SERVIDOR: O horário atual é {resposta}")
        
    except ConnectionRefusedError:
        print("[ERRO] Conexão recusada. O servidor está rodando?")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")
    finally:
        # Encerra a conexão conforme solicitado
        if 'conection' in locals():
            conection.close()

if __name__ == "__main__":
    start_client()