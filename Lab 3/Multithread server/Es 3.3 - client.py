from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
serverAddr = ("localhost", 12000)
timeoutValue = 10

clientSocket.connect(serverAddr)
clientSocket.settimeout(timeoutValue)
print("Client connesso")

try:
    while 1:
        num = input("Inserisci numero > ")
        if num == '.':
            print("La connessione termina")
            break
        clientSocket.send(str(num).encode("utf-8"))

        isPrimo = clientSocket.recv(2048)
        print("Is num primo? ", isPrimo.decode("utf-8"))
except timeout:
    print("Timeout scaduto")
finally:
    clientSocket.close()