import pandas as pd

import numpy as np



def load_data(path):

    return pd.read_csv(path)



def split_of_stat(value):

    if pd.isna(value):

        return pd.Series([np.nan, np.nan])

    value = str(value).strip()

    if "of" not in value:

        return pd.Series([np.nan, np.nan])

    try:

        parts = value.split("of")

        landed = int(parts[0].strip())

        attempted = int(parts[1].strip())

        return pd.Series([landed, attempted])

    except:

        return pd.Series([np.nan, np.nan])



def percent_to_float(value):

    if pd.isna(value):

        return np.nan

    value = str(value).strip()

    if value in ["---", "--", ""]:

        return np.nan

    try:

        value = value.replace("%", "").strip()

        return float(value)
    except:

        return np.nan



def control_to_seconds(value):

    if pd.isna(value):

        return np.nan

    value = str(value).strip()

    if value in ["--", "---", ""]:

        return np.nan

    try:

        parts = value.split(":")

        minutes = int(parts[0])

        seconds = int(parts[1])

        return minutes * 60 + seconds
    except:

        return np.nan



def to_number(value):

    return pd.to_numeric(value, errors="coerce")



def preprocess_data(df):

    df = df.copy()

    df["FIGHTER"] = df["FIGHTER"].astype(str).str.strip()

    df["KD"] = df["KD"].apply(to_number)

    df["SUB.ATT"] = df["SUB.ATT"].apply(to_number)

    df["REV."] = df["REV."].apply(to_number)

    df[["sig_strikes_landed", "sig_strikes_attempted"]] = df["SIG.STR."].apply(split_of_stat)

    df[["total_strikes_landed", "total_strikes_attempted"]] = df["TOTAL STR."].apply(split_of_stat)

    df[["td_landed", "td_attempted"]] = df["TD"].apply(split_of_stat)

    df["sig_str_pct"] = df["SIG.STR. %"].apply(percent_to_float)

    df["td_pct"] = df["TD %"].apply(percent_to_float)

    df["ctrl_seconds"] = df["CTRL"].apply(control_to_seconds)

    df = df.drop_duplicates()

    return df



def save_data(df, path):

    df.to_csv(path, index=False)



def main():

    df = load_data("data/raw/ufc_fight_stats.csv")

    cleaned_df = preprocess_data(df)

    save_data(cleaned_df, "data/processed/cleaned_fight_stats.csv")



if __name__ == "__main__":

    main()
