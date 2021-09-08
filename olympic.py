import pandas as pd
import numpy as np
#df= pd.read_csv("C:\\Pyhton-course\\Admission_Predict.csv")
df= pd.read_csv("C:\\Pyhton-course\\Admission_Predict.csv", index_col=0)
#print(df.columns)
#renaming the column names in the dataframe
new_df = df.rename(columns = {'SOP':'Statement of Purpose','LOR ':'Letter of Reference' })
#using the mapper and function for the same
new_df1 = df.rename(mapper = str.strip, axis='columns')
#print(new_df.columns)
#print(new_df.head())

#print(new_df1.columns)
#print(new_df1.head())
#print(df.head())

# change the names to lowercase using list comphrehension
cols = list(df.columns)
cols = [x.lower().strip() for x in cols]
df.columns = cols
#print(df.head())

#Boolean Masking
#admit_mask = df['chance of admit'] > 0.7
#print(df.where(admit_mask).head())
#print(df.where(admit_mask).dropna().head())
#print(type(admit_mask))
#Another way to write the same
print(df[df['chance of admit']>0.7].head())
#print ( ( df[df['chance of admit'].gt(0.7) )& ( df[df['chance of admit']<0.9]))
print(df['chance of admit'].gt(0.7).lt(0.9))
