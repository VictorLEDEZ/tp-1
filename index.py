# Importing our modules
from utils.gaussian_classification import gaussian_classification
from utils.classes_calculations import classes_calculations
from utils.signals_both_errors import signals_both_errors
from utils.plotting.plot_gaussians import plot_gaussians
from utils.errors_differences import errors_differences
from utils.plotting.plot_signals import plot_signals
from utils.simulate_signal import simulate_signals
from utils.plotting.plot_table import plot_table
from utils.gaussian_noise import gaussian_noise
from utils.mean_error import mean_error
from utils.signals import load_signals
from matplotlib import pyplot as plt

# Importing all the variables
from variables import ERROR_ITERATIONS
from variables import SIMULATION_SIZE
from variables import SIGMA1
from variables import SIGMA2
from variables import CLASS1
from variables import CLASS2
from variables import P1_P2
from variables import MU1
from variables import MU2

# * Import all the signals and storing them in an array
signals = load_signals()
simulated_signals = simulate_signals(SIMULATION_SIZE, CLASS1, CLASS2, P1_P2)

params = {
    'mus1': MU1,
    'mus2': MU2,
    'sigmas1': SIGMA1,
    'sigmas2': SIGMA2,
}

# * I.1.a Function that adds the noise to the signal


# def plot_noised_signal(signal, sigma1, sigma2):
#     mu1, mu2 = class1, class2 = classes_calculations(signal)

#     Y = gaussian_noise(signal, class1, class2, mu1, sigma1, mu2, sigma2)

#     plt.plot(signal, 'r')
#     plt.plot(Y)
#     plt.show()


# plot_noised_signal(signals[0], 4, 5)


# * I.1.c Function that adds the noise to the signal and plots all the signals


# def plot_noised_segmented(signal, sigma1, sigma2):
#     mu1, mu2 = class1, class2 = classes_calculations(signal)

#     Y = gaussian_noise(signal, class1, class2, mu1, sigma1, mu2, sigma2)

#     S = gaussian_classification(Y, class1, class2, mu1, sigma1, mu2, sigma2)

#     plt.plot(signal, 'r')
#     plt.plot(S, 'bo')
#     plt.plot(Y)
#     plt.show()


# plot_noised_segmented(signals[0], 4, 5)


# * I.3 Plots the tau mean curve for a signal


# def plot_tau_mean(signal, mu1, sigma1, mu2, sigma2):
#     class1, class2 = classes_calculations(signal)

#     E_gaussian, _ = mean_error(ERROR_ITERATIONS, signal, class1,
#                                class2, mu1, sigma1, mu2, sigma2)

#     plt.plot(E_gaussian)
#     plt.show()


# plot_tau_mean(signals[0], 127, 1, 128, 1)


# * I.5 Plots the tau mean curves for the 6 signals with the params


# plot_gaussians(MU1, SIGMA1, MU2, SIGMA2)

# signals_guassian_errors, _ = signals_both_errors(
#     signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)

# values = []

# for signal in range(0, len(signals_guassian_errors)):

#     error_signal = []

#     for param in range(0, len(signals_guassian_errors[signal])):

#         error_signal.append(signals_guassian_errors[signal][param][-1])

#     values.append(error_signal)

# plot_table(signals, params, values)


# * II.2 Mean error comparison of the methods for the six signals


signals_guassian_errors, signals_mpm_errors = signals_both_errors(
    signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)

values = errors_differences(signals_guassian_errors, signals_mpm_errors)

plot_gaussians(MU1, SIGMA1, MU2, SIGMA2)

plot_signals(signals_guassian_errors, signals_mpm_errors,
             MU1, SIGMA1, MU2, SIGMA2)

plot_table(signals, params, values)


# * II.4 Mean error comparison of the methods for the five simulated signals


# signals_guassian_errors, signals_mpm_errors = signals_both_errors(
#     simulated_signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)

# values = errors_differences(signals_guassian_errors, signals_mpm_errors)

# plot_gaussians(MU1, SIGMA1, MU2, SIGMA2)

# plot_signals(signals_guassian_errors, signals_mpm_errors,
#              MU1, SIGMA1, MU2, SIGMA2)

# plot_table(simulated_signals, params, values)
