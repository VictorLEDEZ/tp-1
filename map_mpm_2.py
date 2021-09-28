from matplotlib import pyplot as plt
from scipy import stats as stats
import numpy as np

from utils.signals import load_signals

# Import all the signals and storing them in an array
X = load_signals()

# Setting constants
m1 = [120, 127, 127, 127, 127] 
m2 = [130, 127, 128, 128, 128]
s1 = [1, 1, 1, 0.1, 2]
s2 = [2, 5, 1, 0.1, 3]
cl1 = 100
cl2 = 200

# Defining the functions
def apriori_calculation(input, classe1, class2, p1, p2, mu1, sigma1, mu2, sigma2):
    probability_Y1 = np.normpdf(input, mu1, sigma1)
    probability_Y2 = np.normpdf(input, mu2, sigma2)
    return classe1 * (p1 * probability_Y1 > p2 * probability_Y2) + class2 * (p1 * probability_Y1 < p2 * probability_Y2)

# Calling them
S = apriori_calculation(X, cl1, cl2, 0.5, 0.5, m1, s1, m2, s2)

print(S)