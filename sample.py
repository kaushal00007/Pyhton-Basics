import pandas as pd


df = pd.read_csv('C:\\Users\\KS185348\\Downloads\\sample.csv',sep=',', header=0)
def clean_salary(row):
    salary = row['Salary'].replace('$','')
    salary = float(salary)
    return salary
df['clean_salary'] = df.apply(clean_salary,axis=1)
df['rank'] = df['clean_salary'].rank(ascending=False)
print(df.sort_values('rank'))
print('AVERAGE SALARY BASED ON GENDER')
#print(df.groupby('gender')['clean_salary'].mean())

def female_salary(row):
    if row['gender'] == 'Female':
        return row['clean_salary']
df['female_salary_avg'] = df.apply(female_salary,axis = 1)

def male_salary(row):
    if row['gender'] == 'Male':
        return row['clean_salary']
df['male_salary_avg'] = df.apply(male_salary,axis = 1)

pd.set_option('display.max_columns', None)
#print(df.groupby(['Job Title','City'])['clean_salary','male_salary_avg','female_salary_avg'].mean())
#print(df)
#print (df.shape)
#df1 = df.drop_duplicates()
#print (df1.shape)
#df2 = df.drop_duplicates(['first_name'], keep='last')
#print (df2.shape)
#print(df.loc[df['clean_salary'] > 50000])

#Reducing the Data
df2 = df.replace(['Male','Female'],['M','F'])
print(df2[['first_name','last_name','gender']])
