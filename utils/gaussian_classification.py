from scipy import stats as stats
import numpy as np

def gaussian_classification(output, classe1, classe2, mu1, sigma1, mu2, sigma2):
    """Reconstitute the segmented signal S from the recieved signal via classe1 and classe2

    Args:
        output ([Number]): the recieved signal
        classe1 (Number): the first threshold
        classe2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the regenerated signal S
    """
    return np.where(stats.norm.pdf(output, mu1, sigma1) > stats.norm.pdf(output, mu2, sigma2), classe1, classe2)