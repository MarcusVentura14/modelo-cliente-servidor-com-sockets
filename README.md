# Descrição da Atividade de Sistemas Distribuídos

1) Implementar em Python o modelo cliente/servidor com sockets. 

a) O servidor deve atender um único pedido do cliente: Retornar o horário do momento solicitado. O cliente deve solicitar o horário ao servidor e encerrar. O servidor deve ser multithread. 

b) O servidor deve escutar em uma porta específica (ex: 8000). Quando recebe uma string, ele a reverte e a envia de volta. O cliente que se conecta ao servidor, envia uma string ("Olá, Mundo Distribuído") e espera a resposta. 

2) Implementar em Python o modelo cliente/servidor com RPyC (Remote Python Call). O servidor deve atender um único pedido do cliente: Retornar o horário do momento solicitado. O cliente deve solicitar o horário ao servidor e encerrar.

3) Desenvolver uma aplicação de chat em tempo real utilizando a arquitetura Cliente-Servidor, explorando a comunicação entre processos via sockets e o tratamento de concorrência por meio de threads.

4) Implementar um monitor de Heartbeat com sockets. 

a) Worker (Cliente que envia sinais): Um script que roda em loop enviando a cada 3 segundos uma mensagem de Heartbeat ("PING" + ID do Nó) para o Servidor Monitor. Pode ser executado em várias janelas de terminal simulando nós diferentes na rede (ex: Worker_1, Worker_2).

b) Servidor Monitor: Mantém um registro do último instante em que recebeu o sinal de cada Worker.Possui uma thread de checagem que roda periodicamente. Se um Worker ficar mais de 8 segundos sem enviar o sinal de Heartbeat, o servidor deve exibir no terminal: [ALERTA] O Nó Worker_X está OFFLINE!.

5) Desenvolver uma aplicação que utilize o conceito de estado compartilhado. A aplicação pode ser um sistema de reserva de assentos (ex: restaurante, cinema, ônibus, avião, etc).

**Servidor (RPyC):**
- Deve manter uma estrutura de dados na memória (ex: um dicionário ou lista) representando os assentos disponíveis (ex: de A1 a A10).
- Métodos expostos (*exposed_*):
- *exposed_listar_assentos()*: Retorna o status atual de cada assento (Livre / Reservado).
- *exposed_reservar_assento(nome_cliente, assento)*: Tenta reservar o assento desejado.
- **Controle de Concorrência**: Garantir que se dois clientes tentarem reservar o mesmo assento simultaneamente, apenas um receba a confirmação de sucesso e o outro receba um aviso de "Assento já ocupado".
**Cliente (RPyC):**
- Comando simples que se conecta ao servidor RPyC.
- Permite visualizar o mapa de assentos e enviar solicitações de reserva repetidas até o usuário decidir sair.


# Detalhes de Execução

Para visualização da dinâmica cliente/servidor com os sockets é necessário executar primeiro os arquivos de servidor e somente depois executar os arquivos de cliente (que deve ser executado em terminal separado)

Arquivos de código para cada questão:

1) 

a) **cliente_a** e **servidor_a** 

b) **cliente_b** e **servidor_b**

2) **cliente_rpc** e **servidor_rpc**

3) **cliente_chat** e **servidor_chat**

4) **cliente_heartbeat** e **servidor_heartbeat**

5) **cliente_rpyc** e **servidor_rpyc**
