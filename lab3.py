import lab1
import numpy as np
import math
def Pearson(n):
    Y = lab1.create_sample(n, 6)
    sort = sorted(Y)
    y = lambda x: (13 / 10) - (1 / (10 * x))
    M = int(4 * np.log10(n))
    v = math.ceil(len(Y) / M)

    pi = [v / n for _ in range(1, M)]
    pi.append((n - sum(pi * n)) / n)
    A = [sort[0]]
    B = []
    temp = [(sort[(i * v) + 1] + sort[i * v]) / 2 for i in range(1, M)]
    for i in temp:
        A.append(i)
        B.append(i)
    B.append(sort[-1])

    p = [(y(B[i]) - y(A[i])) for i in range(0, M)]
    print("k = ",M-2-1)

    if abs(1-sum(pi))<0.01:
        print("Критерий проходит")
    else:
        print("Критерий не проходит")


    return n*sum([((pi[i] - p[i]) ** 2) / p[i] for i in range(0, M)])

def Kolmogorov(n):
    Y = lab1.create_sample(n, 6)
    sort = sorted(Y)
    y = lambda x: (13 / 10) - (1 / (10 * x))
    xe,ye=lab1.empir(sort,False)
    yt=[y(x) for x in xe[1:]]
    different=max([math.fabs(ye[i]-yt[i])for i in range(1,len(xe),2)])
    return math.sqrt(n)*different

def Mizes(n):
    Y = lab1.create_sample(n, 6)
    sort = sorted(Y)
    y = lambda x: (13 / 10) - (1 / (10 * x))
    xe, ye = lab1.empir(sort, False)
    yt = [y(x) for x in xe[1:]]
    delta=sum([(ye[i]-yt[i])**2for i in range(1,len(xe),2)])
    return (1/(12*n))+delta
if __name__=="__main__":
    p=Pearson(200)
    if  p<16.81:
        print("подчиняются  распределению при уровне значимости a = 0,01")
    else:
        print("не подчиняются распределению при уровне значимости a = 0,01")
    if Kolmogorov(30)<1.62:
        print("подчиняются равномерному распределению при уровне значимости a = 0,05")
    else:
        print("не подчиняются равномерному распределению при уровне значимости a = 0,05")
    if Mizes(50)<0.744:
        print("подчиняются равномерному распределению при уровне значимости a = 0,01")
    else:
        print("не подчиняются равномерному распределению при уровне значимости a = 0,01")