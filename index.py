# Importing our modules
from utils.start_calculations import start_calculations
from utils.simulate_signal import simulate_signals
from utils.plot_gaussians import plot_gaussians
from utils.plot_table import plot_table
from utils.signals import load_signals

# Importing all the variables
from variables import ERROR_ITERATIONS
from variables import SIMULATION_SIZE
from variables import SIGMA1
from variables import SIGMA2
from variables import CLASS1
from variables import CLASS2
from variables import P1_P2
from variables import MU1
from variables import MU2

# Import all the signals and storing them in an array
simulated_signals = simulate_signals(SIMULATION_SIZE, CLASS1, CLASS2, P1_P2)

signals = load_signals()

params = {
    'mus1' : MU1,
    'mus2' : MU2,
    'sigmas1' : SIGMA1,
    'sigmas2' : SIGMA2,
}

plot_table(signals, params)

# plot_gaussians(MU1, SIGMA1, MU2, SIGMA2)

# start_calculations(signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)
# start_calculations(simulated_signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)