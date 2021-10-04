import numpy as np

def simulate_signal(size, class1, class2, p1, p2):
    random_list = np.random.rand(size)
    return class1 * (random_list < p1) + class2 * (random_list > p1)