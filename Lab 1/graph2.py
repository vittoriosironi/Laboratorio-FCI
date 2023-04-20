import matplotlib.pyplot as plt
import requests


siti = ["http://www.google.com", "http://www.polimi.it", "http://www.netflix.com"]

tmax = 0
tmin = 0
for url in siti:
    tempi = []
    for _ in range(10):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)

    print("Tempo min di " + url + ": ", min(tempi))
    plt.plot(tempi, label = url) # label identifica la linea al'interno del grafico (ovvero è come inserire la variabile in cui raggrupare i dati)
    # quindi ogni linea sarà associata ad un url
    tmax = max(tmax, max(tempi)) # massimo tra i tempi
    tmin = min(tmin, min(tempi))
plt.title("Tempi di risposta")
plt.xlabel("Id. Richiesta")
plt.ylabel("Tempo (ms)")
plt.legend() # legenza con i colori associati al sito web
plt.xlim([-1, 11]) # setto al grandezza del grafico
plt.ylim([tmin, tmax])
plt.grid()

plt.show()
