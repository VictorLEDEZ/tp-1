from matplotlib import pyplot as plt

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

def plot_results(signal_number, errors, all_mu_1, all_sigma_1, all_mu_2, all_sigma_2):
    """plots the results thanks to pyplot

    Args:
        signal_number (Number): the number of the current signal
        errors ([[Number]]): all the mean errors depending on the mus and sigmas
        all_mu_1 ([Number]): the array containing the first mus
        all_sigma_1 ([Number]): the array containing the first sigmas
        all_mu_2 ([Number]): the array containing the second mus
        all_sigma_2 ([Number]): the array containing the second sigmas
    """
    fig, axs = plt.subplots(3, 2)
    fig.suptitle('signal = ' + str(signal_number))

    axs[0, 0].plot(errors[0])
    axs[0, 0].set_title(title(all_mu_1[0], all_sigma_1[0], all_mu_2[0], all_sigma_2[0]))
    axs[0, 0].set(ylabel = str(round(errors[0][-1], 3)))

    axs[0, 1].plot(errors[1], 'tab:orange')
    axs[0, 1].set_title(title(all_mu_1[1], all_sigma_1[1], all_mu_2[1], all_sigma_2[1]))
    axs[0, 1].set(ylabel = str(round(errors[1][-1], 3)))

    axs[1, 0].plot(errors[2], 'tab:green')
    axs[1, 0].set_title(title(all_mu_1[2], all_sigma_1[2], all_mu_2[2], all_sigma_2[2]))
    axs[1, 0].set(ylabel = str(round(errors[2][-1], 3)))

    axs[1, 1].plot(errors[3], 'tab:red')
    axs[1, 1].set_title(title(all_mu_1[3], all_sigma_1[3], all_mu_2[3], all_sigma_2[3]))
    axs[1, 1].set(ylabel = str(round(errors[3][-1], 3)))

    axs[2, 0].plot(errors[4])
    axs[2, 0].set_title(title(all_mu_1[4], all_sigma_1[4], all_mu_2[4], all_sigma_2[4]))
    axs[2, 0].set(ylabel = str(round(errors[4][-1], 3)))

    plt.show()