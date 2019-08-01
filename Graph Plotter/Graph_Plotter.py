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

# printing the list using loop 
for x in range(len(filelist)): 
    print (filelist[x], " : ", x)

print("What is the emu file index? ")
emuFile = int(input())
print ("EMU File: ", filelist[emuFile])

print("What is the x86 file index? ")
x86File = int(input())
print ("EMU File: ", filelist[x86File])


emu = pf.parse(filelist[emuFile])

x86 = pf.parse(filelist[x86File])



#if emu[sp,0,4] != x86[sp,0,4]:

#    print("Matrix Size Mismatch")



#x86 = np.append(np.zeros((2,1,5)),x86,1)

#x86 = np.append(x86,np.zeros((2,6,5)),1)



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

    

mp.plot(np.array((emu[:,0]),dtype=int), #thread count axis

        emu[:,2],                    #EMU clock cycles

        x86[:,2],                    #x86 clock cycles

        op,                                 #operation

        int(emu[0,3]),                   #sparsity

        int(emu[0,4]),                   #matrix size

        ps)
