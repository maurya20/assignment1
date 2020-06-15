import pandas as pd
import numpy as np
from scipy.stats import skew,kurtosis

# reading csv file from project folder
file=pd.read_csv("Vibration.csv")
#applying rolling mean on Vibration_Az
vibr=file["Vibration_Az"].values
r=pd.Series(vibr)
# rolling mean calculation and returning a pandas Dataframe
rm=pd.Series.rolling(r,3).mean()
data={'vibration_Az':vibr,
      'Rolling Mean':rm}
df=pd.DataFrame(data)
print(df)

#Variance calculation
vari=np.var(vibr)
print("Variance of vibration data is :",vari)

#Standard deviation calculation
sd=np.std(vibr)
print("Standard deviation of vibration data is :", sd)

#Skewness and Kurtosis calculation
sk=skew(vibr)
print("Skewness of vibration data is :", sk)
kurt=kurtosis(vibr)
print("Kurtosis of the vibration data is :", kurt)