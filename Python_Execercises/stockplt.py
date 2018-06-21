import pandas as pd
import numpy as np
import re
import matplotlib.pyplot as plt

data = pd.read_csv('down.csv')
#print(data)
#print(data.dtypes) 
#due to financial figures been parse as string, need to transform it to float64 to calculate
for col in data.columns[2:]:
    data[col] = data[col].str.replace(r'[^-+\d.]', '').astype(float)
    #print(data[col].)
#print(data)
#print(data.成交股數)
data.plot()
plt.show()