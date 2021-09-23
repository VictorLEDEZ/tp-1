from matplotlib import pyplot as plt
from scipy import stats as stats
import numpy as np

# Import all the signals and storing them in an array
X = []
X.append(np.load('./signals/signal.npy'))
X.append(np.load('./signals/signal1.npy'))
X.append(np.load('./signals/signal2.npy'))
X.append(np.load('./signals/signal3.npy'))
X.append(np.load('./signals/signal4.npy'))
X.append(np.load('./signals/signal5.npy'))

# Setting constants
cl1 = 100
cl2 = 200

# Defining the functions
def apriori_calculation(input, classe1, classe2):
 return 1, 2

# Calling them
p1, p2 = apriori_calculation(X, cl1, cl2)

print(p1)
print(p2)