from datetime import datetime
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import kurtosis
from scipy.stats import skew
from class1 import *

# reading csv file from project folder  
file=pd.read_csv("Vibration.csv") 

#applying rolling mean on Vibration_Az
vibr=file["Vibration_Az"].values
r=pd.Series(vibr)




#Storing timestamps in an array
time=[]
for i in range(0,10):
    df=file.loc[i,'date']
    t=pd.Timestamp(df)
    ts=datetime.timestamp(t)
    time=np.append(time,ts)
    
#Rolling mean calculation
a=Implement(r)
print(a.getrm())

#Variance calculation
vari=np.var(r)

print('Variance of Vibration data is:',vari)

#Standard deviation calculation
std=np.std(r)
print('Standard deviation of Vibration data is :',std)

#Skew and Kurtosis calculations 

print('Skew:',skew(r))  

print('Kurtosis:',kurtosis(r))


