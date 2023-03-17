# Neutron-Data-Analysis

**dsp scripts to automate data analysis. Can save multiple figures to get a quick idea of a signal before a more in-depth approach.**

![Alternate image text](https://github.com/jrafferty15/Neutron-Data-Analysis/blob/main/neutron%20data%20noise/readme%20pix/neutron%20data%20noise_poly-fit.png)

*Ex. a Savitzky–Golay filter used to filter noise in a signal*





Mainly made this automate some data analysis needed for a project. Uses example excel file with random data that a collegue gave me. Can be used for anything really that requires digital signal processing for analysis. Used Anaconda environment and Spyder 3.8. this readme will detail how to use. 

0. I am a big fan of anaconda and spyder. Its fairly easy to install various libraries using the navigator. If you have some experience w/python then you can use whatever IDE/Distrubtion is most convenient. 

![Alternate image text](https://github.com/jrafferty15/Neutron-Data-Analysis/blob/main/neutron%20data%20noise/readme%20pix/install%20packages.PNG)



1. You will need to make sure that you have the correct libraries installed to use properly, see below.(Ex. neutron data noise.py)

-Matplotlib
-datetime
-numpy
-scipy
-os

![Alternate image text](https://github.com/jrafferty15/Neutron-Data-Analysis/blob/main/neutron%20data%20noise/readme%20pix/Libraries%20used.PNG)

2. Download the repo and place it in a folder called "C:\Users\ **INSERT USERNAME** \Documents\Python Scripts\". Change the file path to match you machine's path. You will need to amend the script's path to read the example excel file. Otherwise you can amend the code to use the Create_sine.py file to create your own waveform.  


![Alternate image text](https://github.com/jrafferty15/Neutron-Data-Analysis/blob/main/neutron%20data%20noise/readme%20pix/Change%20Path.PNG)

*amend the path on lines 23 and 126 of **neutron data noise.py** to correctly use script. See below*



3.Script has various functions such as FFT,low-pass filter, Polynominal filter, inverse FFT, cross-correlation, and moving averages. You can add functions as needed as long as you add to the dataframe similar to lines 106-118 (neutron data noise.py) then amend class_graph.py file. See below. 


![Alternate image text](https://github.com/jrafferty15/Neutron-Data-Analysis/blob/main/neutron%20data%20noise/readme%20pix/graph%20class.PNG)
 **amend class_graph.py**

4. Once script is ran, it will add figures to a folder called "C:\Users\ **USERNAME** \Pictures\Python Plots\ *todays date* \  " . If the folder doesn't exisit, it will create one for you then add the plots. It uses the *datetime* library, so you could use the hour:minute if you wanted to be more descriptive. 


![Alternate image text](https://github.com/jrafferty15/Neutron-Data-Analysis/blob/main/neutron%20data%20noise/readme%20pix/added%20figs.PNG)

added figures after script is ran. 





