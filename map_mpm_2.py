# Importing modules
from utils.set_graphs import plot_results
from scipy import stats as stats
import numpy as np

# Importing our own modules
from utils.classes_calculations import classes_calculations
from utils.apriori_calculation import apriori_calculation
from utils.gaussian_noise import gaussian_noise
from utils.error_rate import error_rate
from utils.signals import load_signals
from utils.map_mpm_2 import map_mpm_2

# Importing all the variables
from variables import MU1
from variables import MU2
from variables import SIGMA1
from variables import SIGMA2
from variables import ERROR_ITERATIONS

# Import all the signals and storing them in an array
X = load_signals()

# Defining the functions
def mean_error(error_iterations, input, class1, class2, mu1, sigma1, mu2, sigma2):
    """caclulates the mean error across all the iterations of the signal

    Args:
        error_iterations (Number): the amount of simulated signals
        input ([Number]): the emitted signal
        class1 (Number): the first threshold
        class2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the array containing all the errors across the iterations
    """
    E = []
    for t in range(0, error_iterations):
        Y = gaussian_noise(input, class1, class2, mu1, sigma1, mu2, sigma2)
        p1, p2 = apriori_calculation(input, class1, class2)
        S = map_mpm_2(Y, class1, class2, p1, p2, mu1, sigma1, mu2, sigma2)
        tau = error_rate(input, S)
        E.append(tau)
        E[t] = np.mean(E)
    return E

def main(input, mu1, sigma1, mu2, sigma2):
    """call all the functions for the exercise

    Args:
        input ([[Number]]): the array of all the signals
        mu1 ([Number]): the array containing the first mus
        sigma1 ([Number]): the array containing the first sigmas
        mu2 ([Number]): the array containing the second mus
        sigma2 ([Number]): the array containing the second sigmas
    """
    signal_number = 0 
    for inp in input:
        signal_number += 1 
        c1, c2 = classes_calculations(inp)
        all_mean_erros = []
        for i in range(0, len(mu1)):
            E = mean_error(ERROR_ITERATIONS, inp, c1, c2, mu1[i], sigma1[i], mu2[i], sigma2[i])
            all_mean_erros.append(E)
        plot_results(signal_number, all_mean_erros, mu1, sigma1, mu2, sigma2)        

# Calling them
main(X, MU1, SIGMA1, MU2, SIGMA2)