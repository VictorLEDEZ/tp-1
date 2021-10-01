# Importing our modules
from utils.classes_calculations import classes_calculations
from utils.set_graphs import plot_results
from utils.mean_error import mean_error
from utils.signals import load_signals

# Importing all the variables
from variables import MU1
from variables import MU2
from variables import SIGMA1
from variables import SIGMA2
from variables import ERROR_ITERATIONS

# Import all the signals and storing them in an array
signals = load_signals()

signal_number = 0

for signal in signals:

    signal_number += 1 

    c1, c2 = classes_calculations(signal)
    all_guassian_errors = []
    all_mpm_errors = []

    for i in range(0, len(MU1)):
        E_gaussian, E_mpm = mean_error(ERROR_ITERATIONS, signal, c1, c2, MU1[i], SIGMA1[i], MU2[i], SIGMA2[i])
        all_guassian_errors.append(E_gaussian)
        all_mpm_errors.append(E_mpm)

    plot_results(signal_number, all_guassian_errors, all_mpm_errors, MU1, SIGMA1, MU2, SIGMA2)        