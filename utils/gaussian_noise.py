import numpy as np


def gaussian_noise(input, class1, class2, mu1, sigma1, mu2, sigma2):
    """Changes the input by adding some noise depending on omega1 or omega2

    Args:
        input ([Number]): the emitted signal
        class1 (Number): the first threshold
        class2 (Number): the second threshold
        mu1 (Number): the first mean
        sigma1 (Number): the first standard deviation
        mu2 (Number): the second mean
        sigma2 (Number): the second standard deviation

    Returns:
        [Number]: the recieved signal with some noise due to the communication
    """
    return (input == class1) * np.random.normal(mu1, sigma1, input.shape) + (input == class2) * np.random.normal(mu2, sigma2, input.shape)
