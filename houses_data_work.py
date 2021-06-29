import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from Creating_state_city_columns import add_cities_provinces_to_dataset

path = 'Dataset\\final_list_houses_dataset.csv'
houses_data = pd.read_csv(path, sep=',')
# copy dataframe
houses_copy = houses_data.copy()
print(houses_copy.columns)

houses_copy = houses_copy.drop(columns='Unnamed: 0')
# del houses_copy[houses_copy['type of property']]
# houses_copy = houses_copy.drop(columns='open fire')

def make_postal_code_second_attempt(df):
    # Create column "province"
    df["province"] = ''
    for index, row in df.iterrows():
        if (row["locality"] >= 1000 & row["locality"] <= 1299):
            row["province"] = "Brussels-Capital"
            continue
        elif (row["locality"] >= 1300 & row["locality"] <= 1499):
            row["province"] = "Walloon Brabant"
            continue
        elif (row["locality"] >= 1500 & row["locality"] <= 1599):
            row["province"] = "Flemish Brabant"
            continue
        elif (row["locality"] >= 2000 & row["locality"] <= 2999):
            row["province"] = "Antwerp"
            continue
        elif (row["locality"] >= 3000 & row["locality"] <= 3399):
            row["province"] = "Flemish Brabant"
            continue
        elif (row["locality"] >= 3500 & row["locality"] <= 3599):
            row["province"] = "Limburg"
            continue
        elif (row["locality"] >= 4000 & row["locality"] <= 4999):
            row["province"] = "Liège"
            continue
        elif (row["locality"] >= 5000 & row["locality"] <= 5999):
            row["province"] = "Namur"
            continue
        elif (row["locality"] >= 6000 & row["locality"] <= 6599):
            row["province"] = "Hainaut"
            continue
        elif (row["locality"] >= 6600 & row["locality"] <= 6999):
            row["province"] = "Luxembourg"
            continue
        elif (row["locality"] >= 7000 & row["locality"] <= 7799):
            row["province"] = "Hainaut"
            continue
        elif (row["locality"] >= 8000 & row["locality"] <= 8899):
            row["province"] = "West Flanders"
            continue

    return df


def make_postal_code_qualitative_value(dataframe):
    # Create column "province"
    dataframe["province"] = ' '
    df = dataframe.sort_values('locality')

    # for row in df['locality']:
    for index, row in df.iterrows():
        # if df.loc[row, 'locality'] >= 1000 & df.loc[row, 'locality'] <= 1299:
        #     df.loc[row, "province"] = "Brussels-Capital"

        if row['locality']>= 1000 and row['locality']<= 1299:
            # row['province'] = "Brussels-Capital"
            # df.loc[index, "province"] = "Brussels-Capital"
            df.at[index, 'province'] = "Brussels-Capital"
            continue
        # elif df.loc[row, 'locality']>= 1300 & df.loc[row, "locality"] <= 1499:
        #     df.loc[row, "province"] = "Walloon Brabant"
        # elif df.loc[row, 'locality']>= 1500 & df.loc[row, "locality"] <= 1999:
        #     df.loc[row, "province"] = "Flemish Brabant"
        # elif (row["locality"] >= 2000 & row["locality"] <= 2999):
        #     row["province"] = "Antwerp"
        # elif (row["locality"] >= 3000 & row["locality"] <= 3499):
        #     row["province"] = "Flemish Brabant"
        # elif (row["locality"] >= 3500 & row["locality"] <= 3999):
        #     row["province"] = "Limburg"
        # elif (row["locality"] >= 4000 & row["locality"] <= 4999):
        #     row["province"] = "Liège"
        # elif (row["locality"] >= 5000 & row["locality"] <= 5999):
        #     row["province"] = "Namur"
        # elif (row["locality"] >= 6000 & row["locality"] <= 6599):
        #     row["province"] = "Hainaut"
        # elif (row["locality"] >= 6600 & row["locality"] <= 6999):
        #     row["province"] = "Luxembourg"
        # elif (row["locality"] >= 7000 & row["locality"] <= 7999):
        #     row["province"] = "Hainaut"
        # elif (row["locality"] >= 8000 & row["locality"] <= 8999):
        #     row["province"] = "West Flanders"
        # elif (row["locality"] >= 9000 & row["locality"] <= 9999):
        #     row["province"] = "East Flanders"

        return df


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
                               'number of bedrooms',
                               'surface of the land'], keep=False)
    return df


