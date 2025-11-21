import hashlib

def sha256(file):
    h = hashlib.sha256()
    with open(file, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

print(sha256("./Data/input_data/annual_aqi_by_county_2021.csv"))
print(sha256("./Data/input_data/County_COPD_prevalence.csv"))
print(sha256("./Data/merge_data/merged_dataset.csv"))
