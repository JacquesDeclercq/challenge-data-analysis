import matplotlib.pyplot as plt

from properties_cleaning_analysis import *

def show_heatmap_subtypehouse():
    plt.figure(figsize=(12, 15))
    copy = houses_copy.copy()
    copy = copy.drop(columns='locality')
    corr = copy.corr()
    sns.heatmap(corr)
    plt.show()


def plot_price_by_area(x_val, y_val, data_val, hue_val):
    sns.lmplot(x=x_val, y=y_val, data=data_val, hue=hue_val, col=hue_val)
    plt.show()


def show_barplot(x_val, y_val, data_val, hue_value=None, hue_order_list=None):
    plt.figure(figsize=(20, 5))
    plt.title('prices by region (prices below € 750.000)')
    sns.barplot(x=x_val, y=y_val, data=data_val, palette="Blues", hue=hue_value, hue_order=hue_order_list)
    plt.xlabel(str(x_val))
    plt.ylabel(str(y_val))
    plt.show()


def show_boxplot(data_val):
    plt.figure(figsize=(20, 5))
    sns.boxplot(data=data_val)
    plt.show()


def show_boxplot_xaxis(column):
    plt.figure(figsize=(5, 20))
    copy_df = houses_copy[column]
    sns.boxplot(data=copy_df)
    plt.xlabel(str(column))
    plt.show()


def show_barplot_stats():
    mean = round(houses_copy.price.mean(), 2)
    max = round(houses_copy.price.max(), 2)
    min = round(houses_copy.price.min(), 2)
    print(mean, max, min)

    sns.countplot(x='price',
                  y='province',
                  data=houses_copy)


def show_barplot_typeofsubproperty_absoluteprice_region():
    list_properties = ['house', 'apartment', 'villa']
    copy_df = properties_data_copy[properties_data_copy['subtype of property'].isin(list_properties)]
    sns.barplot(x='region', y='price', data=copy_df, hue="subtype of property", palette="Blues")
    plt.ylabel('price in millions')
    plt.title('prices per property type per region')
    plt.show()


def show_barplot_typeofsubproperty_pricespermeter_region():
    # price based on type of property and region
    # ax = plt.subplot()
    list_properties = ['house', 'apartment', 'villa']
    copy_df = properties_data_copy[properties_data_copy['subtype of property'].isin(list_properties)]
    sns.barplot(x='region', y='price_meter', data=copy_df, hue="subtype of property", palette="Blues")
    # ax.set_xticklabels(["Appartment", "House"])
    # plt.xlabel("Type of property")
    # plt.ylabel("Price")
    plt.show()


def show_barplot_pricespermeter_region():
    # price based on type of property and region
    # ax = plt.subplot()
    list_properties = ['house', 'apartment', 'villa']
    copy_df = properties_data_copy[properties_data_copy['subtype of property'].isin(list_properties)]
    sns.barplot(x='region', y='price_meter', data=copy_df, palette="Blues",
                hue="subtype of property", hue_order=[  'apartment',
                                                        'house',
                                                        'villa'])
    plt.ylabel("price per square meter")
    plt.title('price per square meter for property types and region')
    plt.show()