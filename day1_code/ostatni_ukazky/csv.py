from csv import DictReader, DictWriter

from pandas import read_csv

df = pd.read_csv("data.csv")

df.to_csv('output.csv', index=False)