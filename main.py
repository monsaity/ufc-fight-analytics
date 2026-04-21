from src.preprocess import main as preprocess_fighters_main

from src.load_data import main as preprocess_fight_results_main

from src.stats_analysis import main as preprocess_fight_stats_main

from src.feature_engineering import main as feature_engineering_main



def main():

    preprocess_fighters_main()

    preprocess_fight_results_main()

    preprocess_fight_stats_main()

    feature_engineering_main()

    print("Data pipeline completed successfully.")



if __name__ == "__main__":

    main()
