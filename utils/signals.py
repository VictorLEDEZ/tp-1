import numpy as np


def load_signals():
    """loads all the signals

    Returns:
        [[Number]]: the loaded signals
    """
    signals = []
    signals.append(np.load('./signals/signal.npy'))
    signals.append(np.load('./signals/signal1.npy'))
    signals.append(np.load('./signals/signal2.npy'))
    signals.append(np.load('./signals/signal3.npy'))
    signals.append(np.load('./signals/signal4.npy'))
    signals.append(np.load('./signals/signal5.npy'))
    return signals
