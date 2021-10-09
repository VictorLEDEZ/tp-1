import numpy as np


def simulate_signals(size, class1, class2, p1_p2):
    random_list = np.random.rand(size)
    signals = []
    for probabilities in p1_p2:
        signals.append(
            class1 * (random_list < probabilities[0]) + class2 * (random_list > probabilities[0]))
    return signals
