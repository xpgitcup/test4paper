import numpy as np
import math
import matplotlib.pyplot as pt

x = np.linspace(1, 30, 100)
y = []


def funca(ee):
    v = 3 * (ee - 8) ** 2 + 1 / ee + math.log(ee + 11)
    return v


def funcaa(ee):
    v = 6 * (ee - 8) - 1 / ee + 1 / (ee + 11)
    return v


def funcaaa(ee):
    v = 6 + 2 / ee / ee / ee - 1 / (ee + 11) ** 2
    return v


for ee in x:
    v = funca(ee)
    y.append(v)
#print(x)
#print(y)
pt.plot(x, y)
pt.show()

x = 1
e = 1
print("迭代：")
while (e>1e-10):
    f1 = funcaa(x)
    f2 = funcaaa(x)
    xn = x - f1/f2
    e = abs(x - xn)
    print(f1, f2, xn)
    x = xn
