import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline
table = pd.read_csv("1617table.csv")
table.head()
plt.bar(x=np.arange(1,6),height=table['Pts'])
plt.title("Premier League 16/17")
plt.xticks(np.arange(1,6), table['Team'], rotation=90)
plt.xlabel("Team")
plt.ylabel("Points")
plt.show()
