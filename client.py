from socket import *
import sys

class Client:
    
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('127.0.0.1',9000))
        print('Digite o seu primeiro nome e RG (Ex: Joao 123)')
        self.id = input().replace(' ', '')
        msg = 'id_' + self.id
        self.socket.send(msg.encode())
        self.socket.close()

    def connect(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('127.0.0.1',9000))
        
    def sendmsg(self):
        print('Digite o número de acordo com a opção que deseja:')
        print('1: Saque')
        print('2: Depósito')
        print('3: Transferência')
        print('4: Saldo')
        print('5: Sair')
        msg = input()

        print('')
        
        if msg == '1':
            print('Digite a quantia')
            msg = msg + self.id + '.' + input().strip()
            self.connect()
            self.socket.send(msg.encode())
            resposta = self.socket.recv(1).decode()
            if resposta == '1':     
                print('Sua solicitação foi realizada com sucesso!')
            else:
                print('Quantia insuficiente!')
            
        elif msg == '2':
            print('Digite a quantia')
            msg = msg + self.id + '.' + input().strip()
            self.connect()
            self.socket.send(msg.encode())
            print('Sua solicitação foi realizada com sucesso!')

        elif msg == '3':
            print('Digite a conta do destinatário (id)')
            destinatario = input()
            print('Digite a quantia')
            msg = msg + self.id + '.' + destinatario + '.' + input().strip()
            self.connect()
            self.socket.send(msg.encode())
            resposta = self.socket.recv(1).decode()
            if resposta == '2':     
                print('Sua solicitação foi realizada com sucesso!')
            elif resposta == '1':
                print('Destinatario invalido!')
            else:
                print('Quantia insuficiente!')

        elif msg == '4':
            msg = msg + self.id
            self.connect()
            self.socket.send(msg.encode())
            saldo = self.socket.recv(10).decode()
            print('Seu saldo é:', saldo)
            
        elif msg == '5':
            self.connect()
            self.socket.send(msg.encode())
            self.socket.close()
            sys.exit()

        else:
            self.connect()
            print('Operação inválida!')

        print('')        
        
        self.socket.close()

client = Client()

while True:
    client.sendmsg()
