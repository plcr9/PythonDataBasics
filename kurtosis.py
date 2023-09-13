import numpy as np
from scipy.stats import norm, kurtosis
data = norm.rvs(size-1000, random_state=3)
kurtosis(data)
