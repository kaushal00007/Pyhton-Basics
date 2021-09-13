import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:\|Pyhton-course\\resulting_data.csv")
plt.xlabel("Net Score")
plt.ylabel("Number of Retweets")
fig,ax=plt.subplots()
my_scatter_plot=ax.scatter(df[" Net Score"],df["Number of Retweets"])

plt.show()