def strip_strings(df):
    # strip strings
    columns_to_strip = ['state of the building',
                        'fully equipped kitchen',
                        'type of property',
                        'subtype of property']
    df[columns_to_strip].apply(lambda x: x.str.strip())  # TODO x


def convert_price_from_string_to_int(df):
    # convert columns dtypes
    df.drop(houses_copy.index[houses_copy["price"] == "no"], inplace=True)
    df.price = houses_copy.price.astype(int)
    return df.price


def print_column_values(df, column):
    print("possible values in ", column, df[column].unique())
    print("possible values in ", column, df[column].value_counts('Brussels-Capital'))


def print_column_na_count(df, column):
    print("null count column", column, df[column].isnull().sum())


def print_ratio_without_null(df, column):
    print("ratio without null: ", end=' ')
    print(houses_copy['area'].value_counts(normalize=True) * 100)


def show_lmplot(x_value, y_value, data_value, hue_value):
    sns.lmplot(x_value, y_value, data_value, hue_value, fit_reg=False)
    # sns.lmplot(x='price', y='area',data=houses_copy, hue='state of the building')
    plt.show()


houses_copy = rename_column_titles(houses_copy)
# houses_copy = make_postal_code_qualitative_value(houses_copy)
houses_copy = add_cities_provinces_to_dataset(houses_copy)


# houses_copy = make_postal_code_second_attempt(houses_copy)
# print(houses_copy.head())

# print(houses_copy.columns)
# print(houses_copy['province'].head())
# print(print_column_values(houses_copy, 'province'))
# print(houses_copy.tail())
# print(houses_copy.columns)
# print(houses_copy.groupby('province').count())
# print_duplicate_houses(houses_copy)
houses_copy = drop_duplicate_columns(houses_copy)
strip_strings(houses_copy)
convert_price_from_string_to_int(houses_copy)
# houses_copy.info()
# print(houses_copy.price)
# print(np.where(pd.isnull(houses_copy.price)))
# print_column_values(houses_copy, 'state of the building')
# print_column_na_count(houses_copy, 'state of the building')

# print_column_values(houses_copy, 'area')
# print_column_na_count(houses_copy, 'area')
# print_ratio_without_null(houses_copy, 'area')

# amount nulls in state of the building, not that important. Or graph shows otherwise
# KEEP THIS PLOT: shows the impact of state of the building on house price
# show_lmplot('price', 'area', houses_copy, 'state of the building')

# sns.pairplot(houses_copy)

# facades not that important on price
# sns.lmplot(x='price', y='number of facades',data=houses_copy)

# bedrooms: not the most important one, but it seems to have some impact, up to five rooms
# sns.lmplot(x='price', y='number of bedrooms',data=houses_copy)

# work locality first
# sns.barplot(x='locality', y='price', data=houses_copy, hue='state of the building')
# sns.lmplot(x='fully equipped kitchen', y='state of the building',data=houses_copy)

# print(houses_copy['subtype of property'].unique())

# percentage of the values
# print(houses_copy['state of the building'].value_counts(normalize=True) * 100)
# print(houses_copy.head())
# print(houses_copy.tail())
# houses_pairplot = sns.pairplot(houses_copy)

# print(houses_copy[['subtype of property']].value_counts())


# max prices by area
# print(houses_copy.groupby('area').price.agg(['max']))


# correlation heatmap
# corr = houses_copy.corr()
# sns.heatmap(corr)
# plt.show()

# print(houses_copy.dtypes)

houses_copy = houses_copy[houses_copy['subtype of property'] == 'house']

############### KEEP HOUSES ################
subtype_house_copy = houses_copy[houses_copy['subtype of property'] == 'house']
# print(subtype_house_copy.head())
# print(subtype_house_copy.shape)

subtype_house_copy.info()