# -*- coding: utf-8 -*-

"""
Created on Wed Jul 14 2:21:11 2021

@author: jared
"""


import numpy as np
import matplotlib.pyplot as plt


class Create_Sine:
    
    # methods
    def __init__(self, freq,N,amp,fs): #makes a sine wave to use instead of using data file
       
        self.freq = freq
        self.N = N
        self.amp = amp
        self.fs =fs
        print((1/fs)*N)

    def Create_wfm(self):
        theta = 0
        x = np.arange(0,self.N,1/self.fs)
        signal = self.amp * np.sin(2 * np.pi * self.freq * x + theta)
        
        return signal,x
    
    
    
#test 
# y,x =Create_Sine(1,5,3,50).Create_wfm()

# plt.plot(x,y)
