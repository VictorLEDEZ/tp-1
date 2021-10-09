from scipy import stats as stats


def map_mpm_2(input, class1, class2, p1, p2, mu1, sigma1, mu2, sigma2):
    """re-finds the original signal with the mpm

    Args:
        input ([Number]): the emitted signal
        class1 (Number): the first threshold
        class2 (Number): the second threshold
        p1 (Number): probability of the first omega
        p2 (Number): probability of the second omega
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the segmented signal
    """

    probability_Y1 = stats.norm.pdf(input, mu1, sigma1)
    probability_Y2 = stats.norm.pdf(input, mu2, sigma2)
    return class1 * (p1 * probability_Y1 > p2 * probability_Y2) + class2 * (p1 * probability_Y1 < p2 * probability_Y2)
