from radianclass import *

# reading csv file from project folder  
file=pd.read_csv("Vibration.csv") 
#Storing vibration data in an array
vibr=file["Vibration_Az"].values
r=pd.Series(vibr)

#Implementing STFT on user input sampling frequency and datset range
a=Implement(vibr)
a.get_stft()
#Implementing FFT on whole data
b=Implement(vibr)
b.get_fft()
