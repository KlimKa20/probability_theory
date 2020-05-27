import lab1
import numpy as np
import math
import matplotlib.pyplot as plt


def equal_interval(Y):
    sort = sorted(Y)
    M = int(4 * np.log10(len(Y)))
    h = (sort[-1] - sort[0]) / M
    A = [sort[0]]
    B = []
    for i in range(2, M + 1):
        A.append(sort[0] + h * (i - 1))
        B.append(sort[0] + h * (i - 1))
    B.append(sort[-1])
    v = []
    temp = 0
    number = 0
    for i in sort:
        if i < B[number]:
            temp += 1
        else:
            if i == B[number]:
                u = sort.count(i) / 2
                temp += u
                v.append(temp)
                temp = u
            else:
                v.append(temp)
                temp = 0
            number += 1
    f = [v[i] / (len(Y) * h) for i in range(0, M)]
    x, y = [], []
    x.append(A[0])
    y.append(0)
    for key, item in enumerate(A):
        x.append(A[key])
        x.append(B[key])
        y.append(f[key])
        y.append(f[key])
    x.append(B[-1])
    y.append(0)

    print("равноинтервальный метод(гистограмма)")
    for i in range(len(A)):
        print("{0} - {1}    ---  {2}".format(A[i],B[i],f[i]))

    plt.plot(x, y, label='равноинтервальный метод(гистограмма)')
    plt.legend()
    plt.show()


    x, y = [(B[i] + A[i]) / 2 for i in range(0, len(B))], f
    f1 = lambda x: 1 / (10 * (x ** 2))
    x1 = np.linspace((B[0] + A[0]) / 2 , (B[-1] + A[-1]) / 2 , 100)

    print("равноинтервальный метод(полигон)")
    lab1.table(x,y)

    plt.plot(x1, f1(x1), "orange", label='теоритическая плотность')
    plt.plot(x, y, label='равноинтервальный метод(полигон)')
    plt.legend()
    plt.show()


    li = [x / len(sort) for x in v]
    temper = []
    for i in range(0, len(li)):
        temper.append(sum(li[:i + 1]))

    print("Эмпирическая функция по сгрупированным данным ")
    for i in range(len(A)):
        print("{0} - {1}    ---  {2}".format(A[i], B[i], temper[i]))

    x, y = [0], [0, 0]
    for key, item in enumerate(B):
        x.extend([item, item])
        y.append(temper[key])
        y.append(temper[key])
    y.pop()
    x.append(1 / 3)
    y.append(y[-1])
    y.append(y[-1])
    x.append(0.41)
    plt.plot(x, y, label='Эмпирическая функция по сгрупированным данным')
    plt.legend()
    plt.show()

def equal_probability(Y):
    sort = sorted(Y)
    M = int(4 * np.log10(len(Y)))
    v = int(len(Y) / M)
    A = [sort[0]]
    B = [(sort[0] + sort[v - 1]) / 2]
    temp = [(sort[(i * v) - 1] + sort[((i + 1) * v) - 1]) / 2 for i in range(1, M - 1)]
    A.append(B[0])
    for i in temp:
        A.append(i)
        B.append(i)
    B.append(sort[-1])
    h = [B[i] - A[i] for i in range(0, M)]
    f = [v / (len(Y) * h[i]) for i in range(0, M)]
    x, y = [], []
    x.append(A[0])
    y.append(0)
    for key, item in enumerate(A):
        x.append(A[key])
        x.append(B[key])
        y.append(f[key])
        y.append(f[key])
    x.append(B[-1])
    y.append(0)

    print("равновероятностный метод(гистограмма)")
    for i in range(len(A)):
        print("{0} - {1}    ---  {2}".format(A[i],B[i],f[i]))

    plt.plot(x, y, label='равновероятностный метод(гистограмма)')
    plt.legend()
    plt.show()

    x, y = [(B[i] + A[i]) / 2 for i in range(0, len(B))], f
    f = lambda x: 1 / (10 * (x ** 2))
    x1 = np.linspace((B[0] + A[0]) / 2, (B[-1] + A[-1]) / 2, 100)

    print("равновероятностный метод(полигон)")
    lab1.table(x,y)

    plt.plot(x1, f(x1), "orange", label='теоритическая плотность')
    plt.plot(x, y, label='равновероятностный метод(полигон)')
    plt.legend()
    plt.show()

    li = [v / len(sort) for x in range(len(A)) ]
    temper = []
    for i in range(0, len(li)):
        temper.append(sum(li[:i + 1]))

    print("Эмпирическая функция по сгрупированным данным ")
    for i in range(len(A)):
        print("{0} - {1}    ---  {2}".format(A[i], B[i], temper[i]))

    x, y = [0], [0, 0]
    for key, item in enumerate(B):
        x.extend([item, item])
        y.append(temper[key])
        y.append(temper[key])
    y.pop()
    x.append(1 / 3)
    y.append(y[-1])
    y.append(y[-1])
    x.append(0.41)
    plt.plot(x, y, label='Эмпирическая функция по сгрупированным данным')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    Y = lab1.create_sample(1000, 6)
    equal_interval(Y)
    equal_probability(Y)


