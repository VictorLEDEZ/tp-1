from matplotlib import pyplot as plt
import scipy.stats as stats
import numpy as np

from utils.title import title


def calculate_x(mu, sigma):
    """generates the x axis for the gaussian distribution

    Args:
        mu (Number): the mu of the gaussian
        sigma (Number): the sigma of the gaussian

    Returns:
        [Number]: the x-axis array
    """
    return np.linspace(mu - 3 * sigma, mu + 3 * sigma, 100)


def plot_gaussians(all_mu_1, all_sigma_1, all_mu_2, all_sigma_2):
    """plots the results thanks to pyplot

    Args:
        all_mu_1 ([Number]): the array containing the first mus
        all_sigma_1 ([Number]): the array containing the first sigmas
        all_mu_2 ([Number]): the array containing the second mus
        all_sigma_2 ([Number]): the array containing the second sigmas
    """
    fig, axs = plt.subplots(3, 2)
    fig.suptitle('Gaussian distributions')

    x = calculate_x(all_mu_1[0], all_sigma_1[0])
    axs[0, 0].plot(x, stats.norm.pdf(x, all_mu_1[0], all_sigma_1[0]))
    x = calculate_x(all_mu_2[0], all_sigma_2[0])
    axs[0, 0].plot(x, stats.norm.pdf(x, all_mu_2[0], all_sigma_2[0]), 'r')
    axs[0, 0].set_title(title(all_mu_1[0], all_sigma_1[0],
                        all_mu_2[0], all_sigma_2[0]))

    x = calculate_x(all_mu_1[1], all_sigma_1[1])
    axs[0, 1].plot(x, stats.norm.pdf(x, all_mu_1[1], all_sigma_1[1]))
    x = calculate_x(all_mu_2[1], all_sigma_2[1])
    axs[0, 1].plot(x, stats.norm.pdf(x, all_mu_2[1], all_sigma_2[1]), 'r')
    axs[0, 1].set_title(title(all_mu_1[1], all_sigma_1[1],
                        all_mu_2[1], all_sigma_2[1]))

    x = calculate_x(all_mu_1[2], all_sigma_1[2])
    axs[1, 0].plot(x, stats.norm.pdf(x, all_mu_1[2], all_sigma_1[2]))
    x = calculate_x(all_mu_2[2], all_sigma_2[2])
    axs[1, 0].plot(x, stats.norm.pdf(x, all_mu_2[2], all_sigma_2[2]), 'r')
    axs[1, 0].set_title(title(all_mu_1[2], all_sigma_1[2],
                        all_mu_2[2], all_sigma_2[2]))

    x = calculate_x(all_mu_1[3], all_sigma_1[3])
    axs[1, 1].plot(x, stats.norm.pdf(x, all_mu_1[3], all_sigma_1[3]))
    x = calculate_x(all_mu_2[3], all_sigma_2[3])
    axs[1, 1].plot(x, stats.norm.pdf(x, all_mu_2[3], all_sigma_2[3]), 'r')
    axs[1, 1].set_title(title(all_mu_1[3], all_sigma_1[3],
                        all_mu_2[3], all_sigma_2[3]))

    x = calculate_x(all_mu_1[4], all_sigma_1[4])
    axs[2, 0].plot(x, stats.norm.pdf(x, all_mu_1[4], all_sigma_1[4]))
    x = calculate_x(all_mu_2[4], all_sigma_2[4])
    axs[2, 0].plot(x, stats.norm.pdf(x, all_mu_2[4], all_sigma_2[4]), 'r')
    axs[2, 0].set_title(title(all_mu_1[4], all_sigma_1[4],
                        all_mu_2[4], all_sigma_2[4]))

    plt.show()
