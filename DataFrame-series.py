import pandas as pd
import numpy as np
data = ['state1','state2','state3','state4']
df = pd.DataFrame(data)
#print(df)

#Data Format in List format
data1 = [['state1',100],['state2',120],['state3',130],['state4',90]]
df1 = pd.DataFrame(data1,columns=['Name Of States','Population'],index=['Id1','Id2','Id3','Id4'])
#print(df1)

#DataFrame in dict format
data2 = {'States':['state1','state2','state3','state4'],'Population':[100,30,90,20]}
df2 = pd.DataFrame(data2)
#print(df2)

#Namin the index
data3 = {'States':['state1','state2','state3','state4'],'Population':[100,30,90,20]}
df3 = pd.DataFrame(data3,index=['Id1','Id2','Id3','Id4'])
#print(df3)

#DataFrame from list of dict
data4 = [{'A':1,'B':2,'C':3,'D':4}, {'A':1,'B':2,'C':3,'D':4}]
df4 = pd.DataFrame(data4)
#print(df4)


###########PANDA SERIES#######################
detail = np.array([1,2,3,4,5,6])
ds = pd.Series(detail,index = ['A','B','C','D','E','F'])
#print(ds)

# Series from dict
detail2 = {'x':2,'y':3,'z':4}
ds1 = pd.Series(detail2)
print(ds1)
