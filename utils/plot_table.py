from numpy.random.mtrand import normal
from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plot_table(x, params):
    
    index = []
    for i in range(0, len(params['mus1'])):
        index.append(
            'm1: ' + str(params['mus1'][i]) + ', ' +
            's1: ' + str(params['sigmas1'][i]) + ', ' +
            'm2: ' + str(params['mus2'][i]) + ', ' +
            's2: ' + str(params['sigmas2'][i])
        )
    
    columns = []
    for i in range(0, len(x)):
        columns.append('s' + str(i + 1) + ': ' + str(len(x[i])))

    data_frame = pd.DataFrame(
        np.random.randn(len(params['mus1']), len(x)),
        index = index,
        columns = columns
    )
    
    values = np.around(data_frame.values, 4)
    norm = plt.Normalize(values.min() - 1, values.max() + 1)
    colours = plt.cm.autumn(values)

    figure = plt.figure(figsize = (15, 8))
    ax = figure.add_subplot(111, frameon = False, xticks = [], yticks = [])

    the_table = plt.table(
        cellText = values,
        rowLabels = data_frame.index,
        colLabels = data_frame.columns,
        colWidths = [0.05] * values.shape[1],
        loc = 'center',
        cellColours = colours
    )

    the_table.auto_set_font_size(False)
    the_table.set_fontsize(16)
    the_table.scale(2, 2)

    plt.show()