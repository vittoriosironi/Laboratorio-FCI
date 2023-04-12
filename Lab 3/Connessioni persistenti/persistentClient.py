# Il client invia una stringa di caratteri al server, il quale risponde con la stessa stringa in cui le lettere minuscole sono rese maiuscole
# Ogni messaggio è terminato da un carattere << a capo >> e la connessione va terminata quando il messaggio è un singolo punto << . >>

from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
serverAddr = ("localhost", serverPort)
clientSocket.connect(serverAddr)
print("Client connesso")

while 1:
    message = input("Inserisci una stringa (PUNTO per terminare la connessione):")

    clientSocket.send(message.encode("utf-8"))

    modifiedMessage = clientSocket.recv(2048)
    if message == '.':
        print("L'applicazione termina...")
        break

    print("Il server risponde: ", modifiedMessage.decode("utf-8"))

clientSocket.close()