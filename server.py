from socket import *

# Definições da classe do servidor.
# Importamos bibliotecas de socket para podermos simular as operações de maneira 
# mais real dentro da rede.
# Estaremos definindo endereços padrões, para não causarmos conflitos etc.

class Server:
    # Essa é a função de inicalização, onde definimos os valores padrões
    # para o nosso socket.
    # Além disso, inicalizamos um array para armazenarmos os dados
    # dos possíveis clientes.
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('127.0.0.1',9000))
        self.clients = {}
        
    # Operação de escuta, onde aguardamos e tratamos solicitações por
    # parte do cliente, a partir dos pacotes.
    def listen(self):
        self.socket.listen(5)
        (client, dummy) = self.socket.accept()
        packet = client.recv(50).decode()
        
        # Tratamento que fazemos para o primeiro momento de cadastro,
        # onde recebemos a informação do cliente, guardando o seu id
        # e inicalizando o seu saldo zerado.
        # Em todas as opções seguintes, observamos a requisição a partir do
        # caractere '.' ; o que acontece é que separamos valores e flags, 
        # entre pontos " . " para sabermos o que é ID e o que é valor.
        if packet[:3] == 'id_':
            self.clients[packet[3:]] = 0
            print('id do cliente:', packet[3:])
        
        # Opção de saque, retorna mensagem de sucesso ou falha (0 ou 1)
        elif packet[0] == '1':
            id, quantia = packet[1:].split('.')

            if abs(int(quantia)) > self.clients[id]:
                msg = '0' #quantia_insuficiente
                client.sendall(msg.encode())
            else:
                msg = '1' #quantia_suficiente
                client.sendall(msg.encode())
                self.clients[id] -= abs(int(quantia))

        # Opção de depósito, onde somente adicionamos quantia ao cliente,
        # sem retorno.
        elif packet[0] == '2':
            id, quantia = packet[1:].split('.')
            self.clients[id] += abs(int(quantia))

        # Opção de transferência, retorna mensagem de sucesso ou falha, pois
        # além de checar o saldo, verifica a existência do destinatário no
        # sistema. Caso tudo esteja de acordo, realizamos as operações
        # matemáticas.
        elif packet[0] == '3':
            id, id2, quantia = packet[1:].split('.')
            if abs(int(quantia)) > self.clients[id]:
                msg = '0' #quantia_insuficiente
                client.sendall(msg.encode())
            elif id2 not in self.clients:
                msg = '1' #destinatario_invalido
                client.sendall(msg.encode())
            else:
                msg = '2' #quantia_suficiente
                self.clients[id] -= abs(int(quantia))
                self.clients[id2] += abs(int(quantia))
                client.sendall(msg.encode())
                
        # Opção de saldo, retorna o valor do cliente específico.
        elif packet[0] == '4':
            client.sendall(str(self.clients[packet[1:]]).encode())
            
        client.close()

server = Server()

while True:
    server.listen()
