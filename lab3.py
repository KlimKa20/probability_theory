import lab1
import numpy as np
import math
def Prison(n):
    Y = lab1.create_sample(n, 6)
    sort = sorted(Y)
    y = lambda x: (13 / 10) - (1 / (10 * x))
    M = int(2 * np.log10(n))
    v = int(100 / M)
    x = [sort[0]]
    x.append((sort[0] + sort[v - 1]) / 2)
    temp = [(sort[(i * v) - 1] + sort[((i + 1) * v) - 1]) / 2 for i in range(1, M - 1)]
    for i in temp:
        x.append(i)
    x = [sort[i] for i in range(0, M + 1)]
    p = [(y(x[i + 1]) - y(x[i])) for i in range(0, M)]
    ni = M / n
    return sum([((ni - n * p[i]) ** 2) / (n * p[i]) for i in range(0, M)])

def Kolmogorova(n):
    Y = lab1.create_sample(n, 6)
    sort = sorted(Y)
    y = lambda x: (13 / 10) - (1 / (10 * x))
    xe,ye=lab1.empir(sort,False)
    yt=[y(x) for x in xe]
    different=max([math.fabs(ye[i]-yt[i])for i in range(0,len(xe))])
    return math.sqrt(n)*different

def Mizes(n):
    Y = lab1.create_sample(n, 6)
    sort = sorted(Y)
    y = lambda x: (13 / 10) - (1 / (10 * x))
    xe, ye = lab1.empir(sort, False)
    yt = [y(x) for x in xe]
    delta=sum([(ye[i]-yt[i])**2for i in range(0,len(xe))])
    return (1/(12*n))+delta
if __name__=="__main__":
    p=Prison(200)
    if  p<13.28:
        print("подчиняются равномерному распределению при уровне значимости a='0.1'")
    else:
        print("не подчиняются равномерному распределению при уровне значимости a='0.1'")
    if Kolmogorova(30)<1.62:
        print("подчиняются равномерному распределению при уровне значимости a = 0,05")
    else:
        print("не подчиняются равномерному распределению при уровне значимости a = 0,05")
    if Mizes(50)<0.744:
        print("подчиняются равномерному распределению при уровне значимости a = 0,01")
    else:
        print("не подчиняются равномерному распределению при уровне значимости a = 0,01")