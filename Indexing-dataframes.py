import pandas as pd
import numpy as np
#df= pd.read_csv("C:\\Pyhton-course\\Admission_Predict.csv")
df= pd.read_csv("C:\\Pyhton-course\\presidents.csv")
#df['Serial Number'] = df.index

#setting the 'chance of admit' as index now
#df = df.set_index('Chance of Admit ')
#df['First'] = df['President']
def splitName(row):
    row['First'] = row['President'].split(" ")[0]
    row['Last']  = row['President'].split(" ")[-1]
    return row
df =df.apply(splitName, axis='columns')
print(df.columns)
print(df.head())