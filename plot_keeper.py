import matplotlib.pyplot as plt

from properties_cleaning_analysis import *
from plotting_functions import *

# 1
# show heatmap normal prices
plt.figure(figsize=(12, 15))
sns.heatmap(properties_data_copy_heatmap.corr())
plt.show()

# show distribution
# fig, ax = plt.subplots(1, 2)
# plt.subplot(1,2,1)
sns.displot(data=properties_data_copy, x='price', kind='kde', row_order=None)
# plt.subplot(1,2,2)
sns.displot(data=normal_properties_data, x='price', kind='kde', row_order=None)
plt.show()


# 2
# price by region
show_barplot('region', 'price', normal_properties_data, 'state of the building',
             hue_order_list=['to restore',
                             'to renovate',
                             'to be done up',
                             'just renovated',
                             'good',
                             'as new'])

# 3
# TODO cities (cheapest, most expensive)



# 4
# prices per subtype per region
show_barplot_typeofsubproperty_absoluteprice_region()


# ? subtypes by city ?

# 5
# price square meter
show_barplot_pricespermeter_region()



# 6 bonus



# show_lmplot('area', 'price', normal_properties_data, 'state of the building')
# plot_price_by_area('area', 'price', normal_properties_data, 'province')
# plot_price_by_area('area', 'price', normal_properties_data, 'region')
sns.lmplot(x='area', y='price', data=normal_properties_data, col='region')
# plt.xlim(0, 500)
plt.show()

# HEATMAP
# show_heatmap_subtypehouse()



# show heatmap expensive
# sns.heatmap(expensive_properties_data.corr())
# plt.show()

# BARPLOTS
# show_barplot('province', 'price', subtype_house_copy, 'state of the building',
#              hue_order_list=['to restore',
#                              'to renovate',
#                              'to be done up',
#                              'just renovated',
#                              'good',
#                              'as new'])
# # show_barplot('region', 'price', subtype_house_copy, 'state of the building',
#              hue_order_list=['to restore',
#                              'to renovate',
#                              'to be done up',
#                              'just renovated',
#                              'good',
#                              'as new'])
# show_barplot_typeofsubproperty_absoluteprice_region()


# show_barplot('state of the building', 'price', subtype_houses_copy_statebuilding_fillna)  # see effect 'not specified'
# show_barplot_typeofsubproperty_pricespermeter_region()
# show_barplot_pricespermeter_region()



# BOXPLOT
show_boxplot(properties_data_copy_heatmap)    # shows outliers
# show_boxplot_xaxis('area')            # not saved
# show_boxplot_xaxis('province')        # not saved


# sns.displot(data=houses_copy, x='price', kind='kde', row_order=None)

# sns.displot(data=normal_properties_data, x='price', kind='kde', row_order=None)
# plt.show()
# sns.displot(data=expensive_properties_data, x='price', kind='kde', row_order=None)
