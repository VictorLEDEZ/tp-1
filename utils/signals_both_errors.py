from .classes_calculations import classes_calculations
from .mean_error import mean_error


def signals_both_errors(signals, error_iterations, mus1, sigmas1, mus2, sigmas2):
    """caclulates the mean error across all the iterations of the signal with the two methods

    Args:
        signals ([[Number]]): all the signals
        error_iterations (Number): the amount of simulated signals
        mu1s ([Number]): the first means
        sigmas1 ([Number]): the first standard deviations
        mus2 ([Number]): the second means
        sigmas2 ([Number]): the second standard deviations

    Returns:
        [[[Number]]]: the array containing all the errors across the iterations with the two methods
    """

    signals_guassian_errors = []
    signals_mpm_errors = []

    for signal in signals:

        c1, c2 = classes_calculations(signal)
        all_guassian_errors = []
        all_mpm_errors = []

        for i in range(0, len(mus1)):
            E_gaussian, E_mpm = mean_error(
                error_iterations, signal, c1, c2, mus1[i], sigmas1[i], mus2[i], sigmas2[i])
            all_guassian_errors.append(E_gaussian)
            all_mpm_errors.append(E_mpm)

        signals_guassian_errors.append(all_guassian_errors)
        signals_mpm_errors.append(all_mpm_errors)

    return signals_guassian_errors, signals_mpm_errors
