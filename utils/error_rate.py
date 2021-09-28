import numpy as np

def error_rate(emitted, received):
    """calculates the Bit Error Rate (BER) between the emitted and the recieved signal

    Args:
        emitted ([Number]): the clean emited signal
        received ([Number]): the segmented signal

    Returns:
        Number: the Bit Error Rate
    """
    return np.count_nonzero(received - emitted) / len(emitted)
