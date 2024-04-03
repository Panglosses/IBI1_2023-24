import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
os.chdir("c:/Users/lhx/Desktop/IBI1/IBI1_2023-24/Practical7")
dalys_data = pd.read_csv("c:/Users/lhx/Desktop/IBI1/IBI1_2023-24/Practical7/dalys-rate-from-all-causes.csv")
dalys_data.head(5)
dalys_data.info()
print(dalys_data.describe())
print(dalys_data.iloc[0:101:10,3])
my_column=[False,False,False,True]
print(dalys_data.loc[0:29,my_column])
china_data=dalys_data.iloc[1140:1170,[0,2,3]]
print(china_data)
np.mean(dalys_data.iloc[1140:1170,3]) #The mean value is 30677.69 which is more than the data in 2019:22270.51, 2019 is below the mean
plt.plot(china_data.Year, china_data.DALYs,'g+')
plt.xticks(china_data.Year,rotation=90)
plt.show()
plt.close()


Select=dalys_data[dalys_data.Year==2019]
low_daly_places = Select[Select['DALYs'] < 18000]
print(low_daly_places['Entity'])