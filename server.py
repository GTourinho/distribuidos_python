from socket import *

class Server:
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.bind(('127.0.0.1',9000))
        self.clients = {}
        
    def listen(self):
        self.socket.listen(5)
        (client, dummy) = self.socket.accept()
        packet = client.recv(50).decode()
        
        if packet[:3] == 'id_':
            self.clients[packet[3:]] = 0
            print('id do cliente:', packet[3:])
        elif packet[0] == '1':
            id, quantia = packet[1:].split('.')

            if abs(int(quantia)) > self.clients[id]:
                msg = '0' #quantia_insuficiente
                client.sendall(msg.encode())
            else:
                msg = '1' #quantia_suficiente
                client.sendall(msg.encode())
                self.clients[id] -= abs(int(quantia))

        elif packet[0] == '2':
            id, quantia = packet[1:].split('.')
            self.clients[id] += abs(int(quantia))
            
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
                
            
        elif packet[0] == '4':
            client.sendall(str(self.clients[packet[1:]]).encode())
            
        client.close()

server = Server()

while True:
    server.listen()
