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
    table = np.zeros((1,1,len(keywords)),dtype=float)
    values = np.zeros((1,len(keywords)),dtype=float) #line of values, be sure to put this in square brackets before appending to table
    splittingValues = np.zeros((1,len(keywords)),dtype=float)
    
    for l,line in enumerate(filelines):
        if l == 12: break
        for i,keyword in enumerate(keywords):
            if keyword.lower() in line.lower():
                if case_sensitive[i] == 1:
                    if keyword in line:
                        if splitting[i] == 0:
                            table[0][-1] = values
                            table = np.append(table,np.zeros((1,1,len(keywords))),1)
                        if splitting[i] == 1:
                            table[0][-1] = values
                            table = np.append(table,np.zeros((1,1,len(keywords))),1)
                            values = np.copy(splittingValues) #########################
                        if method[i] == 0 or method[i] == 1:
                            try:
                                values[0][i] = float(filelines[l+method[i]])
                                if splitting[i] == 0 or splitting[i] == 1: splittingValues[i] = values[i] ## only if it's a splitting variable
                            except IndexError: print("File Incomplete")
                            except ValueError: print("Parse Method Error")
                        else:
                            try:
                                values[0][i] = float(line.split(method[i])[1])
                                if splitting[i] == 0 or splitting[i] == 1: splittingValues[i] = values[i] ## only if it's a splitting variable
                            except IndexError: print("File Incomplete")
                            except ValueError: print("Parse Method Error")
                else:
                    if splitting[i] == 0:
                        table[0][-1] = values
                        table = np.append(table,np.zeros((1,1,len(keywords))),1)
                    if splitting[i] == 1:
                        table[0][-1] = values
                        #table = np.append(table,np.zeros((1,1,len(keywords))),1)
                        #values = np.copy(splittingValues) #########################
                        table = np.append(table,[splittingValues],1)
                    if method[i] == 0 or method[i] == 1:
                        try:
                            #print(l)
                            #print(float(filelines[l+method[i]].split()[-1]))
                            values[0][i] = float(filelines[l+method[i]].split()[-1])
                            if splitting[i] == 0 or splitting[i] == 1: splittingValues[0][i] = values[0][i] ## only if it's a splitting variable
                        except IndexError: print("File Incomplete1")
                        except ValueError: print("Parse Method Error")
                    else:
                        try:
                            values[0][i] = float(line.split(method[i])[1])
                            if splitting[i] == 0 or splitting[i] == 1: splittingValues[0][i] = values[0][i] ## only if it's a splitting variable
                        except IndexError: print("File Incomplete2")
                        except ValueError: print("Parse Method Error")
    return table

f = open("SolOnly29July3rdAPOut512Threads.txt")
lines = f.readlines()
f.close()

Keywords = ["thread","sparsity","compression time taken","solution time taken"]
Case_sensitivity = [0,0,0,0]
Method = [1,0,0,0]
Splitting = [0,1,3,3]

table = parse(lines,Keywords,Case_sensitivity,Method,Splitting)