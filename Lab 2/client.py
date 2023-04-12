# importo la libreria
from socket import *

# apro socket per comunicare UDP
clientSocket = socket(AF_INET, SOCK_DGRAM) # AF_INET -> IPv4, SOCK_DGRAM -> protocollo UDP
# METTO UN TIMEOUT PE GESTIRE GLI ERRORI
timeoutValue = 3
clientSocket.settimeout(timeoutValue)

# chiedi una stringa all'utente
message = input("Inserisci una stringa: ") # l'utente inserisce le stringhe


serverPort = 12000 # attraverso la porta 120000, porta usata dal server. La porta usata del server dev'essere aperta
serverAdress = ("127.0.0.1", serverPort)

try:
    # richiedi al server inviando la stringa
    clientSocket.sendto(message.encode("utf-8"), serverAdress) # codifichiamo la sctringa in utf-8 transformadola in binario e mandando i byte tramite la nostra socket UDP


    # ascolto dalla socket per la risposta
    modifiedMessage, serverAdress = clientSocket.recvfrom(2048) # ricevo il messaggio di conferma dal server con 2048 che è la dimensione massima in byte del messaggio

    print("Il server risponde: ", modifiedMessage.decode("utf-8"))

except timeout:
    print("Il server non ha risposto entro il timeout")
except ZeroDivisionError:
    print("Divisione per zero")
except:
    print("Errore generico")
finally:
# chiudere la socket
    clientSocket.close()
    print("Il programma è terminato con successo")