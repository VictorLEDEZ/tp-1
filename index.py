# Importing our modules
from utils.errors_differences import errors_differences
from utils.plotting.plot_signals import plot_signals
from utils.signals_both_errors import signals_both_errors
from utils.simulate_signal import simulate_signals
from utils.plotting.plot_gaussians import plot_gaussians
from utils.plotting.plot_table import plot_table
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
signals = load_signals()
simulated_signals = simulate_signals(SIMULATION_SIZE, CLASS1, CLASS2, P1_P2)

params = {
    'mus1': MU1,
    'mus2': MU2,
    'sigmas1': SIGMA1,
    'sigmas2': SIGMA2,
}

plot_gaussians(MU1, SIGMA1, MU2, SIGMA2)

# signals_guassian_errors, signals_mpm_errors = signals_both_errors(signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)
# plot_signals(signals_guassian_errors, signals_mpm_errors, MU1, SIGMA1, MU2, SIGMA2)

# signals_guassian_errors, signals_mpm_errors = signals_both_errors(signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)
# values = errors_differences(signals_guassian_errors, signals_mpm_errors)
# plot_table(signals, params, values)

signals_guassian_errors, signals_mpm_errors = signals_both_errors(
    simulated_signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)
plot_signals(signals_guassian_errors, signals_mpm_errors,
             MU1, SIGMA1, MU2, SIGMA2)

# signals_guassian_errors, signals_mpm_errors = signals_both_errors(simulated_signals, ERROR_ITERATIONS, MU1, SIGMA1, MU2, SIGMA2)
values = errors_differences(signals_guassian_errors, signals_mpm_errors)
plot_table(simulated_signals, params, values)
