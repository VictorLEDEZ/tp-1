from utils.classes_calculations import classes_calculations
from utils.plot_graphs import plot_graphs
from utils.mean_error import mean_error

def start_calculations(signals, error_iterations, mus1, sigmas1, mus2, sigmas2):

    signal_number = 0

    for signal in signals:

        signal_number += 1 

        c1, c2 = classes_calculations(signal)
        all_guassian_errors = []
        all_mpm_errors = []

        for i in range(0, len(mus1)):
            E_gaussian, E_mpm = mean_error(error_iterations, signal, c1, c2, mus1[i], sigmas1[i], mus2[i], sigmas2[i])
            all_guassian_errors.append(E_gaussian)
            all_mpm_errors.append(E_mpm)

        plot_graphs(signal_number, all_guassian_errors, all_mpm_errors, mus1, sigmas1, mus2, sigmas2)