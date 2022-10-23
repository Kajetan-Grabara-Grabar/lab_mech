import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
def wykres():
    data = pd.read_csv("data.csv",encoding="UTF-8")
    print(data)
    plt.plot(data['Hz'],data['Obroty/minuty'])
    plt.title("Obroty na minutę względem Hz")
    plt.xlabel("Hz")
    plt.xticks(range(10, 31))
    plt.grid(True)
    plt.ylabel('Obroty na minutę')
    plt.savefig('wyres1.png',dpi=300)

if __name__=="__main__":
    wykres()