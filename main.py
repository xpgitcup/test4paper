import numpy as np
import math
import matplotlib.pyplot as pt

x = np.linspace(-10, 30, 50)
y = []
for ee in x:
    v = 3 * (ee - 8) ** 2 + 1 / ee + math.log(ee + 11)
    y.append(v)

pt.plot(x, y)
pt.show()
