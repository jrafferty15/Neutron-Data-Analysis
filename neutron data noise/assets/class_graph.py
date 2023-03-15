# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 1:17:13 2021

@author: jared
"""


import matplotlib.pyplot as plt
plt.style.use('seaborn-whitegrid')


# need correct functions added to dataframe get graphing to work. raw should work with just x,y
class Graphing:
    
    
    # methods
    def __init__(self, dataframe, plot_type,bounds, title): #name is string, subplot is plt obj from matplotlib, path is string
        self.dataframe = dataframe
        self.plot_type = plot_type
        self.bounds = bounds
        self.title =title

    #specific graphs
    def raw(self):
        ## graphing on same plot for comparison
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("raw data plotted")

        
    def simple_avg(self,window_size):
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        self.dataframe.plot(kind ="line", x = 'X', y = 'Simple moving Avg', color = 'r', ax =ax, label = str(window_size) + ' point moving average')
        print("simple moving average, window size: " + str(window_size))
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("simple avg plotted")
        
    def exp_avg (self, window_size):
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        self.dataframe.plot(kind = 'line', x = 'X', y ='ExpMA', color = 'k',ax = ax ,label = str(window_size) + " point ExpMoving Avg" )
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("Exp.Moving avg plotted")
        
        
    def inverse_FFT (self):
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        self.dataframe.plot(kind='line', x = "X", y = 'inverse FFT', color = 'gold', ax = ax, label = "inverse FFT")
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("Inverse FFT plotted")
        
        
        
    def low_pass (self, order):
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        self.dataframe.plot(kind='line' , x = 'X', y ="low pass filter", color ='palegreen', ax =ax, label =str(order)+ " order Low Pass")
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("low-pass_filter plotted,"+ str(order)+ "order Low Pass")
        
        
    def correlation (self):
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        self.dataframe.plot(kind='line' , x = 'X', y ="correlation", color ='b', ax =ax, label ='correlation')
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("Cross Correlation plotted")
        
        
    def poly_filter (self,window_length, poly):
        ax = self.dataframe.plot(kind="line", x="X" ,y="Y", color="darkorange", label="raw data")
        self.dataframe.plot(kind ='line', x ='X', y ="Savitzky-Golay filter", color = 'k', ax = ax, label = 'Savitzky-Golay filter')
        ax.set_title(self.title)
        ax.set_xlabel('time')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("Savitsky Golay Filter Plotted window:"+ str(window_length)+ ", poly: "+ str (poly))
        
    def FFT (self):
        ax = self.dataframe.plot(kind="line", x="FFTx" ,y="FFTy", color="k", label="FFT")
        ax.set_title(self.title)
        ax.set_xlabel('Freq (hz)')
        ax.set_ylabel("some unit of measurement")
        ax.set_xlim(self.bounds[0]) # bounds of axis 1
        ax.set_ylim(self.bounds[1]) # bounds of axis 1
        print("FFT plotted")
                                  
        
        
        
    


# test 
#ax =Graphing(data,"raw",[0,1]).raw()

