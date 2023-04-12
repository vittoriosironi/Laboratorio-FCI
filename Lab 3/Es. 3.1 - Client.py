from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
clientPort = 12000
timeoutValue = 2
serverAddr = ("localhost", clientPort)

clientSocket.connect(serverAddr)
clientSocket.settimeout(timeoutValue)

message = input("Inserisci una stringa > ")
clientSocket.send(message.encode("utf-8"))

try:
    message = clientSocket.recv(2048)
    modifiedMessage = message.decode("utf-8")
    print("Numero di consonanti > ", modifiedMessage)
except timeout:
    print("Timeout scaduto")
except:
    print("Errore generico")
finally:
    clientSocket.close()