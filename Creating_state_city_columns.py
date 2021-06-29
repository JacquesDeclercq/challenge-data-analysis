import pandas as pd


def add_cities_provinces_to_dataset(df):

    # df.set_index(df["locality"], inplace=True)
    # df = df.drop(columns='locality')

    data_postcodes = "Dataset\\postalcode_city_state.csv"
    loc_pc = pd.read_csv(data_postcodes, sep=";")
    loc_pc = loc_pc.drop(columns='Unnamed: 3')
    loc_pc = loc_pc.drop(columns='Unnamed: 4')
    loc_pc = loc_pc.drop_duplicates(subset=['Postcode'])
    print(loc_pc.Postcode.value_counts())

    df = df.merge(loc_pc, how='inner', left_on='locality', right_on="Postcode")
    df = df.rename(columns={'City': 'city',
                            'State': 'province'})
    df = df.drop(columns='Postcode')
    print(df.shape)

    return df
