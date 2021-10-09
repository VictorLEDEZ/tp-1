def errors_differences(signals_guassian_errors, signals_mpm_errors):
    """calculates the delta between all the gaussian and the mpm signal errors

    Args:
        signals_guassian_errors ([[[[Number]]]]): all the gaussian errors
        signals_mpm_errors ([[[[Number]]]]): all the mpm errors

    Returns:
        [[[Number]]]: all the deltas between the mpm and the gaussian
    """

    values = []

    for signal in range(0, len(signals_guassian_errors)):

        error_signal = []

        for param in range(0, len(signals_guassian_errors[signal])):

            error_signal.append(
                signals_guassian_errors[signal][param][-1] - signals_mpm_errors[signal][param][-1])

        values.append(error_signal)

    return values
