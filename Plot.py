import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('final_data_with_gravity.csv')
print(df.head())

df['Distance'] = df['Distance'].apply(lambda x:x.replace('$','').replace(',','')).astype('float')
#print(df.dtypes)

mass = df['Mass'].to_list()
radius = df['Radius'].to_list()
distance = df['Distance'].to_list()
gravity = df['Gravity'].to_list()

mass.sort()
radius.sort()
distance.sort()
gravity.sort()

# plt.plot(radius,mass)
# plt.title("Radius & Mass of the Star")
# plt.xlabel("Radius")
# plt.ylabel("Mass")
# plt.show()

plt.plot(mass,gravity)
plt.title("Mass & Gravity of the Star")
plt.xlabel("Mass")
plt.ylabel("Gravity")
plt.show()