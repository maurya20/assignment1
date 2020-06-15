import pandas as pd
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy import fftpack


#Defining base class
class Implement():
     def __init__(self,vibr):
         self.vibr=vibr

    #Fuction to implemet stft
     def get_stft(self):
         v=self.vibr
         fs = int(input('Implementing STFT\n Enter sampling frequency:'))
         n1 = int(input('Enter dataset range from:'))
         n2 = int(input('Enter dataset range to:'))
         N = v[n1:n2]
         f, t, Zxx = signal.stft(N, fs, nperseg=100)
         data=Zxx
         df=pd.DataFrame(data)
         print(df)
         plt.pcolormesh(t, f, np.abs(Zxx))
         plt.title('STFT Magnitude')
         plt.ylabel('Frequency [Hz]')
         plt.xlabel('Time [sec]')
         return plt.show()


     def get_fft(self):
         vibr=self.vibr
         print("Implementing FFT, find plot ")
         fs = 100  # Sampling frequency
         T = 1 / fs
         N = len(vibr)
         # considerig only positive frequencies
         xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
         vibr_fft = fftpack.fft(vibr)
         fre = np.linspace(0, N, N)
         # Ploting vibration vs timestamp plot
         figure, (fig1, fig2) = plt.subplots(2)
         fig1.plot(fre, vibr)
         fig1.set_title("Vibration vs Timestamp plot")
         fig1.set_ylabel('vibration ')
         # Ploting frequency spectrum
         fig2.stem(xf, 2.0 / N * np.abs(vibr_fft[:N // 2]), use_line_collection=True)
         fig2.set_xlabel('Frequency in (Hz)')
         fig2.set_ylabel('Frequency Spectrum Magnitude')
         return plt.show()





