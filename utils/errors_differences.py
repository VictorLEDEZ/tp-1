def errors_differences(signals_guassian_errors, signals_mpm_errors):

    values = []

    for signal in range(0, len(signals_guassian_errors)):

        error_signal = []

        for param in range(0, len(signals_guassian_errors[signal])):

            error_signal.append(
                signals_guassian_errors[signal][param][-1] - signals_mpm_errors[signal][param][-1])

        values.append(error_signal)

    return values
