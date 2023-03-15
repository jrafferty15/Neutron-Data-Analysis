# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 09:47:13 2021

@author: jared
"""

import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')
import numpy as np
from scipy.fft import fft, fftfreq,ifft
from scipy.signal import blackman # other windows??
from scipy import signal 


import assets.class_save_Fig as SAVE #imports figure saving class from assets subdirectory as SAVE
import assets.class_graph as GRAPH
import assets.Create_sine as SINE


## data folder
data_file_path = r'C:\Users\Jared\Documents\Python Scripts\neutron data noise\data_files' +'\\'

## open excel file,saved as 2003 workbook. 
excel_file = data_file_path + 'neutron data.xls'
#excel_file = data_file_path + 'sine_wave_example.xls'

#sneak peak of data
data = pd.read_excel(excel_file)
headers = data.head()


#sinewave input 
y1,x1 =SINE.Create_Sine(1,5,3,50).Create_wfm()

## pull data
x = data.iloc[:,0]
y = data.iloc[:,1]

## series to array
x_arr=np.array(x.values.tolist())
y_arr =np.array(y.values.tolist())
N = len(y_arr)  # Number of sample points
sample_interval = x_arr[1]-x_arr[0] 
fs = 1/sample_interval
T = sample_interval/ N  #sample spacing/points 


########### look to see if any periodicity with FFT and Inverse FFT ######

###### FFT + windowed version ####
window = blackman(N)
yf = fft(y_arr)
yfw =fft(y_arr*window)  


##### only care about + freq terms ####
xf = fftfreq(N, T)[:N//2]
abs_yf = 2.0/N *np.abs(yf[0:N//2])
abs_yfw = 2.0/N *np.abs(yfw[0:N//2])






######### reconstructing the signal in time series, real only #########
def invert_fft(fft_data):
    yinv =ifft(fft_data)
    real = yinv.real
    return real
    
real = invert_fft(yf)
real_w = invert_fft(yfw)


##########    savitsky-golay filer    ##########

def poly_fitler(array,window_length,poly):
    SG_filter = signal.savgol_filter(x = array, polyorder=poly,window_length = window_length)
    return SG_filter
window_length = 11
poly = 5
sg_filter = poly_fitler(y_arr,window_length, poly)


########## construct low pass filter to filter noise   #########

def lowpass_filter(_samples,fs, cutoff_F,yf, order):
    numerator_coeffs, denominator_coeffs = signal.butter(order,cutoff_F,analog= False, fs =fs)
    filtered_signal = signal.lfilter(numerator_coeffs, denominator_coeffs, yf)
    return filtered_signal
    

order = 1
filtered_data = lowpass_filter(N, 5000, 1000, y_arr, order) # fyi, nyqusit theorem fs > 2*(cutoff or signal F) 


## moving average simple(equal w) vs expotential(most recent value has more weight)
window_size = 5
simple_mov_avg =data['Simple moving Avg'] = data.iloc[:,1].rolling(window=window_size).mean()



##################  add signal processing to dataframe  ######################

data['ExpMA'] = data.iloc[:,1].ewm(span = window_size, adjust = False).mean()
data['inverse FFT']= pd.Series(real)
data['inverse FFT, window'] = pd.Series(real_w)
data["low pass filter"] =pd.Series(filtered_data)
data["Savitzky-Golay filter"] =pd.Series(sg_filter)

data["FFTx"] =pd.Series(xf)
data["FFTy"] =pd.Series(abs_yf)


###########   cross correlation method   ###############

correlate = np.correlate(y_arr, y_arr ,mode='full')
data['correlation'] =pd.Series(correlate)



plot_types =  {1: 'raw', 2: 'average', 3: 'ExpMA', 4: "inverse FFT",5: "low pass", 6: "cross correlation",7:"poly-fit", 8 :"FFT" }
path = r'C:\Users\Jared\Pictures\Python Plots' #path to save figure

title = "neutron data noise"

bounds = [0,10],[-2,5]  # x,y axis bounds

FFTbounds =[0,1000],[0,1]

############################ iterates thru dictionary ####################
########## can comment out specific keys if need only specific graphs  #########


for key, value in plot_types.items():
    if key == 1:
        GRAPH.Graphing(data,value,bounds,title).raw() # calls graphing class, sets title, xy bounds. if amending, call correct method + inputs
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot() # calls saving class, using plotname above and dict. value
    elif key == 2:
        GRAPH.Graphing(data,value,bounds,title).simple_avg(window_size) # simple moving avg
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    elif key == 3:
        GRAPH.Graphing(data,value,bounds,title).exp_avg(window_size) # Exp moving avg
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    elif key == 4:
        GRAPH.Graphing(data,value,bounds, title).inverse_FFT () # inverse FFT
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    elif key == 5:
        GRAPH.Graphing(data,value,bounds,title).low_pass(order) # low pass filter
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    elif key == 6:
        GRAPH.Graphing(data,value,bounds,title).correlation() # cross correlation method
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    elif key == 7:
        GRAPH.Graphing(data,value,bounds,title).poly_filter (window_length,poly) # poly filter
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    elif key == 8:
        GRAPH.Graphing(data,value,FFTbounds,title).FFT() # FFT
        plot_name =title +"_"+ value 
        SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    
    
    


# class methods for testing
# GRAPH.Graphing(data,"average",[0,1]).simple_avg(window_size)
#SAVE.Save_Figure(plot_name, plt, path).save_Plot()


# GRAPH.Graphing(data,"FFT",FFTbounds,title).FFT() # FFT
# plot_name ='_test_neutron_' + "FFT"
# SAVE.Save_Figure(plot_name, plt, path).save_Plot()
    
    



