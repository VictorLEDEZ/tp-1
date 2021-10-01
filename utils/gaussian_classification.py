from scipy import stats as stats
import numpy as np

def gaussian_classification(output, class1, class2, mu1, sigma1, mu2, sigma2):
    """Reconstitute the segmented signal S from the recieved signal via class1 and class2

    Args:
        output ([Number]): the recieved signal
        class1 (Number): the first threshold
        class2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the regenerated signal S
    """
    return np.where(stats.norm.pdf(output, mu1, sigma1) > stats.norm.pdf(output, mu2, sigma2), class1, class2)