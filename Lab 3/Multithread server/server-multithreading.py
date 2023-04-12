from socket import *
from threading import Thread # importeremo le funzioni per gestire i thread

welcomeSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000
welcomeSocket.bind(("", serverPort))

welcomeSocket.listen(1)
welcomeSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # -> con questa opzione stiamo dicendo alla socket di permettergli di utilizzare più volte lo stesso indirizzo nella stessa socket. Questo quindi vuole dire che posso usare la funzione accpet più volte senza chiuderle
print("Server pronto")

def gestisciClient(connSocket):
    while 1:
        message = connSocket.recv(2048)
        message = message.decode("utf-8")
        if message == '.':
            break
        modifiedMessage = message.upper()
        connSocket.send(modifiedMessage.encode("utf-8"))
        print("Client gestito")
    connSocket.close()
    print("Connessione chiusa")

while 1:
    connectionSocket, clientAddr = welcomeSocket.accept()
    print("Connessione accettata: ", clientAddr)

    # ci permette di creare nuovi thread nel sistema operativo
    # gestisci client è la funzione che andrà fatta su più thread e in args mettiamo gli argomenti della funzione
    # IMPORTANTE: l'ultimo elemento della tuple di args dev'essere vuoto
    thread = Thread(target=gestisciClient, args=(connectionSocket, )) # -> genero un lavoratore
    thread.start() # avvio il thread
    # il thread gestisce quindi il client