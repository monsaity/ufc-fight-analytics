import pandas as pd

import numpy as np


def load_data(path):
    
    return pd.read_csv(path)


def height_to_cm(value):
    
    if pd.isna(value):
        
        return np.nan

    value = str(value).strip()

    if value in ["--", ""]:
        
        return np.nan

    try:
        
        parts = value.split("'")
        
        feet = int(parts[0].strip())
        
        inches = int(parts[1].replace('"', "").strip())
        
        return round(feet * 30.48 + inches * 2.54, 2)
    
    except:
        
        return np.nan


def weight_to_kg(value):
    
    if pd.isna(value):
        
        return np.nan

    value = str(value).strip().lower()

    if value in ["--", ""]:
        
        return np.nan

    try:
        
        value = value.replace("lbs.", "").replace("lbs", "").strip()
        
        pounds = float(value)
        
        return round(pounds * 0.453592, 2)
    
    except:
        
        return np.nan


def reach_to_cm(value):
    
    if pd.isna(value):
        
        return np.nan

    value = str(value).strip()

    if value in ["--", ""]:
        
        return np.nan

    try:
        
        value = value.replace('"', "").strip()
        
        inches = float(value)
        
        return round(inches * 2.54, 2)
    
    except:
        
        return np.nan


def clean_stance(value):
    
    if pd.isna(value):
        
        return "Unknown"

    value = str(value).strip()

    if value in ["--", ""]:
        
        return "Unknown"

    return value.title()


def clean_dob(value):
    
    return pd.to_datetime(value, errors="coerce")


def preprocess_data(df):
    
    df = df.copy()

    df["FIGHTER"] = df["FIGHTER"].astype(str).str.strip()
    
    df["height_cm"] = df["HEIGHT"].apply(height_to_cm)
    
    df["weight_kg"] = df["WEIGHT"].apply(weight_to_kg)
    
    df["reach_cm"] = df["REACH"].apply(reach_to_cm)
    
    df["stance_clean"] = df["STANCE"].apply(clean_stance)
    
    df["dob_clean"] = df["DOB"].apply(clean_dob)

    df = df.drop_duplicates()

    return df


def save_data(df, path):
    
    df.to_csv(path, index=False)


def main():
    
    df = load_data("data/raw/ufc_fighter_tott.csv")

    print(df.head())
    
    print(df.shape)
    
    print(df.isnull().sum())

    cleaned_df = preprocess_data(df)

    print(cleaned_df.head())
    
    print(cleaned_df.shape)

    save_data(cleaned_df, "data/processed/cleaned_fighter_data.csv")


if __name__ == "__main__":
    
    main()
