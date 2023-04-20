import requests # questo importa la libreria

# prima richiesta HTTP
r = requests.get("http://www.google.com")
print(r.content) # visualizza il contenuto della risposta
print(r.cookies) # visualizza i cookies del nostro pacchetto
print(r.status_code) # sono i codici di stato HTTP quindi identifica se la richiesta è andata a buon fine
print("Il codice di stao è: " + str(r.status_code)) # così è più carino
print("Tempo di risposta: " + str(r.elapsed.microseconds) + " in microsecondi") # ci indica quanto tempo è trascorso dall'invio della risposta alla ricezione -> è il TEMPO DI RISPOSTA
print("Tempo di risposta: " + str(r.elapsed.microseconds / 1000) + " in milliseconfi")


# 10 richieste HTTP
# for _ in range(10):
for i in range(10):
    r = requests.get("http://www.polimi.it")
    print(str(i + 1) + "° tempo:" + str(r.elapsed.microseconds / 1000))
print("For finito")

# Calcoliamo il tempo di risposta minimo su 10 richieste
listatempi = []
for _ in range(10):
    r = requests.get("http://www.polimi.it")
    listatempi.append(r.elapsed.microseconds / 1000)
print("Questa è la lista dei tempi", listatempi)
print("Tempo minimo: ", min(listatempi))
print("Tempo medio:  ", sum(listatempi) / len(listatempi))
