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

# Defining the functions
def gaussian_noise(input, classe1, classe2, mu1, sigma1, mu2, sigma2):
    """Changes the input by adding some noise depending on omega1 or omega2

    Args:
        input ([Number]): the emitted signal
        classe1 (Number): the first threshold
        classe2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the recieved signal with some noise due to the communication
    """
    return (input == classe1) * np.random.normal(mu1, sigma1, input.shape) + (input == classe2) * np.random.normal(mu2, sigma2, input.shape)

def gaussian_classification(output, classe1, classe2, mu1, sigma1, mu2, sigma2):
    """Reconstitute the segmented signal S from the recieved signal via classe1 and classe2

    Args:
        output ([Number]): the recieved signal
        classe1 (Number): the first threshold
        classe2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the regenerated signal S
    """
    return np.where(stats.norm.pdf(output, mu1, sigma1) > stats.norm.pdf(output, mu2, sigma2), classe1, classe2)

def error_rate(emitted, received):
    """calculates the Bit Error Rate (BER) between the emitted and the recieved signal

    Args:
        emitted ([Number]): the clean emited signal
        received ([Number]): the segmented signal

    Returns:
        Number: the Bit Error Rate
    """
    return np.count_nonzero(received - emitted) / len(emitted)

def mean_error(error_iterations, input, classe1, classe2, mu1, sigma1, mu2, sigma2):
    """caclulates the mean error across all the iterations of the signal

    Args:
        error_iterations (Number): the amount of simulated signals
        input ([Number]): the emitted signal
        classe1 (Number): the first threshold
        classe2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the array containing all the errors across the iterations
    """
    E = []
    for t in range(0, error_iterations):
        Y = gaussian_noise(input, classe1, classe2, mu1, sigma1, mu2, sigma2)
        S = gaussian_classification(Y, classe1, classe2, mu1, sigma1, mu2, sigma2)
        tau = error_rate(input, S)
        E.append(tau)
        E[t] = np.mean(E)
    return E

def title(mu1, sigma1, mu2, sigma2):
    """generates the title string

    Args:
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        String: the generated string
    """
    return 'mu1 = ' + str(mu1) + ', sigma1 = ' + str(sigma1) + '  |  ' + 'mu2 = ' + str(mu2) + ', sigma2 = ' + str(sigma2)

def plot_results(signal_number, errors, mu1, sigma1, mu2, sigma2):
    """plots the results thanks to pyplot

    Args:
        signal_number (Number): the number of the current signal
        errors ([[Number]]): all the mean errors depending on the mus and sigmas
        mu1 ([Number]): the array containing the first mus
        sigma1 ([Number]): the array containing the first sigmas
        mu2 ([Number]): the array containing the second mus
        sigma2 ([Number]): the array containing the second sigmas
    """
    fig, axs = plt.subplots(3, 2)
    fig.suptitle('signal = ' + str(signal_number))

    axs[0, 0].plot(errors[0])
    axs[0, 0].set_title(title(mu1[0], sigma1[0], mu2[0], sigma2[0]))
    axs[0, 0].set(ylabel = str(round(errors[0][-1], 3)))

    axs[0, 1].plot(errors[1], 'tab:orange')
    axs[0, 1].set_title(title(mu1[1], sigma1[1], mu2[1], sigma2[1]))
    axs[0, 1].set(ylabel = str(round(errors[1][-1], 3)))

    axs[1, 0].plot(errors[2], 'tab:green')
    axs[1, 0].set_title(title(mu1[2], sigma1[2], mu2[2], sigma2[2]))
    axs[1, 0].set(ylabel = str(round(errors[2][-1], 3)))

    axs[1, 1].plot(errors[3], 'tab:red')
    axs[1, 1].set_title(title(mu1[3], sigma1[3], mu2[3], sigma2[3]))
    axs[1, 1].set(ylabel = str(round(errors[3][-1], 3)))

    axs[2, 0].plot(errors[4])
    axs[2, 0].set_title(title(mu1[4], sigma1[4], mu2[4], sigma2[4]))
    axs[2, 0].set(ylabel = str(round(errors[4][-1], 3)))

    plt.show()

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
        counts, _ = np.histogram(inp, bins = int(inp.max() + 1), range = (0, int(inp.max())))
        c1, c2 = np.nonzero(counts)[0]
        all_mean_erros = []
        for i in range(0, len(m1)):
            E = mean_error(150, inp, c1, c2, mu1[i], sigma1[i], mu2[i], sigma2[i])
            all_mean_erros.append(E)
        plot_results(signal_number, all_mean_erros, mu1, sigma1, mu2, sigma2)        

# Calling them
main(X, m1, s1, m2, s2)
