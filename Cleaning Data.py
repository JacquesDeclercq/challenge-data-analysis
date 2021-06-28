import pandas as pd
import numpy as np
import regex as re

path = 'final_list_houses_dataset.csv'
houses_data = pd.read_csv(path, sep=',')
houses_copy = houses_data.copy()
houses_copy = houses_copy.rename(columns={'Price [€]':'price',
                                          'Area [m²]': 'area',
                                          'locality [zip code]':'locality',
                                          'surface of the land [m²]':'surface of the land',
                                          'terrace surface [m²]':'terrace surface',
                                          'garden surface [m²]':'garden surface'})


print(houses_copy.columns)
df = houses_copy[["locality",'fully equipped kitchen', "furnished", 'number of facades']]

def facades_num():
    """This function cleans facades_number by converting values into integers
    and assign '0', 'nan' and 'none' to -999 (=treat as null)"""

    df['number of facades'] = df['number of facades'].apply(str)
    df['number of facades'].replace("(\.0)", "", regex=True, inplace=True)
    df["number of facades"] = df['number of facades'].replace(
        ["nan", "None", "0"], -999
    )  # maybe treat 0 as -999 too?
    df["number of facades"] = df["number of facades"].astype(int)
    return df["number of facades"]

#df.loc["number of facades"] = facades_num()

df.head()
