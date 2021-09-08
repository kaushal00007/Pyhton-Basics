import pandas as pd
df = pd.read_csv('C:\\Users\\KS185348\\Downloads\\exercise_course.csv', sep = ',', header = 0)
df2 = df.groupby('url')['bytes'].sum().reset_index()
df2 = df2.sort_values('bytes', ascending=False)

print(df2)


def usage_by_male(row):
    if row['gender'] == 'Male':
        return row['bytes']
df['data_usage_by_male'] = df.apply(usage_by_male, axis = 1)
def usage_by_female(row):
    if row['gender'] == 'Female':
        return row['bytes']
df['data_usage_by_female'] = df.apply(usage_by_female, axis = 1)

#print(df.groupby('url')['data_usage_by_male', 'data_usage_by_female'].sum() )
print(df.groupby(['url','country'])['data_usage_by_male', 'data_usage_by_female'].sum() )
#print(df.head(10))
