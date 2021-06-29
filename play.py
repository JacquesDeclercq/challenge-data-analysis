from houses_data_work import *
from Creating_state_city_columns import *
from plot_keeper import *

#TODO   price // square meter == x=price. y=area
#TODO   nulls
#TODO   columns we do not use: loose?
#TODO   outliers? normalise ~ displot?
#TODO   explain redundant info: locality=city -> region, province // area,price -> price_meter
# colors
# creative questions


# check values like max, min, mean for each column:
x = subtype_house_copy.describe()
print(x)

# to see all of the columns plotted
# sns.pairplot(subtype_house_copy)
# plt.show()

# nulls
print(subtype_house_copy.isnull().sum())
# lose some columns
subtype_house_copy_without_cols = subtype_house_copy.drop(columns=['number of facades',
                                                                   'fully equipped kitchen',
                                                                   'furnished',
                                                                   'swimming pool',
                                                                   'garden',
                                                                   'garden surface',
                                                                   'terrace',
                                                                   'terrace surface',
                                                                   'number of bedrooms',
                                                                   'surface of the land',])

# print(subtype_house_copy_without_cols.shape)
# print(subtype_house_copy_without_cols.head())
# print(subtype_house_copy_without_cols.describe())
# subtype_house_copy_without_cols.info()
# 7438 rows. Area had 1400 nulls, state of the building more but is qualitative

# lose the nulls in area
subtype_house_copy_without_cols_without_area_nulls = subtype_house_copy_without_cols.dropna(subset=['area'])
print(subtype_house_copy_without_cols_without_area_nulls.shape)
subtype_house_copy_without_cols_without_area_nulls.info()

print(subtype_house_copy_without_cols_without_area_nulls['state of the building'].unique())
# no correlation between number of bedrooms and
# sns.lmplot(x='number of bedrooms', y='price', data=subtype_house_copy, hue='furnished')
# plt.show()
# print(subtype_house_copy['garden surface'].unique())

# sns.jointplot(x='price', y='area', kind='kde', data=subtype_house_copy_without_cols_without_area_nulls)
# try to normalise, distribution
# sns.distplot(a= subtype_house_copy_without_cols_without_area_nulls.price,kde=True, hist=True)
# sns.distplot(a= subtype_house_copy_without_cols_without_area_nulls.area,kde=True, hist=True) # deprecated
# sns.displot(data=subtype_house_copy_without_cols_without_area_nulls, x='price', kind='kde', row_order=None)
# plt.show()


##################### APPARTMENTS ######################
appartments = houses_copy.copy()
appartments = appartments[appartments['subtype of property'] == 'apartment']
appartments.info()
# print(appartments['subtype of property'].unique())

# CORR HEATMAP
# sns.heatmap(appartments.corr())


# is there correlation between number of bedrooms for appartments and price?
# fig, ax = plt.subplots()
# sns.barplot(x='number of bedrooms', y='price', data=appartments)
# sns.barplot(x='furnished', y='price', data=appartments)
# ax.set_('Lukt?')
# plt.xticks(rotation=30)
# plt.show()

###################### VILLAS ###########################
villas = houses_copy.copy()
villas = villas[villas['subtype of property'] == 'villa']
villas.info()
print(villas['subtype of property'].unique())

# CORR HEATMAP
# sns.heatmap(villas.corr())
# sns.barplot(x='number of bedrooms', y='price', data=villas)
# plt.show()


###################### prices by subtype #####################
# sns.barplot(x='subtype of property', y='price_meter', data=houses_copy)
# plt.xticks(rotation=30)
# plt.show()