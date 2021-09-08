import pandas as pd;
data = [["India",130], ["China",140],["Russia",40]]
df = pd.DataFrame(data,columns=["country","population"], dtype=float)
print(df)