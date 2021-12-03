from socket import *
import sys

# Definições da classe de cliente
# Importamos bibliotecas de socket para podermos simular as operações de maneira 
# mais real dentro da rede.
# Estaremos definindo endereços padrões, para não causarmos conflitos etc.

class Client:
    # Essa é a função de inicalização, onde definimos os valores padrões
    # para o nosso client.
    # Iniciamos sempre solicitando os dados do usuario, para gravarmos
    # no nosso servidor.
    # Utilizamos um padrão para identificalos, com nome e RG.
    def __init__(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('127.0.0.1',9000))
        print('Digite o seu primeiro nome e RG (Ex: Joao 123)')
        self.id = input().replace(' ', '')
        msg = 'id_' + self.id
        self.socket.send(msg.encode())
        self.socket.close()

    # Função connect responsável por iniciar a conexao ao endereço determinado.
    def connect(self):
        self.socket = socket(AF_INET, SOCK_STREAM)
        self.socket.connect(('127.0.0.1',9000))
        
    # Função auxiliar que servirá ao longo do programa, enviando
    # mensagens ao usuário, via console.
    # Existem diversas opções, mas todas são realizadas enviando mensagens
    # ao servidor e recebendo respostas, para designarmos a tela.
    def sendmsg(self):
        print('Digite o número de acordo com a opção que deseja:')
        print('1: Saque')
        print('2: Depósito')
        print('3: Transferência')
        print('4: Saldo')
        print('5: Sair')
        msg = input()

        print('')
        
        # Opção de saque, retorna mensagem de sucesso ou falha
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
            
        # Opção de depósito, retorna mensagem de sucesso
        elif msg == '2':
            print('Digite a quantia')
            msg = msg + self.id + '.' + input().strip()
            self.connect()
            self.socket.send(msg.encode())
            print('Sua solicitação foi realizada com sucesso!')

        # Opção de transferência, retorna mensagem de sucesso ou falha, pois
        # além de checar o saldo, verifica a existência do destinatário no
        # sistema.
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

        # Opção de saldo, retorna o valor
        elif msg == '4':
            msg = msg + self.id
            self.connect()
            self.socket.send(msg.encode())
            saldo = self.socket.recv(10).decode()
            print('Seu saldo é:', saldo)
            
        # Opção de saida, finaliza o servidor e sai do sistema
        # atual, o client.
        elif msg == '5':
            self.connect()
            self.socket.send(msg.encode())
            self.socket.close()
            sys.exit()

        # Tratamento de erro para caso o usuário selecioanr uma
        # opção inválida
        else:
            self.connect()
            print('Operação inválida!')

        print('')        
        
        self.socket.close()

client = Client()

while True:
    client.sendmsg()
