import pandas as pd

filepath = "data/yellow_tripdata_2021-07.csv"

def load_data():
    return pd.read_csv(filepath,low_memory=False)

def preprocess_data(data):
    return data.dropna()

data = load_data()

print(data.shape)

# print(data.head())

