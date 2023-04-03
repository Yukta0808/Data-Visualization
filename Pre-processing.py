import pandas as pd
import csv

df = pd.read_csv('Bright_stars.csv')
df.drop(['Unnamed: 0'], axis = 1, inplace = True)
# print(df.columns)

final_data = df.dropna()
# print(final_data)

final_data.reset_index(drop = True, inplace = True)
final_data.to_csv('Bright_stars1.csv')