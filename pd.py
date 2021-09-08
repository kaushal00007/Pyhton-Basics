import pandas as pd
import matplotlib.pyplot as plt
data = [['India',130],['China',140],['Russia',40]]
df = pd.DataFrame(data,columns=['Country','Population'])
print (df)
plt.plot()

mydisc = {'Country':['India','China','Russia'],'Population':[130,140,40]}
df1 = pd.DataFrame(mydisc,index=['1st','2nd','3rd'])
print ("\n", df1)

newdata = [{'x':2,'y':3,'z':4},{'x':8,'y':9,'z':10},{'x':6,'y':7,'z':8}]
df2 = pd.DataFrame(newdata, index=['1st','2nd','3rd'])
print(df2)