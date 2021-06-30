import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from Creating_state_city_columns import add_cities_provinces_to_dataset

path = 'Dataset//final_list_houses_dataset.csv'
properties_data = pd.read_csv(path, sep=',')



def rename_column_titles(df):
    df = df.rename(columns={'Price [€]': 'price',
                            'Area [m²]': 'area',
                            'locality [zip code]': 'locality',
                            'surface of the land [m²]': 'surface of the land',
                            'terrace surface [m²]': 'terrace surface',
                            'garden surface [m²]': 'garden surface'})

    return df


def print_duplicate_houses(df):
    print(df.duplicated().value_counts())
    print(df.duplicated(['locality',
                         'price',
                         'number of bedrooms',
                         'surface of the land']).value_counts())


def drop_duplicate_columns(df):
    # choice of columns to decide which properties are duplicates
    df.drop_duplicates(subset=['locality',
                               'price',
                               # 'number of bedrooms',
                               # 'surface of the land'
                               ], keep=False)
    return df


def strip_strings(df):
    # strip strings
    columns_to_strip = ['state of the building',
                        # 'fully equipped kitchen',
                        # 'type of property',
                        'subtype of property']
    df[columns_to_strip].apply(lambda x: x.str.strip())  # TODO x


def convert_price_from_string_to_float(df):
    # convert columns dtypes
    df.drop(properties_data_copy.index[properties_data_copy["price"] == "no"], inplace=True)
    df.price = properties_data_copy.price.astype(float)
    # return df.price


def print_column_values(df, column):
    print("possible values in ", column, df[column].unique())
    print("possible values in ", column, df[column].value_counts('Brussels-Capital'))


def print_column_na_count(df, column):
    print("null count column", column, df[column].isnull().sum())


def print_ratio_without_null(df, column):
    print("ratio without null: ")
    print(df[column].value_counts(normalize=True) * 100)


def show_lmplot(x_value, y_value, data_value, hue_value):
    sns.lmplot(x_value, y_value, data_value, hue_value, fit_reg=False)
    # sns.lmplot(x='price', y='area',data=houses_copy, hue='state of the building')
    plt.show()


def add_price_per_square_meter(df):
    calculation = df['price'] / df['area']
    df['price_meter'] = calculation
    return df


# copy dataframe
properties_data_copy = properties_data.copy()
properties_data_copy = rename_column_titles(properties_data_copy)
convert_price_from_string_to_float(properties_data_copy)

# drop columns that we will not use for general overview.
# We can return to original dataset when we want to add bonuses
# print(houses_copy.isnull().sum())


properties_data_copy_heatmap = properties_data_copy.drop(columns=['Unnamed: 0'])


properties_data_copy = properties_data_copy.drop(columns=['garden surface',
                                        'terrace surface',
                                        'surface of the land',
                                        'Unnamed: 0',
                                        'open fire',
                                        'type of property',
                                        'fully equipped kitchen',
                                        'furnished',
                                        'swimming pool',
                                        'garden',
                                        'terrace'])
                                        # 'number of bedrooms'])

# drop properties with missing area values
properties_data_copy.dropna(subset=['area'], inplace=True)
# add columns to work regionally
properties_data_copy = add_cities_provinces_to_dataset(properties_data_copy)

# cleaning data
properties_data_copy = drop_duplicate_columns(properties_data_copy)
strip_strings(properties_data_copy)
# convert_price_from_string_to_float(properties_data_copy)
properties_data_copy = add_price_per_square_meter(properties_data_copy)

# take a look at 'not specified' state of the building
properties_data_copy['state of the building'].fillna('not specified', inplace=True)
print_ratio_without_null(properties_data_copy, 'state of the building')


# seperate the normal from the rich at 750.000
normal_properties_data = properties_data_copy[properties_data_copy.price < 750000]
# print('normal properties', normal_properties_data.shape)
# print(normal_properties_data['subtype of property'].value_counts())
# print(normal_properties_data.head())
expensive_properties_data = properties_data_copy[properties_data_copy.price >= 750000]
# print('expensive properties', expensive_properties_data.shape)
# print(expensive_properties_data.head())

# exclude area outlier
normal_properties_data = normal_properties_data[normal_properties_data.area < 3000]
print('normal properties', normal_properties_data.shape)


############### KEEP HOUSES ################
houses_copy = properties_data_copy[properties_data_copy['subtype of property'] == 'house']
# print(subtype_house_copy.head())
# print(subtype_house_copy.shape)

# houses_copy.info()
# print(subtype_house_copy.shape)
# print(subtype_house_copy.head())
# print(subtype_house_copy.tail())


def calculate_price_per_meter():
    list_properties = ['house', 'apartment', 'villa']
    copy_df = properties_data_copy[properties_data_copy['subtype of property'].isin(list_properties)]

    copy_df = copy_df.sort_values('price_meter', ascending=False)
    max = copy_df['price_meter'].head()
    # print(copy_df)
    # print(max)


# calculate_price_per_meter()
# pd.set_option('display.max_columns', None)
# print(normal_properties_data.groupby('region').describe())
# print(normal_properties_data.groupby('region').max('price'))
# print(properties_data_copy.groupby('region').describe())

