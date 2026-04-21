import pandas as pd

import numpy as np



def load_data(path):

    return pd.read_csv(path)



def split_fighters(value):

    if pd.isna(value):

        return pd.Series([np.nan, np.nan])

    value = str(value)

    if "vs." in value:

        parts = value.split("vs.")

    elif "VS." in value:

        parts = value.split("VS.")

    else:

        return pd.Series([np.nan, np.nan])

    fighter_1 = parts[0].strip()

    fighter_2 = parts[1].strip()

    return pd.Series([fighter_1, fighter_2])



def get_winner(row):

    if row["OUTCOME"] == "W/L":

        return row["fighter_1"]

    if row["OUTCOME"] == "L/W":

        return row["fighter_2"]

    return np.nan



def get_loser(row):

    if row["OUTCOME"] == "W/L":

        return row["fighter_2"]

    if row["OUTCOME"] == "L/W":

        return row["fighter_1"]

    return np.nan



def clean_round(value):

    return pd.to_numeric(value, errors="coerce")



def time_to_seconds(value):

    if pd.isna(value):

        return np.nan

    try:

        parts = str(value).split(":")

        minutes = int(parts[0])

        seconds = int(parts[1])

        return minutes * 60 + seconds

    except:

        return np.nan



def preprocess_data(df):

    df = df.copy()

    df[["fighter_1", "fighter_2"]] = df["BOUT"].apply(split_fighters)

    df["winner"] = df.apply(get_winner, axis=1)

    df["loser"] = df.apply(get_loser, axis=1)

    df["round_clean"] = clean_round(df["ROUND"])

    df["time_seconds"] = df["TIME"].apply(time_to_seconds)

    df["METHOD"] = df["METHOD"].astype(str).str.strip()

    df["WEIGHTCLASS"] = df["WEIGHTCLASS"].astype(str).str.strip()

    df = df.drop_duplicates()

    return df



def save_data(df, path):

    df.to_csv(path, index=False)



def main():

    df = load_data("data/raw/ufc_fight_results.csv")

    cleaned_df = preprocess_data(df)

    save_data(cleaned_df, "data/processed/cleaned_fight_results.csv")



if __name__ == "__main__":

    main()
