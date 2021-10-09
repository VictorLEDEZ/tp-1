from .plot_graphs import plot_graphs


def plot_signals(signals_guassian_errors, signals_mpm_errors, mus1, sigmas1, mus2, sigmas2):
    """loop for plotting all the signals in order

    Args:
        signals_guassian_errors ([[[Number]]]): mean gaussian errors for all the signals
        signals_mpm_errors ([[[Number]]]): mean mpm errors for all the signals
        mus1 ([Number]): all the mus1
        sigmas1 ([Number]): all the sigmas1
        mus2 ([Number]): all the mus2
        sigmas2 ([Number]): all the sigmas2
    """

    signal_number = 0

    for i in range(0, len(signals_guassian_errors)):

        signal_number += 1

        plot_graphs(
            signal_number, signals_guassian_errors[i], signals_mpm_errors[i], mus1, sigmas1, mus2, sigmas2)
