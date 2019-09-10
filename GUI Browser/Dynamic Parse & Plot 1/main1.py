# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 21:57:05 2019

@author: Youssef Aly
"""

import os
import sys
import numpy as np
import myplot as mpl
import myparser as mpr

#import matplotlib as plt

COMPRESSION,SOLUTION = 0,1
SPARSITY0,SPARSITY90 = 0,1
ps,SAVE = 0,1

error = ["File is empty","Error: File not found","No data files found"]
spl = []

#******************************************************************************
op = SOLUTION
#op = COMPRESSION

sp = SPARSITY0
#sp = SPARSITY90

ps = SAVE
#******************************************************************************


selfname = sys.argv[0].split('/')[-1]

try:
    filelist.clear()
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



#(8,10) 512
#(7,9) 1024
##emu = pf.parse(filelist[1])
##x86 = pf.parse(filelist[0])

#512
#x86    = pf.parse(filelist[7])
#x86TH  = pf.parse(filelist[5])
#emu    = pf.parse(filelist[1])
#emuTH  = pf.parse(filelist[3])

#1024

f = open(filelist[6],"r")
x86    = f.readlines()
f.close()

f = open(filelist[4],"r")
x86TH    = f.readlines()
f.close()

f = open(filelist[0],"r")
emu    = f.readlines()
f.close()

f = open(filelist[2],"r")
emuTH    = f.readlines()
f.close()

Keywords = ["threads","sparsity","compression time taken","solution time taken"]
Case_sensitivity = [0,0,0,0]
Method = [1,0,0,0]
Splitting = [0,2,3,3]

t_x86   = mpr.parse(x86  ,Keywords,Case_sensitivity,Method,Splitting)
t_x86TH = mpr.parse(x86TH,Keywords,Case_sensitivity,Method,Splitting)
t_emu   = mpr.parse(emu  ,Keywords,Case_sensitivity,Method,Splitting)
t_emuTH = mpr.parse(emuTH,Keywords,Case_sensitivity,Method,Splitting)
    
if (type(t_emu) == int):
    print(error[t_emu-1])

#plt = mp.plot(np.array((x86[:,0]),dtype=int),                           #X data
#        np.array([emuTH[:,2],x86TH[:,2]*np.ones((x86.shape[0],))]),                              #Y data
#        [0,0],                                                          #Plot Type
#        ["blue","orange"],                                              #Colors
#        ["Threads","Clock Cycles","EMU vs x86 1024","EMU","x86"],       #Names
#        [1,1])                                                          #Labels

plt = mpl.plot(["emu1","emu2","emu3","emu4","emu5","emu6","emu7","emu8"],                           #X data
        np.array([t_x86[0,:,3],t_emu[0,:,3]]),                              #Y data
        [0,0],                                                          #Plot Type
        ["blue","orange"],                                              #Colors
        ["Threads","Clock Cycles","EMU vs x86 1024","EMU","x86"],       #Names
        [1,1])                                                          #Labels

plt.savefig('1024emuVSx86.png',transparent = True)
plt.savefig('1024emuVSx86.svg',transparent = True)