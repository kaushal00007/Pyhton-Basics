import matplotlib.pyplot as plt
import numpy as np

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Separator is , and telling that the header is present at 1st Row
sample_DataFrame = pd.read_csv("C:\\Users\KS185348\\OneDrive - NCR Corporation\\Desktop\\POWER-BI\\Pandas\\data.csv",
                          sep = ',',header = 0)

#plt.hist(x)
#sample_DataFrame.plot()
sample_DataFrame["Duration"].plot(kind = 'hist')
plt.show()