import numpy as np
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd

# reading csv file from project folder
file = pd.read_csv("Vibration.csv")
vibr = file["Vibration_Az"].values
# Finding top 10 vibration magnitudes
idx = (-vibr).argsort()[:10]
print('Top 10 vibration magnitudes',vibr[idx])

# Storing timestamps in an array
time = []
for i in range(0,524286):
    df=file.loc[i,'date']
    t=pd.Timestamp(df)
    ts=datetime.timestamp(t)
    time=np.append(time,ts)


print('machine failure may occur at:',time[idx])

plt.plot(time[idx],vibr[idx])
plt.title('top 10 max vibration magnitude vs timestamp')
plt.ylabel('Max Vibration')
plt.xlabel('timestamp')
plt.show()