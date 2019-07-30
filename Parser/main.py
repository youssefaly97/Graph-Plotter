# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:57:05 2019

@author: Youssef Aly
"""

import os
import sys
import parse_function as pf
import numpy as np
import myplot as mp
#import matplotlib as plt

error = ["File is empty","Error: File not found","No data files found"]

selfname = sys.argv[0].split('/')[-1]

try:
    filelist.clear()
    x.clear()
except:
    i = 0

for i in range(0,len(os.listdir())):
    if("." in os.listdir()[i] and ".txt" in os.listdir()[i]):
        try:
            filelist.append(os.listdir()[i])
        except NameError:
            filelist = ([os.listdir()[i]])

#for i in range(0,len(filelist)):
    #x = np.append(x,[pf.parse(filelist[i])],2)

x = pf.parse(filelist[1])
if (type(x) == int):
    print(error[x-1])
    
mp.plot(x[0][:,0],x[0][:,1],x[0][:,1],0,x[0,0,3],x[0,0,4])
    
