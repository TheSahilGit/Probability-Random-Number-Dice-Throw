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
    a = np.random.random()

    if 0 * probability < a < 1 * probability:
        o += 1

    elif probability < a < 2 * probability:
        tw += 1

    elif 2*probability < a < 3 * probability:
        th += 1

    elif 3 * probability < a < 4 * probability:
        fo += 1

    elif 4 * probability < a < 5 * probability:
        fi += 1

    elif 5 * probability < a < 6 * probability:
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
