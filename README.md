# Descrição da Atividade de Sistemas Distribuídos

1) Implementar em Python o modelo cliente/servidor com sockets. 

a) O servidor deve atender um único pedido do cliente: Retornar o horário do momento solicitado. O cliente deve solicitar o horário ao servidor e encerrar. O servidor deve ser multithread. 

b) O servidor deve escutar em uma porta específica (ex: 8000). Quando recebe uma string, ele a reverte e a envia de volta. O cliente que se conecta ao servidor, envia uma string ("Olá, Mundo Distribuído") e espera a resposta. 

2) Implementar em Python o modelo cliente/servidor com RPyC (Remote Python Call). O servidor deve atender um único pedido do cliente: Retornar o horário do momento solicitado. O cliente deve solicitar o horário ao servidor e encerrar.

3) Desenvolver uma aplicação de chat em tempo real utilizando a arquitetura Cliente-Servidor, explorando a comunicação entre processos via sockets e o tratamento de concorrência por meio de threads.


# Detalhes de Execução

Para visualização da dinâmica cliente/servidor com os sockets é necessário executar primeiro os arquivos de servidor e somente depois executar os arquivos de cliente (que deve ser executado em terminal separado)

Arquivos de código para cada questão:

1)  a) **cliente_a** e **servidor_a**
    b) **cliente_b** e **servidor_b**

2) **cliente_rpc** e **servidor_rpc**

3) **cliente_chat** e **servidor_chat**
