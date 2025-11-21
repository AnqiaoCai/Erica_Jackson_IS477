import pandas as pd

def clean_copd(input_path="./Data/input_data/County_COPD_prevalence.csv", output_path="./Data/cleaned/copd_clean.csv"):

    df = pd.read_csv(input_path)

    df["County"] = df["County"].str.replace(" County", "", regex=False)

    df["State"] = df["StateDesc"]

    df["Percent_COPD"] = pd.to_numeric(df["Percent_COPD"], errors="coerce")

    df = df.dropna(subset=["Percent_COPD"])

    df = df[["State", "County", "Percent_COPD", "Quartile"]]
    df.to_csv(output_path, index=False)
    return df


def clean_air(input_path="./Data/input_data/annual_aqi_by_county_2021.csv", output_path="./Data/cleaned/air_clean.csv"):

    df = pd.read_csv(input_path)

    df["County"] = df["County"].str.replace(" County", "", regex=False)

    df["State"] = df["State"]

    df = df[["State", "County", "Year", "Median AQI", "Days Ozone", "Days PM2.5", "Days NO2", "Days PM10"]].copy()

    for col in ["Median AQI", "Days Ozone", "Days PM2.5", "Days NO2", "Days PM10"]:
        df[col] = pd.to_numeric(df[col], errors="coerce")

    df = df.dropna()
    df.to_csv(output_path, index=False)
    return df


if __name__ == "__main__":
    clean_copd()
    clean_air()
