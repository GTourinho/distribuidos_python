# <div align="center">Bank System 🏦</div>

##### <div align="center">Sistema de banco montado na arquitetura cliente/servidor </div>

https://user-images.githubusercontent.com/41840640/144530702-037919a6-99ce-4e5b-94bc-7b3fd1287e5c.mp4

## Notas do Projeto 📜

1. Este trabalho objetiva promover um entendimento básico do funcionamento e importância da comunicação entre processos na arquitetura cliente/servidor.
2. Este sistema simula uma caixa eletrônico, oferecendo operações financeiras.
3. Dentre as opções do programa, temos:
- Realizar saque 
- Realizar depósito
- Realizar transferência
- Consultar saldo

## Prerequisitos ⚙️

1. Python 3 (min) - ```$ install python3``` ou [Python.org](https://www.python.org/downloads/)
2. Git - ```$ brew install git``` ou ```$ install git```


## Instalação 📌


##### 1. Clone o repositório

```$ git clone https://github.com/GTourinho/distributed-banking-system-python.git  ```

##### 2. Mude para o diretório de trabalho

```$ cd distributed-banking-system-python ```

##### 3. Execute a aplicação servidor

```$ py server/main.py  ```

##### 4. Execute a aplicação cliente

```$ py client/main.py  ```


## Instruções de uso 📋


##### 1. O sistema irá funcionar a partir da inicialização do servidor e, posteriormente, da tela do cliente.
##### 2. Para inicializar um cliente, você deve cadastra-lo, informando o nome seguido do RG.
##### 3. Após o cadastro, serão mostradas as opções do caixa eletrônico. Lembrando que todo cliente inicia sua conta com saldo zerado.
##### 4. Ao selecionar as opções de SAQUE ou DEPÓSITO, o cliente deverar informar o valor. 
##### 5. Ao selecionar a opção de TRANSFERÊNCIA, o cliente deverar informar o ID do destinatário seguido do valor. 
##### 6. Nosso sistema não aceita valores negativos.
##### 7. Operações que solicitarem valores maiores que os disponíveis, serão automaticamente canceladas e informadas no visor.


## Equipe desenvolvedora 💻

- [Gabriel Tourinho](https://github.com/GTourinho/)
- [Paulo Bomfim](https://github.com/phbomfim/)

*Universidade Federal da Bahia - 2021.1 - MATA59 - Redes de Computadores*
