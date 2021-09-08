import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('C:\\Users\\KS185348\\Downloads\\sample.csv',sep=',', header=0)
def clean_salary(row):
    Salary = row['Salary'].replace('$','')
    Salary = float(Salary)
    return Salary

df['clean_salary'] = df.apply(clean_salary, axis=1)
def female_salary(row):
    if row['gender']=='Female':
        return row['clean_salary']
df['female_salary'] = df.apply(female_salary, axis=1)

def male_salary(row):
    if row['gender']=='Male':
        return row['clean_salary']
df['male_salary'] = df.apply(male_salary, axis=1)

print(df.groupby('gender')['clean_salary'].mean())
#x = np.array(["Male", "Female"])
#y = np.array([clean_salary])
print(df.groupby(['Job Title','City'])['clean_salary','female_salary','male_salary'].mean())
print(df.loc[(df['clean_salary'] >50000) & (df['clean_salary'] < 80000)])
print(df.sort_values('clean_salary'))
#df.plot(x='Job Title',y=['male_salary', 'female_salary'])
#plt.bar(x,y)
#plt.show()
#print(df.head())
#print(df.columns)