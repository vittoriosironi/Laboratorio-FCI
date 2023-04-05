from socket import *

serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
ciao = serverSocket.bind(("", serverPort)) # lasciamo una stringa vuota perchè il pycharm andrà a riempirlo lui e server port che indica il numero di porta della nostra socket
# La parentesi interna è per definire una tuple
# bind = lega
print(ciao)

print("Il server è pronto")
while 1:
    message, clientAddr = serverSocket.recvfrom(2048) # 2048 -> dimensione massima del buffer. La funzione ritorna due parametri ovvero il messaggio inviato e l'indirizzo di chi ci sta contattando
    print("Ho ricevuto una richiesta da ", clientAddr)
    modifiedMessage = message.decode("utf-8")
    modifiedMessage = modifiedMessage.upper()

    serverSocket.sendto(modifiedMessage.encode("utf-8"), clientAddr)


# rispondo tramite la socket
