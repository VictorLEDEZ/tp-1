from matplotlib import pyplot as plt
from scipy import stats as stats
import numpy as np

from utils.signals import load_signals

# Importing all the variables
from variables import M1
from variables import M2
from variables import S1
from variables import S2
from variables import ERROR_ITERATIONS

# Import all the signals and storing them in an array
X = load_signals()

# Setting constants
cl1 = 100
cl2 = 200

# Defining the functions
def apriori_calculation(input, classe1, class2, p1, p2, mu1, sigma1, mu2, sigma2):
    probability_Y1 = stats.norm.pdf(input, mu1, sigma1)
    probability_Y2 = stats.norm.pdf(input, mu2, sigma2)
    return classe1 * (p1 * probability_Y1 > p2 * probability_Y2) + class2 * (p1 * probability_Y1 < p2 * probability_Y2)

# Calling them
S = apriori_calculation(X[0], cl1, cl2, 0.8, 0.2, M1[0], S1[0], M2[0], S2[0])

plt.plot(S)
plt.show()