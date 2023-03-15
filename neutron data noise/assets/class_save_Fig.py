# -*- coding: utf-8 -*-
"""
Created on Wed Jul 14 12:41:23 2021

@author: jared
"""

import os
from datetime import datetime
import matplotlib.pyplot as plt


class Save_Figure:

    # methods
    def __init__(self, name, subplot, path): #name is string, subplot is plt obj from matplotlib, path is string
        self.name = name
        self.subplot = subplot
        self.file_path = path

    def save_Plot(self):
        
        try:
            
            today = datetime.now() #today's date
            
            if os.path.isdir( self.file_path +'\\'+ today.strftime('%m.%d.%Y')) == True: # checks to see if folder exists 
                
                plt.savefig( self.file_path  + '\\' + today.strftime('%m.%d.%Y') + '\\' + self.name , dpi=300) # save file w today's date
                print("saved in plot directory")
                print(self.file_path  + '\\' + today.strftime('%m.%d.%Y') + '\\'+ self.name + ".png") #tells you where saved
            else:
                os.mkdir( self.file_path  + '\\' + today.strftime('%m.%d.%Y'))
                plt.savefig( self.file_path + '\\' + today.strftime('%m.%d.%Y') + '\\'+ self.name + ".png", dpi=300) 
                print("created a new plot directory and saved")
                print(self.file_path + '\\' + today.strftime('%m.%d.%Y') +'\\'+ self.name) # tells you where saved
                
        except:
            print("saving error occured, please check file path")  # most likely error. may need tester + better error handling
        


# test 
#Save_Figure('_test_neutron', plt, r'C:\Users\smsch\Pictures\Python Plots').save_Plot()


