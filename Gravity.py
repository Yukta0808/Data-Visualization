import pandas as pd

df = pd.read_csv('final_data.csv')

#print(df.head())

df.drop(['Unnamed: 0'],axis = 1,inplace = True)
#print(df.head())

#print(df.dtypes)
df['Radius'] = df['Radius'].apply(lambda x:x.replace('$','').replace(',','')).astype('float')

print(df.dtypes)

radius = df['Radius'].to_list()
mass = df['Mass'].to_list()

gravity = []

def unit_conversion(Radius,Mass):
    for i in range(0,len(Radius)-1):
        Radius[i] = Radius[i]*6.957e+8
        Mass[i] = Mass[i]*1.989e+30

unit_conversion(radius,mass)

def gravity_calculation(radius,mass):
    G = 6.674e-11
    for i in range(0,len(mass)):
        g = (mass[i]*G)/((radius[i])**2)
        gravity.append(g) 

gravity_calculation(radius,mass)

df['Gravity'] = gravity        
print(df.head)
df.to_csv('final_data_with_gravity.csv')