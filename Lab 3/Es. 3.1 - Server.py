from socket import *

def consonanti(stringa):
    num = 0
    vocali = ['a', 'e', 'i', 'o', 'u', ' ']

    stringa.lower()
    for i in vocali:
        num += stringa.count(i)

    num = len(stringa) - num
    return num

welcomeSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000

welcomeSocket.bind(("", serverPort))
welcomeSocket.listen(1)
print("Server pronto")

while 1:
    connectionSocket, clientAddr= welcomeSocket.accept()
    message = connectionSocket.recv(2048)

    modifiedMessage = message.decode("utf-8")
    toSend = consonanti(modifiedMessage)

    connectionSocket.send(str(toSend).encode("utf-8"))
    print("Client gestito correttamente")
    connectionSocket.close()
