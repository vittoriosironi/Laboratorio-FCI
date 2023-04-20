import requests
# import matplotlib
# from matplotlib import pyplot
import matplotlib.pyplot as plt

tempi = []
url = "http://www.polimi.it"
for _ in range(10):
    r = requests.get(url)
    tempi.append(r.elapsed.microseconds / 1000)
minvalue = min(tempi)
maxvalue = max(tempi)
avg = sum(tempi) / len(tempi)
print("Min: ", minvalue, " Max: ", maxvalue, " Avg: ", avg)

plt.plot(tempi)

plt.title("Tempo di risposta di " + str(url))
plt.xlabel("Id. Richiesta")
plt.ylabel("Tempo (ms)")
plt.grid() # sfondo del grafico quadrettato

plt.show()