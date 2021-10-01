import numpy as np

from .gaussian_classification import gaussian_classification
from .apriori_calculation import apriori_calculation
from .gaussian_noise import gaussian_noise
from .error_rate import error_rate
from .map_mpm_2 import map_mpm_2

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

    E_gaussian = []
    E_mpm = []
    
    for t in range(0, error_iterations):
        Y = gaussian_noise(input, class1, class2, mu1, sigma1, mu2, sigma2)
        
        S_gaussian = gaussian_classification(Y, class1, class2, mu1, sigma1, mu2, sigma2)
        
        p1, p2 = apriori_calculation(input, class1, class2)
        S_mpm = map_mpm_2(Y, class1, class2, p1, p2, mu1, sigma1, mu2, sigma2)

        tau_gaussian = error_rate(input, S_gaussian)
        E_gaussian.append(tau_gaussian)
        E_gaussian[t] = np.mean(E_gaussian)
        
        tau_mpm = error_rate(input, S_mpm)
        E_mpm.append(tau_mpm)
        E_mpm[t] = np.mean(E_mpm)
    
    return E_gaussian, E_mpm
