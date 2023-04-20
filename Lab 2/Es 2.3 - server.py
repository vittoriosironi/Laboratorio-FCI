from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM)
serverPort = 12000

serverSocket.bind(("", serverPort))
print("Server pronto")

message, clientAddr = serverSocket.recvfrom(2048)
message = message.decode("utf-8").lower()
print("Messagio ricevuto da: ", clientAddr)

vocali = ['a', 'e', 'i', 'o', 'u', ' ']
count = 0
for i in vocali:
    count += message.count(i)
countCons = len(message) - count

serverSocket.sendto(str(countCons).encode("utf-8"), clientAddr)
