import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from houses_data_work import subtype_house_copy
from houses_data_work import houses_copy
from houses_data_work import plot_price_by_area
from houses_data_work import show_lmplot
from houses_data_work import show_heatmap_subtypehouse
from houses_data_work import *

# plot_price_by_area('area', 'price', subtype_house_copy, 'province')
# show_lmplot('area', 'price', houses_copy, 'state of the building')

# HEATMAP
# show_heatmap_subtypehouse()

# BARPLOTS
# show_barplot('province', 'price', subtype_house_copy, 'state of the building')
# show_barplot('region', 'price', subtype_house_copy, 'state of the building')

# BOXPLOT
# show_boxplot(subtype_house_copy)    # shows outliers
# show_boxplot_xaxis('area')            # not saved
# show_boxplot_xaxis('province')        # not saved
