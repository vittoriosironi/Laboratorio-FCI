from socket import *

serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
timeoutValue = 5
clientSocket.settimeout(timeoutValue)

serverAddr = ("127.0.0.1", serverPort)
message = input("Inserisci la stringa: ")

try:
    clientSocket.sendto(message.encode("utf-8"), serverAddr)
    count, serverAddr = clientSocket.recvfrom(2048)

    print("Il server ha risposto: ", count.decode("utf-8"))
except timeout:
    print("Errore timeout")
except:
    print("Errore generico")
finally:
    clientSocket.close()
    print("Socket client chiuso")