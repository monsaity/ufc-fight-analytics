import pandas as pd

import numpy as np



def load_data(path):

    return pd.read_csv(path)



def prepare_fighters(df):

    df = df.copy()

    columns = [
        "FIGHTER",
        "height_cm",
        "weight_kg",
        "reach_cm",
        "stance_clean",
        "dob_clean"
    ]

    df = df[columns]

    df = df.rename(columns={
        "FIGHTER": "fighter_name"
    })

    df["fighter_name"] = df["fighter_name"].astype(str).str.strip()

    df = df.drop_duplicates(subset=["fighter_name"])

    return df



def prepare_fight_results(df):

    df = df.copy()

    columns = [
        "EVENT",
        "BOUT",
        "OUTCOME",
        "WEIGHTCLASS",
        "METHOD",
        "round_clean",
        "time_seconds",
        "fighter_1",
        "fighter_2",
        "winner",
        "loser"
    ]

    df = df[columns]

    df = df.rename(columns={
        "EVENT": "event",
        "BOUT": "bout",
        "OUTCOME": "outcome",
        "WEIGHTCLASS": "weightclass",
        "METHOD": "method"
    })

    df["fighter_1"] = df["fighter_1"].astype(str).str.strip()

    df["fighter_2"] = df["fighter_2"].astype(str).str.strip()

    df["winner"] = df["winner"].astype(str).str.strip()

    df["loser"] = df["loser"].astype(str).str.strip()

    df = df.drop_duplicates()

    return df



def prepare_fight_stats(df):

    df = df.copy()

    columns = [
        "FIGHTER",
        "KD",
        "SUB.ATT",
        "REV.",
        "sig_strikes_landed",
        "sig_strikes_attempted",
        "total_strikes_landed",
        "total_strikes_attempted",
        "td_landed",
        "td_attempted",
        "sig_str_pct",
        "td_pct",
        "ctrl_seconds"
    ]

    df = df[columns]

    df = df.rename(columns={
        "FIGHTER": "fighter_name",
        "KD": "kd",
        "SUB.ATT": "sub_att",
        "REV.": "rev"
    })

    df["fighter_name"] = df["fighter_name"].astype(str).str.strip()

    df = df.drop_duplicates()

    return df



def create_fighter_summary(stats_df):

    summary = stats_df.groupby("fighter_name", as_index=False).agg({
        "kd": "mean",
        "sub_att": "mean",
        "rev": "mean",
        "sig_strikes_landed": "mean",
        "sig_strikes_attempted": "mean",
        "total_strikes_landed": "mean",
        "total_strikes_attempted": "mean",
        "td_landed": "mean",
        "td_attempted": "mean",
        "sig_str_pct": "mean",
        "td_pct": "mean",
        "ctrl_seconds": "mean"
    })

    return summary



def merge_fighter_data(fighters_df, fighter_summary_df):

    merged = fighters_df.merge(
        fighter_summary_df,
        on="fighter_name",
        how="left"
    )

    return merged



def save_data(df, path):

    df.to_csv(path, index=False)



def main():

    fighters = load_data("data/processed/cleaned_fighter_data.csv")

    fight_results = load_data("data/processed/cleaned_fight_results.csv")

    fight_stats = load_data("data/processed/cleaned_fight_stats.csv")

    fighters_prepared = prepare_fighters(fighters)

    fight_results_prepared = prepare_fight_results(fight_results)

    fight_stats_prepared = prepare_fight_stats(fight_stats)

    fighter_summary = create_fighter_summary(fight_stats_prepared)

    fighters_with_stats = merge_fighter_data(fighters_prepared, fighter_summary)

    save_data(fighters_prepared, "data/processed/fighters_final.csv")

    save_data(fight_results_prepared, "data/processed/fight_results_final.csv")

    save_data(fight_stats_prepared, "data/processed/fight_stats_final.csv")

    save_data(fighter_summary, "data/processed/fighter_summary.csv")

    save_data(fighters_with_stats, "data/processed/fighters_with_stats.csv")



if __name__ == "__main__":

    main()
