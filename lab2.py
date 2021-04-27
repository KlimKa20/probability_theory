import lab1
import numpy as np
import math
import matplotlib.pyplot as plt


def equal_interval(Y):
    sort = sorted(Y)
    if len(Y)>100:
        M = math.ceil(int(4 * np.log10(len(Y))))
    else:
        M=math.ceil(math.sqrt(len(Y)))
    h = (sort[-1] - sort[0]) / M
    A = [sort[0]]
    B = []
    for i in range(2, M+1):
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
    f1 = lambda x: 1 / (10 * (x ** 2))
    x1 = np.linspace(A[0], B[-1] , 100)
    plt.plot(x1, f1(x1), "orange", label='теоритическая плотность')
    plt.plot([0, A[0]], [0, 0], "orange")
    plt.plot([B[-1], 0.5], [0, 0], "orange")
    plt.legend()
    plt.show()

    print("равноинтервальный метод(полигон)")
    x = [(B[i] + A[i]) / 2 for i in range(0, len(B))]
    f = [v[i] / (len(Y)) for i in range(0, M)]
    lab1.table(x, f)

    print("\nАналитический вид")
    print("-infinity - {0} = {1}".format((B[0] + A[0]) / 2, 0))
    for i in range(0, len(B) - 1):
        print("{0} - {1} = {2}".format((B[i + 1] + A[i + 1]) / 2, (B[i + 1] + A[i + 1]) / 2, f[i+1]))
    print("{0}-infinity = {1}".format((B[-1] + A[-1]) / 2, 0))
    plt.plot(x, f, label='равноинтервальный метод(полигон)')
    plt.legend()
    plt.show()

    print("Эмпирическая функция по сгрупированным данным ")
    li = [x / len(sort) for x in v]
    temper = []
    for i in range(0, len(li)):
        temper.append(sum(li[:i + 1]))
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
    if len(Y) > 100:
        M = int(4 * np.log10(len(Y)))
    else:
        M = int(math.sqrt(len(Y)))
    v = int(len(Y) / M)
    A = [sort[0]]
    B = []
    temp = [(sort[(i * v) - 1] + sort[i * v]) / 2 for i in range(1, M)]
    for i in temp:
        A.append(i)
        B.append(i)
    B.append(sort[-1])
    h = [B[i] - A[i] for i in range(0, M)]
    f = [v / (len(Y) * h[i]) for i in range(0, M-1)]
    f.append((n-v*(M-1))/n / (len(Y) * h[-1]))
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
    f1 = lambda x: 1 / (10 * (x ** 2))
    x1 = np.linspace(A[0], B[-1], 100)
    plt.plot(x1, f1(x1), "orange", label='теоритическая плотность')
    plt.plot([0, A[0]], [0, 0], "orange")
    plt.plot([B[-1], 0.5], [0, 0], "orange")
    plt.legend()
    plt.show()

    # x, y = [(B[i] + A[i]) / 2 for i in range(0, len(B))], f
    # f = lambda x: 1 / (10 * (x ** 2))

    # print("равновероятностный метод(полигон)")
    # lab1.table(x,y)
    #
    # f = [v / (len(Y)) for i in range(0, M)]
    # plt.plot(x, f, label='равновероятностный метод(полигон)')
    # plt.legend()
    # plt.show()



    print("Эмпирическая функция по сгрупированным данным ")
    li = [v / len(sort) for x in range(len(A))]
    temper = []
    for i in range(0, len(li)):
        temper.append(sum(li[:i + 1]))
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
    n = int(input("Введите размер выборки"))
    Y = lab1.create_sample(n, 6)
    equal_interval(Y)
    equal_probability(Y)


