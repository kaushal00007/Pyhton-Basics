import pandas as pd
import numpy as np
#Energy = pd.read_excel("C:\\Pyhton-course\\Assignment-3\\assets\\scimagojr-3.xlsx", engine='openpyxl')
#print(Energy.columns)

x = pd.ExcelFile('C:\\Pyhton-course\\Assignment-3\\assets\\Energy Indicators.xls')
energy = x.parse(skiprows=17, skip_footer=(38))
energy = energy[['Unnamed: 1', 'Petajoules', 'Gigajoules', '%']]
energy.columns = ['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']
energy[['Energy Supply', 'Energy Supply per Capita', '% Renewable']] = energy[
    ['Energy Supply', 'Energy Supply per Capita', '% Renewable']].replace('...', np.NaN).apply(pd.to_numeric)
energy['Energy Supply'] = energy['Energy Supply'] * 1000000
energy['Country'] = energy['Country'].replace({'China, Hong Kong Special Administrative Region': 'Hong Kong',
                                               'United Kingdom of Great Britain and Northern Ireland': 'United Kingdom',
                                               'Republic of Korea': 'South Korea',
                                               'United States of America': 'United States',
                                               'Iran (Islamic Republic of)': 'Iran'})
energy['Country'] = energy['Country'].str.replace(r" \(.*\)", "")

GDP = pd.read_csv('C:\\Pyhton-course\\Assignment-3\\assets\\world_bank.csv', skiprows=4)
GDP['Country Name'] = GDP['Country Name'].replace('Korea, Rep.', 'South Korea')
GDP['Country Name'] = GDP['Country Name'].replace('Iran, Islamic Rep.', 'Iran')
GDP['Country Name'] = GDP['Country Name'].replace('Hong Kong SAR, China', 'Hong Kong')
GDP = GDP[['Country Name', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
GDP.columns = ['Country', '2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']

ScimEn = pd.read_excel(io='C:\\Pyhton-course\\Assignment-3\\assets\\scimagojr-3.xlsx',engine='openpyxl')
ScimEn_m = ScimEn[:15]

df = pd.merge(ScimEn_m, energy, how='inner', left_on='Country', right_on='Country')
final_df = pd.merge(df, GDP, how='inner', left_on='Country', right_on='Country')
final_df = final_df.set_index('Country')
#return merge_2.nsmallest(15, 'Rank')
print(final_df)

