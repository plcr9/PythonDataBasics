import pandas as pd
import numpy as np
import statistics

speed = [99,86,87,88,86,103,87,94,78,77,85,86]

x = np.mean(speed)
y = np.median(speed)
z = np.mode(speed)

print(x)
print(y)
print(z)
print(statistics.stdev(speed))
