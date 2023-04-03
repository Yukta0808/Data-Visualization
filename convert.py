import pandas as pd

df = pd.read_csv('Dwarf_Stars.csv')
df = df.dropna()
df.drop(['Unnamed: 0'], axis = 1, inplace = True)

# print(df.head())

df.reset_index(drop = True, inplace = True)

df['Radius'] = 0.102763*df['Radius']
df['Mass'] = df['Mass'].apply(lambda x:x.replace('$','').replace(',','')).astype('float')
df['Mass'] = 0.000954588*df['Mass']

# print(df.dtypes)

df.to_csv('Dwarf_Stars1.csv')
