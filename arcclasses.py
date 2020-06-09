import pandas as pd

#Defining base class
class Implement():
     def __init__(self,r):
         self.r=r
    
    
    #function to get rolling mean 
     def getrm(self):
         rm=pd.Series.rolling(self.r,6).mean()
         return rm