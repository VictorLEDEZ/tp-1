import numpy as np


def simulate_signals(size, class1, class2, p1_p2):
    """simulates a signal with two probabilities p1 and p2 to get omega1 or omega2

    Args:
        size (Number): size of the signal
        class1 (Number): the first omega of the signal
        class2 (Number): the second omega of the signal
        p1_p2 ([[Number]]): all the test probabilities

    Returns:
        [[Number]]: all the simulated signals
    """

    random_list = np.random.rand(size)
    signals = []
    for probabilities in p1_p2:
        signals.append(
            class1 * (random_list < probabilities[0]) + class2 * (random_list > probabilities[0]))
    return signals
