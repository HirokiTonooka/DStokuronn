import pandas as pd
import numpy as np
import sys
from time import sleep
import matplotlib.pyplot as plt
import subprocess as sp
from sklearn.metrics import r2_score as r2
import matplotlib.patches as mpatches


sp.call("wget https://data.covid19india.org/csv/latest/state_wise_daily.csv",shell=True)
sp.call("cat state_wise_daily.csv|sed '2,$s/,-/,/g' >new",shell=True)
sp.call("mv new state_wise_daily.csv",shell=True)
data=pd.read_csv("state_wise_daily.csv")
data.fillna(0,inplace=True)
sp.call("rm state_wise_daily.csv",shell=True)



# print(data)
print(data.plot())
plt.savefig("India_state_wise_daily.png")
print(plt.show())



