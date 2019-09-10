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
x86    = pf.parse(filelist[6])
x86TH  = pf.parse(filelist[4])
emu    = pf.parse(filelist[0])
emuTH  = pf.parse(filelist[2])
    
#if emu[sp,0,4] != x86[sp,0,4]:
#    print("Matrix Size Mismatch")

#x86 = np.append(np.zeros((2,1,5)),x86,1)
#x86 = np.append(x86,np.zeros((2,6,5)),1)

#emu = np.append(emu,np.zeros((1,5)),0)
##x86 = np.delete(x86,-1,0)

if (type(emu) == int):
    print(error[emu-1])

#mp.plot(np.array((emu[0][:,0]),dtype=int),emu[0][:,1],x86[0][:,1],0,int(x[0,0,3]),int(x[0,0,4]))

#mp.plot(np.array((emu[sp][:,0]),dtype=int), #thread count axis
#        emu[sp][:,op+1],                    #EMU clock cycles
#        x86[sp][:,op+1],                    #x86 clock cycles
#        op,                                 #operation
#        int(emu[sp,0,3]),                   #sparsity
#        int(emu[sp,0,4]),                   #matrix size
#        ps)
    
#plt = mp.plot(np.array((x86[:,0]),dtype=int),                             #X data
#        np.array([emu[:,2],x86[:,2],-2.8*x86[:,2],1.6*x86[:,2],x86[:,2]]),                              #Y data
#        [0,0,1,0,0],                                                      #Plot Type
#        ["blue","red","purple","green","orange"],                                          #Colors
#        ["Threads","Clock Cycles","EMU vs AMD","EMU","x86","x88","x89","x80"],
#        [1,0,1,1,0])     #Labels
#
#plt.savefig('test.svg',transparent = True)
    
#plt = mp.plot(np.array((x86[:,0]),dtype=int),                             #X data
#        np.array([emu[:,2],emuTH[:,2],x86[1,2]*np.ones((x86.shape[0],)),x86TH[1,2]*np.ones((x86.shape[0],))]),                              #Y data
#        [0,0,1,1],                                                      #Plot Type
#        ["blue","red","purple","orange"],                                          #Colors
#        ["Threads","Clock Cycles","EMU vs AMD 1024","EMU","EMU TH","x86","x86 TH"],
#        [1,1,1,1])     #Labels

#plt = mp.plot(np.array((x86[:,0]),dtype=int),                             #X data
#        np.array([emu[:,2],emuTH[:,2],x86[:,2],x86TH[:,2]]),                              #Y data
#        [0,0,0,0],                                                      #Plot Type
#        ["blue","red","purple","orange"],                                          #Colors
#        ["Threads","Clock Cycles","EMU vs AMD 1024","EMU","EMU TH","x86","x86 TH"],
#        [0,0,0,0])     #Labels

#plt.savefig('1024allThreads.png',transparent = True)
#plt.savefig('1024allThreads.svg',transparent = True)
    
#plt = mp.plot(np.array((x86[:,0]),dtype=int),                           #X data
#        np.array([emuTH[:,2],emuTH[:,2],emuTH[:,2],x86TH[1,2]*np.ones((x86.shape[0],))]),                              #Y data
#        [0,0,0,1],                                                          #Plot Type
#        ["blue","green","red","orange"],                                              #Colors
#        ["Threads","Clock Cycles","EMU vs x86 1024","EMU","EMU2","EMU3","x86"],       #Names
#        [1,1,1,1])                                                          #Labels

#plt = mp.plot(np.array((x86[:,0]),dtype=int),                           #X data
#        np.array([emuTH[:,2],emuTH[:,2],emuTH[:,2],emuTH[:,2],x86TH[1,2]*np.ones((x86.shape[0],))]),                              #Y data
#        [0,0,0,0,1],                                                          #Plot Type
#        ["blue","green","cyan","green","orange"],                                              #Colors
#        ["Threads","Clock Cycles","EMU vs x86 1024","EMU","EMU2","EMU2.5","EMU3","x86"],       #Names
#        [1,1,1,1,1])                                                          #Labels

plt = mp.plot(np.array((x86[:,0]),dtype=int),                           #X data
        np.array([emuTH[:,2],x86TH[:,2]*np.ones((x86.shape[0],))]),                              #Y data
        [0,0],                                                          #Plot Type
        ["blue","orange"],                                              #Colors
        ["Threads","Clock Cycles","EMU vs x86 1024","EMU","x86"],       #Names
        [1,1])                                                          #Labels

plt.savefig('1024emuVSx86.png',transparent = True)
plt.savefig('1024emuVSx86.svg',transparent = True)