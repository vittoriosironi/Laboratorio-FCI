# Il client invia una stringa al server ed il server la converte in maiuscolo
from socket import *

# il client apre una socket usando TCP
clientSocket = socket(AF_INET, SOCK_STREAM) # Uso sock stream per specificare lo stream TCP

serverPort = 12000
serverAddr = ("localhost", serverPort)

# stabilisco una connessione con il server
clientSocket.connect(serverAddr)

# chiedo stringa all'utente inviandola al server
message = input("Inserisci stringa: ")
clientSocket.send(message.encode("utf-8"))

# ricevo la risposta al server
modifiedMessage = clientSocket.recv(2048) # non returna l'indirizzo di chi sta inviando ma riceve solo il messaggio della socket

print("Messaggio modificato: ", modifiedMessage.decode("utf-8"))

# chiudo la socket
clientSocket.close()