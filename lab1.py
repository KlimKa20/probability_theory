import random
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import math
import pandas as pd
def create_sample(n, z):
    function = lambda x: 1 / (x + 3)
    X = list()
    a = 0
    b = 10
    for i in range(0, n):
        X.append(a + (b - a) * random.random())
    return [round(function(x), z) for x in X]

def table(x,y):
    df = pd.DataFrame({
    'значения': x,
    'частота': y})
    print(df)

def empir(sort,tableBool):
    count = len(sort)
    setsort=sorted(set(sort))
    li = [sort.count(x) / count for x in setsort]
    if tableBool:
        table(setsort,li)
    temper = []
    for i in range(0, len(li)):
        temper.append(sum(li[:i + 1]))
    x, y = [0], [0,0]
    mass = sorted(set(sort))
    for key, item in enumerate(mass):
        x.extend([item, item])
        y.append(temper[key])
        y.append(temper[key])
    y.pop()
    return x,y

if __name__ == "__main__":
    n = int(input("Введите размер выборки"))
    Y = create_sample(n, 6)
    print("Исходник {0}".format(Y))
    sort = sorted(Y)
    print("Вариационный ряд{0}".format(sort))

    x,y=empir(sort,True)
    x.append(1/3)
    y.append(y[-1])
    y.append(y[-1])
    x.append(0.41)
    plt.plot(x, y, label = 'F*(x)')

    y = lambda x: (13/10)-(1/(10*x))
    x = np.linspace(1/13, 1/3,  100)
    plt.plot(x, y(x),"orange", label = 'F(x)')

    plt.legend()
    plt.show()
