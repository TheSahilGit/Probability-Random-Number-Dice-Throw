"""Code simulates throwing dice using random number generator"""

### Sahil Islam ###
### 30/06/2020 ###


import numpy as np
import matplotlib.pyplot as plt

ones = []
twos = []
threes = []
fours = []
fives = []
sixes = []
xs = []

throws = 1000
probability = 1 / 6.

o = 0
tw = 0
th = 0
fo = 0
fi = 0
s = 0
x = 0

for i in range(throws):
    a = np.random.randint(1, 7)

    if a == 1:
        o += 1

    elif a == 2:
        tw += 1

    elif a == 3:
        th += 1

    elif a == 4:
        fo += 1

    elif a == 5:
        fi += 1

    elif a == 6:
        s += 1

    x += 1

    ones.append(o)
    twos.append(tw)
    threes.append(th)
    fours.append(fo)
    fives.append(fi)
    sixes.append(s)
    xs.append(x)

plt.plot(xs, ones)
plt.plot(xs, twos)
plt.plot(xs, threes)
plt.plot(xs, fours)
plt.plot(xs, fives)
plt.plot(xs, sixes)
plt.show()
