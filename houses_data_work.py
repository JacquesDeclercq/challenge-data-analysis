import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

path = 'Dataset\\final_list_houses_dataset.csv'
houses_data = pd.read_csv(path, sep=',')


# copy dataframe
houses_copy = houses_data.copy()
houses_copy = houses_copy.rename(columns={'Price [€]':'price',
                                          'Area [m²]': 'area',
                                          'locality [zip code]':'locality',
                                          'surface of the land [m²]':'surface of the land',
                                          'terrace surface [m²]':'terrace surface',
                                          'garden surface [m²]':'garden surface'})

print(houses_copy.columns)

# drop duplicates
# print(houses_copy.duplicated().value_counts())
# print(houses_copy.duplicated([  'locality',
#                                 'price',
#                                 'number of bedrooms',
#                                 'surface of the land']).value_counts())

# choice of columns to decide which properties are duplicates
houses_copy = houses_copy.drop_duplicates(subset = ['locality',
                                'price',
                                'number of bedrooms',
                                'surface of the land'], keep=False)


houses_copy = houses_copy.drop(columns='Unnamed: 0')
# print(houses_copy['number of facades'])
# houses_copy.info()

# strip strings
columns_to_strip = ['state of the building',
                    'fully equipped kitchen',
                    'type of property',
                    'subtype of property']
houses_copy[columns_to_strip].apply(lambda x: x.str.strip())  # TODO x

#
# print(houses_copy[columns_to_strip])
#
# print(houses_copy.dtypes)
#
# convert columns dtypes
# convert_price_str_float = houses_copy['Price [€]'].astype(str).astype(float)
# houses_copy = houses_copy.to_numeric(houses_copy['Price [€]'])

# # houses_copy.to_numeric(houses_copy['price'])
# houses_copy = houses_copy.convert_dtypes()
# houses_copy["price"] = houses_copy.drop(houses_copy.index[houses_copy["price"] == "no"], inplace=True)
houses_copy.drop(houses_copy.index[houses_copy["price"] == "no"], inplace=True)
houses_copy.price = houses_copy.price.astype(int)

houses_copy.info()

print(houses_copy.price)
print(np.where(pd.isnull(houses_copy.price)))

print(houses_copy['state of the building'].unique())


# how many nulls in the column area, what to do with the null values?
# print(houses_copy['area'].isnull().sum())
# print(houses_copy['area'].value_counts(normalize=True) * 100)

# amount nulls in state of the building, not that important
# convert to numbers to be able to see correlation / plot
print(houses_copy['state of the building'].isnull().sum())

# how many nulls in the column state of the building
# print(houses_copy['state of the building'].isnull().sum())

# KEEP THIS PLOT: shows the impact of state of the building on house price
# sns.lmplot(x='price', y='area',data=houses_copy, hue='state of the building', fit_reg=False)
# sns.lmplot(x='price', y='area',data=houses_copy, hue='state of the building')

# g = sns.catplot(x='price',
#                 y='area',
#                 data=houses_copy,
#                 hue='state of the building')  # Color by stage
#                 # col='Stage',  # Separate by stage
#                 # kind='swarm') # Swarmplot


# facades not that important on price
# sns.lmplot(x='price', y='number of facades',data=houses_copy)

# bedrooms: not the most important one, but it seems to have some impact, up to five rooms
# sns.lmplot(x='price', y='number of bedrooms',data=houses_copy)

#
# sns.lmplot(x='locality', y='price',data=houses_copy, hue='state of the building')
# sns.catplot(x='locality', y='price',
#             data=houses_copy,
#             hue='state of the building',
#             col='state of the building',
#             kind='swarm')

# sns.swarmplot(x='price', y='locality', data=houses_copy,
#               hue='state of the building')

# sns.barplot(x='locality', y='price', data=houses_copy, hue='state of the building')

# sns.lmplot(x='fully equipped kitchen', y='state of the building',data=houses_copy)

# percentage of the values
# print(houses_copy['state of the building'].value_counts(normalize=True) * 100)
# print(houses_copy.head())
# print(houses_copy.tail())
# houses_pairplot = sns.pairplot(houses_copy)




# max prices by area
# print(houses_copy.groupby('area').price.agg(['max']))


# correlation heatmap
# corr = houses_copy.corr()
# sns.heatmap(corr)
plt.show()