def add_cities_provinces_to_dataset(df):

    df.set_index(df["locality"], inplace=True)
    data_postcodes = "postalcode_city_state.csv"
    loc_pc = pd.read_csv(data_postcodes, sep=";")
    loc_pc = loc_pc.drop(columns='Unnamed: 3')
    loc_pc = loc_pc.drop(columns='Unnamed: 4')

    merged_df = df.merge(loc_pc, left_index=True, right_on="Postcode")
    merged_df = merged_df.reset_index()
    merged_df = merged_df.drop(columns='locality')
    merged_df = merged_df.rename(columns={'Postcode':'locality'})

    return merged_df
