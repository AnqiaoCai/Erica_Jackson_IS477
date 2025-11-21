import hashlib

def sha256(file):
    h = hashlib.sha256()
    with open(file, 'rb') as f:
        h.update(f.read())
    return h.hexdigest()

print(sha256("input_data/copd.csv"))
print(sha256("input_data/air_quality.csv"))
