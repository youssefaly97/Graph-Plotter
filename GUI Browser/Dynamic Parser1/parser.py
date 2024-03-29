# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 18:07:49 2019

@author: Youssef Aly
"""
import numpy as np

#method:    0: same line
#           1: next line
#           char delimited

#splitting:     0: split lines with all zeros
#               1: split lines keeping all previous splitters
#               2: split table
#               3: don't use for splitting

def parse (filelines,keywords,case_sensitive,method,splitting):
    table = np.zeros((1,0,len(keywords)),dtype=float)
    values = np.zeros((1,len(keywords)),dtype=float) #line of values, be sure to put this in square brackets before appending to table
    updateValues = np.zeros((1,len(keywords)),dtype=float)
    splittingValues = np.zeros((1,len(keywords)),dtype=float)
    splitFlag = 0
    
    for l,line in enumerate(filelines):
        for i,keyword in enumerate(keywords):
            if keyword.lower() in line.lower():
                #print("found: "+keyword+" in line: " + line)
                if case_sensitive[i] == 1:
                    if keyword in line:
                        if splitting[i] == 0 and not sum(values[0]) == 0:
                            updateValues = values
                            table = np.append(table,[updateValues],1)
                            values = np.zeros((1,len(keywords)),dtype=float)
                            splitFlag = 0
                        if (splitting[i] == 1 or splitting[i] == 2) and splitFlag == 1:
                            table = np.append(table,[values],1)
                            splittingValues = np.zeros((1,len(keywords)),dtype=float)                        
                        if method[i] == 0 or method[i] == 1:
                            try:
                                values[0][i] = float(filelines[l+method[i]].split()[-1])
                            except IndexError: print("File Incomplete1")
                            except ValueError: print("Parse Method Error")
                        else:
                            try:
                                values[0][i] = float(line.split(method[i])[1]) #used when splitting by char
                            except IndexError: print("File Incomplete2")
                            except ValueError: print("Parse Method Error")
                        if splitting[i] == 0 or (splitting[i] == 1 or splitting[i] == 2): splittingValues[0][i] = values[0][i] ## only if it's a splitting variable
                        #print("\t"*i + keyword + ": " + str(values[0][i]) + " I: " + str(i))
                        for n in range(0,len(keywords)):
                            if splitting[n] == 1:
                                values[0][n] = splittingValues[0][n]
                        if (splitting[i] == 1 or splitting[i] == 2):
                            splitFlag = 1
                else:
                    if splitting[i] == 0 and not sum(values[0]) == 0:
                        updateValues = values
                        table = np.append(table,[updateValues],1)
                        values = np.zeros((1,len(keywords)),dtype=float)
                        splitFlag = 0
                    if (splitting[i] == 1 or splitting[i] == 2) and splitFlag == 1:
                        table = np.append(table,[values],1)
                        splittingValues = np.zeros((1,len(keywords)),dtype=float)                        
                    if method[i] == 0 or method[i] == 1:
                        try:
                            values[0][i] = float(filelines[l+method[i]].split()[-1])
                        except IndexError: print("File Incomplete1")
                        except ValueError: print("Parse Method Error")
                    else:
                        try:
                            values[0][i] = float(line.split(method[i])[1]) #used when splitting by char
                        except IndexError: print("File Incomplete2")
                        except ValueError: print("Parse Method Error")
                    if splitting[i] == 0 or (splitting[i] == 1 or splitting[i] == 2): splittingValues[0][i] = values[0][i] ## only if it's a splitting variable
                    #print("\t"*i + keyword + ": " + str(values[0][i]) + " I: " + str(i))
                    for n in range(0,len(keywords)):
                        if splitting[n] == 1:
                            values[0][n] = splittingValues[0][n]
                    if (splitting[i] == 1 or splitting[i] == 2):
                        splitFlag = 1
    
    table = np.append(table,[values],1)
    return table

#f = open("SolOnly29July3rdAPOut512Threads.txt")
f = open("cooOut512Threads.txt")
lines = f.readlines()
f.close()

Keywords = ["threads","sparsity","compression time taken","solution time taken"]
Case_sensitivity = [0,0,0,0]
Method = [1,0,0,0]
Splitting = [0,2,3,3]

#Keywords = ["threads","sparsity"]
#Case_sensitivity = [0,0]
#Method = [1,0]
#Splitting = [0,3]

#Keywords = ["threads"]
#Case_sensitivity = [0]
#Method = [1]
#Splitting = [0]

table = parse(lines,Keywords,Case_sensitivity,Method,Splitting)