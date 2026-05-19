# matplotlib e seaborn

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.figure()
plt.plot(x, y)

plt.title("Grafico a linee")
plt.xlabel("X")
plt.ylabel("Y")

plt.show()