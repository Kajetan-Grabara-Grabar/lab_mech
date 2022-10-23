import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
def wykres1(data):
    plt.plot(data['Hz'],data['Obroty/minuty'])
    plt.title("Obroty na minutę względem Hz")
    plt.xlabel("Hz")
    plt.xticks(range(10, 31))
    plt.grid(True)
    plt.ylabel('Obroty na minutę')
    plt.savefig('wyres1.png',dpi=300)

def wykres2(data):
    plt.clf()
    plt.plot(data['Hz'],data['Prądnica Tachometryczna'],color="red")
    plt.title("Odczyt z prądnicy tachometrycznej wzglendem Hz")
    plt.xlabel("Hz")
    plt.xticks(range(10, 31))
    plt.grid(True)
    plt.ylabel('Odczyt z prądnicy tachometrycnej w V')
    plt.savefig('wyres2.png',dpi=300)
def wykres3(data):
    plt.clf()
    plt.plot(data['Hz'],data['Czujnik indukcji'],color="green")
    plt.title("Odczyt z czujnika indukcji wzglendem Hz")
    plt.xlabel("Hz")
    plt.xticks(range(10, 31))
    plt.grid(True)
    plt.ylabel('Odczyt z czujnika indukcji')
    plt.savefig('wyres3.png',dpi=300)

def wykres4(data):
    plt.clf()
    plt.plot(data['Hz'],data['Czujnik prędkość przepływu'],color="pink")
    plt.title("Odczyt z czujnika prędkości przepływu wzglendem Hz")
    plt.xlabel("Hz")
    plt.xticks(range(10, 31))
    plt.grid(True)
    plt.ylabel('Odczyt z czujnika prędkości przepływu w V')
    plt.savefig('wyres4.png',dpi=300)

if __name__=="__main__":
    data = pd.read_csv("data.csv",encoding="UTF-8")
    wykres1(data)
    wykres2(data)
    wykres3(data)
    wykres4(data)