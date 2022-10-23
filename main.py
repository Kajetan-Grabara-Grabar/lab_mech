import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import csv
def import_data():
    with open('data.csv', newline='', encoding='UTF-8') as f:
        reader = csv.reader(f)
        data = list(reader)
    return data
def wykres():
    data = pd.read_csv("data.csv",encoding="UTF-8")
    print(data)
    plt.plot(data['Hz'],data['Obroty/minuty'],data['Prądnica Tachometryczna'])
    plt.show()
def test():
    df = pd.read_csv(r'https://analityk.edu.pl/wp-content/uploads/2020/12/data.csv')
    df['date'] = pd.to_datetime(df.date, format='%d/%m/%Y')
    x=df['date']
    y=df['Close']
    plt.plot(x,y)
    plt.show()

if __name__=="__main__":
    # plt.plot(import_data())
    # test()
    wykres()