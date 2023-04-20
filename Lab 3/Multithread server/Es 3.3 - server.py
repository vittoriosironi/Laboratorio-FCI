from socket import *
from threading import Thread

welcomeSocket = socket(AF_INET, SOCK_STREAM)
serverAddr = ("", 12000)
welcomeSocket.bind(serverAddr)

welcomeSocket.listen(1)
welcomeSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
print("Server pronto")

def isPrimo(connSocket):

    while 1:
        num = connSocket.recv(2048)
        num = num.decode("utf-8")
        numInt = int(num)

        out = "Yes"
        for i in (2, numInt / 2):
            if numInt % i == 0:
                out = "No"
                break
        connSocket.send(str(out).encode("utf-8"))
        print("Client gestito")
    connSocket.close()
    print("Connessione chiusa")


while 1:
    connectionSocket, clientAddr = welcomeSocket.accept()
    print("Connessione accettata: ", clientAddr)

    thread = Thread(target=isPrimo, args=(connectionSocket, ))
    thread.start()