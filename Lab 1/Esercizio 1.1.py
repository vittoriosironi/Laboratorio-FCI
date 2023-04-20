import matplotlib.pyplot as plt
import requests

siti = ["http://www.google.com", "http://www.youtube.com"]
tempi = []

minT = 9999
avg = 0.0
urlMin = ""
for url in siti:
    for _ in range(5):
        r = requests.get(url)
        tempi.append(r.elapsed.microseconds / 1000)
    avg = sum(tempi)/len(tempi)
    plt.plot(tempi, label = url)
    if minT > avg:
        minT = avg
        urlMin = url

print("Il sito più veloce è: " + str(urlMin))
plt.legend()
plt.show()

# list.index(x) da la posizione dell'elemento x enlla lista LIST