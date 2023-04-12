from socket import *

welcomeSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000

welcomeSocket.bind(("", serverPort))
welcomeSocket.listen(1) # questo permette di definire quanti client in coda abbiamo, se si supera la coda arriverà un errore sul client che gli dirà che la coda è piena
print("Server pronto")

while 1:
    # accetto i client e li gestisco con una connessione persistente
    connectionSocket, clientAddr = welcomeSocket.accept()
    print("Connessione accettata: ", clientAddr)

    while 1:
        message = connectionSocket.recv(2048)
        message = message.decode("utf-8")
        if message == '.':
            break

        modifiedMessage = message.upper()

        connectionSocket.send(modifiedMessage.encode("utf-8"))
        print("Client gestito")

    connectionSocket.close()
    print("Connessione chiusa")