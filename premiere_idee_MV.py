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
current_X = 0

counts, _ = np.histogram(X[current_X], bins = int(X[current_X].max() + 1), range = (0, int(X[current_X].max())))
c1, c2 = np.nonzero(counts)[0]

error_iterations = 300

m1 = [120, 127, 127, 127, 127] 
m2 = [130, 127, 128, 128, 128]
s1 = [1, 1, 1, 0.1, 2]
s2 = [2, 5, 1, 0.1, 3]

# Defining the functions
def gaussian_noise(input, classe1, classe2, mu1, sigma1, mu2, sigma2):
    distribution1 = np.random.normal(mu1, sigma1, input.shape)
    distribution2 = np.random.normal(mu2, sigma2, input.shape)
    noise = (input == classe1) * distribution1 + (input == classe2) * distribution2
    return noise

def gaussian_classification(output, classe1, classe2, mu1, sigma1, mu2, sigma2):
    p_omega1 = stats.norm.pdf(output, mu1, sigma1)
    p_omega2 = stats.norm.pdf(output, mu2, sigma2)     
    segmented_signal = np.where(p_omega1 > p_omega2, classe1, classe2)
    return segmented_signal

def error_rate(emitted, received):
    return np.count_nonzero(received - emitted) / len(emitted)

def mean_error(input, classe1, classe2, mu1, sigma1, mu2, sigma2):
    E = []
    for t in range(0, error_iterations):
        Y = gaussian_noise(input, classe1, classe2, mu1, sigma1, mu2, sigma2)
        S = gaussian_classification(Y, classe1, classe2, mu1, sigma1, mu2, sigma2)
        tau = error_rate(input, S)
        E.append(tau)
        E[t] = np.mean(E)
    return E

# Calling them
Y = gaussian_noise(X[current_X], c1, c2, m1, s1, m2, s2)
S = gaussian_classification(Y, c1, c2, m1, s1, m2, s2)
E = mean_error(X[current_X], c1, c2, m1, s1, m2, s2)

# Plot everything
fig, axs = plt.subplots(2, 2)
fig.suptitle('signal = ' + str(current_X) + '  |  ' + 'mu1 = ' + str(m1) + ', sigma1 = ' + str(s1) + '  |  ' + 'mu2 = ' + str(m2) + ', sigma2 = ' + str(s2))

axs[0, 0].plot(X[current_X])
axs[0, 0].set_title('X')
axs[0, 0].set(xlabel = '', ylabel = 'omega')

axs[0, 1].plot(Y, 'tab:orange')
axs[0, 1].set_title('Y')
axs[0, 1].set(xlabel = '', ylabel = '')

axs[1, 0].plot(S, 'tab:green')
axs[1, 0].set_title('S')
axs[1, 0].set(xlabel = 'samples', ylabel = 'omega')

axs[1, 1].plot(E, 'tab:red')
axs[1, 1].set_title('Error over time')
axs[1, 1].set(xlabel = 'samples', ylabel = '')

plt.show()