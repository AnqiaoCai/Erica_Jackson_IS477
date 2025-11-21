import pandas as pd

def integrate_datasets(
    copd_path="./Data/cleaned/copd_clean.csv",
    air_path="./Data/cleaned/air_clean.csv",
    merged_path="./Data/merge_data/merged_dataset.csv"
):

    copd_df = pd.read_csv(copd_path)
    air_df = pd.read_csv(air_path)

    merged = pd.merge(copd_df, air_df, on=["State", "County"], how="inner")
    merged.to_csv(merged_path, index=False)
    return merged

if __name__ == "__main__":
    integrate_datasets()
