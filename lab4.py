import lab1
import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
import scipy.stats as sts


def first_task(n, plt):
    print("\n")
    print("выборка {}".format(n))
    Y = lab1.create_sample(n, 6)
    m = sum(Y) / n
    print("Точечное мат. ожидание {0}".format(m))
    D = (sum([(i - m) ** 2 for i in Y]) / (n - 1))
    print("Точечная дисперсия {0}".format(D))
    tt = sts.t(n-1)
    arr = tt.rvs(1000000)
    deltam1 = sts.mstats.mquantiles(arr, prob=0.9) * math.sqrt(D / (n - 1))  # 0.9
    deltam2 = sts.mstats.mquantiles(arr, prob=0.94) * math.sqrt(D / (n - 1))  # 0.95
    deltam3 = sts.mstats.mquantiles(arr, prob=0.98) * math.sqrt(D / (n - 1))  # 0.98
    deltam4 = sts.mstats.mquantiles(arr, prob=0.999) * math.sqrt(D / (n - 1))  # 0.99
    print("интервал мат ожидания:{0}....{1}".format(m - deltam1, m + deltam1))
    print("интервал мат ожидания:{0}....{1}".format(m - deltam2, m + deltam2))
    print("интервал мат ожидания:{0}....{1}".format(m - deltam3, m + deltam3))
    print("интервал мат ожидания:{0}....{1}".format(m - deltam4, m + deltam4))
    plt.plot([0.9, 0.94, 0.98, 0.99], [2 * deltam1, 2 * deltam2, 2 * deltam3, 2 * deltam4], label=n)
    return Y


def first_task_theory(n, plt):
    print("\n")
    print("выборка {}".format(n))
    y = lambda x: 1 / (10 * (x ** 2))*x
    m = integrate.quad(y, 1 / 13, 1 / 3)[0]
    print("мат. ожидание{0}".format(m))
    y1 = lambda x: ((x - m) ** 2) * (1 / (10 * (x ** 2)))
    D = integrate.quad(y1, 1 / 13, 1 / 3)[0]
    print("Дисперсия{0}".format(D))
    tt = sts.t(n-1)
    arr = tt.rvs(1000000)
    deltam1 = sts.mstats.mquantiles(arr, prob=0.9) * math.sqrt(D / (n - 1))  # 0.9
    deltam2 = sts.mstats.mquantiles(arr, prob=0.94) * math.sqrt(D / (n - 1))  # 0.95
    deltam3 = sts.mstats.mquantiles(arr, prob=0.98) * math.sqrt(D / (n - 1))  # 0.98
    deltam4 = sts.mstats.mquantiles(arr, prob=0.99) * math.sqrt(D / (n - 1))  # 0.99
    print("интервал мат ожидания:{0}....{1}".format(m - deltam1, m + deltam1))
    print("интервал мат ожидания:{0}....{1}".format(m - deltam2, m + deltam2))
    print("интервал мат ожидания:{0}....{1}".format(m - deltam3, m + deltam3))
    print("интервал мат ожидания:{0}....{1}".format(m - deltam4, m + deltam4))
    plt.plot([0.9, 0.94, 0.98, 0.99], [2 * deltam1, 2 * deltam2, 2 * deltam3, 2 * deltam4], label=str(n))


def second_task(n, plt):
    print("\n")
    print("выборка {}".format(n))
    Y = lab1.create_sample(n, 6)
    m = sum(Y) / n
    print("мат. ожидание{0}".format(m))
    D = (sum([(i - m) ** 2 for i in Y]) / (n - 1))
    print("Дисперсия{0}".format(D))
    tt = sts.chi2(n - 1)
    arr = tt.rvs(1000000)
    deltam1 = sts.mstats.mquantiles(arr, prob=[0.025, 0.975])  # 0.95
    deltam2 = sts.mstats.mquantiles(arr, prob=[0.01, 0.99])  # 0.98
    deltam3 = sts.mstats.mquantiles(arr, prob=[0.005, 0.995])  # 0.99
    interval = [(n * D / deltam1[1], n * D / deltam1[0]),
                (n * D / deltam2[1], n * D / deltam2[0]),
                (n * D / deltam3[1], n * D / deltam3[0])]
    print("интервал дисперсии:{0}....{1}".format(interval[0][0], interval[0][1]))
    print("интервал дисперсии:{0}....{1}".format(interval[1][0], interval[1][1]))
    print("интервал дисперсии:{0}....{1}".format(interval[2][0], interval[2][1]))
    plt.plot([0.95, 0.98, 0.99],
             [interval[0][1] - interval[0][0],
              interval[1][1] - interval[1][0], interval[2][1] - interval[2][0]], label=n)


def second_task_theory(n, plt):
    print("\n")
    print("выборка {}".format(n))
    y = lambda x: 1 / (10 * (x ** 2))*x
    m = integrate.quad(y, 1 / 13, 1 / 3)[0]
    Y = lab1.create_sample(n, 6)
    D = (sum([(i - m) ** 2 for i in Y]) / n)
    print("Мат ожидание{}".format(m))
    print("Дисперсия{0}".format(D))
    tt = sts.chi2(n - 1)
    arr = tt.rvs(1000000)

    deltam1 = sts.mstats.mquantiles(arr, prob=[0.025, 0.975])  # 0.95
    deltam2 = sts.mstats.mquantiles(arr, prob=[0.01, 0.99])  # 0.98
    deltam3 = sts.mstats.mquantiles(arr, prob=[0.005, 0.995])  # 0.99
    interval = [(n * D / deltam1[1], n * D / deltam1[0]),
                (n * D / deltam2[1], n * D / deltam2[0]),
                (n * D / deltam3[1], n * D / deltam3[0])]
    print("интервал дисперсии:{0}....{1}".format(interval[0][0], interval[0][1]))
    print("интервал дисперсии:{0}....{1}".format(interval[1][0], interval[1][1]))
    print("интервал дисперсии:{0}....{1}".format(interval[2][0], interval[2][1]))
    plt.plot([0.95, 0.98, 0.99],
             [interval[0][1] - interval[0][0],
              interval[1][1] - interval[1][0], interval[2][1] - interval[2][0]], label=n)


if __name__ == "__main__":
    # first_task(20,plt)
    # first_task(30, plt)
    # first_task(50, plt)
    # first_task(70, plt)
    # first_task(100, plt)
    # first_task(150, plt)
    # plt.legend()
    # plt.show()
    # first_task_theory(20, plt)
    # first_task_theory(30, plt)
    # first_task_theory(50, plt)
    # first_task_theory(70, plt)
    # first_task_theory(100, plt)
    # first_task_theory(150, plt)
    # plt.legend()
    # plt.show()

    second_task(20, plt)
    second_task(30, plt)
    second_task(50, plt)
    second_task(70, plt)
    second_task(100, plt)
    second_task(150, plt)
    plt.legend()
    plt.show()

    second_task_theory(20, plt)
    second_task_theory(30, plt)
    second_task_theory(50, plt)
    second_task_theory(70, plt)
    second_task_theory(100, plt)
    second_task_theory(150, plt)
    plt.legend()
    plt.show()
