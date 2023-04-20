from socket import *

# apro una welcome socket su una porta definita
welcomeSocket = socket(AF_INET, SOCK_STREAM)
serverPort = 12000

welcomeSocket.bind(("", serverPort))
print("Server pronto")

welcomeSocket.listen(1) # definisce la dimensione della coda dei client da mettere in attesa mentre gestisco altri client


# CICLO INFINITO -> dev'essere un ciclo che si ripete perchè il server avrà più client che si connettono a lui
while 1:
    # accetto connessioni dal client (genero nuova socket)
    connectionSocket, clientAddr = welcomeSocket.accept() # restituisce la nuova socket e il clientAddr

    # ricevo il messaggio dal client
    message = connectionSocket.recv(2048)
    modifiedMessage = message.decode("utf-8")

    # modfico il messaggio
    modifiedMessage.upper()

    # invio il messaggio modificato al client
    connectionSocket.send(modifiedMessage.encode("utf-8"))

    # chiudo connection socket
    print("Client gestito correttamente")
    connectionSocket.close()



