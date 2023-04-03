import pandas as pd
import csv

D1 = []
D2 = []

with open('Bright_stars1.csv','r',encoding='utf8')as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        D1.append(i)

with open('Dwarf_Stars1.csv','r',encoding='utf8')as f:
    csv_reader = csv.reader(f)
    for i in csv_reader:
        D2.append(i)

h1 = D1[0]
h2 = D2[0]

data1 = D1[1:]
data2 = D2[1:]

h = h1+h2
data = []

for i in data1: 
    data.append(i)
for j in data2:
    data.append(j)

# print(data)

with open('merged_Data.csv','w',encoding='utf8')as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(data)

df = pd.read_csv('merged_Data.csv')
df.drop(['Unnamed: 0','Unnamed: 6','Star_name.1','Distance.1','Mass.1','Radius.1','Luminosity'],axis = 1, inplace = True)
# print(df.head())
df.to_csv('merged1.csv')