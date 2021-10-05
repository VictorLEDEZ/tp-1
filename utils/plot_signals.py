from utils.plot_graphs import plot_graphs

def plot_signals(signals_guassian_errors, signals_mpm_errors, mus1, sigmas1, mus2, sigmas2):
    
    signal_number = 0

    for i in range(0, len(signals_guassian_errors)):

        signal_number += 1 

        plot_graphs(signal_number, signals_guassian_errors[i], signals_mpm_errors[i], mus1, sigmas1, mus2, sigmas2)