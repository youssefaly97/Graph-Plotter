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
    splittingValues = np.zeros((1,len(keywords)),dtype=float)
    
    for l,line in enumerate(filelines):
        for i,keyword in enumerate(keywords):
            if keyword.lower() in line.lower():
                #print("found: "+keyword+" in line: " + line)
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
                    if method[i] == 0 or method[i] == 1:
                        try:
                            #print(float(filelines[l+method[i]].split()[-1]))
                            values[0][i] = float(filelines[l+method[i]].split()[-1])
                            #print(splittingValues)
                        except IndexError: print("File Incomplete1")
                        except ValueError: print("Parse Method Error")
                    else:
                        try:
                            values[0][i] = float(line.split(method[i])[1]) #used when splitting by char
                        except IndexError: print("File Incomplete2")
                        except ValueError: print("Parse Method Error")
                    
                    if splitting[i] == 0 or splitting[i] == 1: splittingValues[0][i] = values[0][i] ## only if it's a splitting variable
                    #print("\t"*i + keyword + ": " + str(values[0][i]))
                    
            if i == 3:#(len(keywords)-1):
                if splitting[i] == 0:# or splitting[i] == 1:
                    #if splitting[i] == 1: values[0][i] = splittingValues[0][i]
                    
                    try:
                        table[0][-1] = values
                    except IndexError:
                        table = np.append(table,[values],1)
                    
                    table = np.append(table,np.zeros((1,1,len(keywords))),1)
                    values = np.zeros((1,len(keywords)),dtype=float)
                if splitting[i] == 1:
                    try:
                        table[0][-1] = splittingValues
                    except IndexError:
                        table = np.append(table,[splittingValues],1)
                    
                #table = np.append(table,np.zeros((1,1,len(keywords))),1)
                #values = np.copy(splittingValues) #########################
                #table = np.append(table,[splittingValues],1)
                        
    #table = np.delete(table,[-1][-1],1)
    return table

#f = open("SolOnly29July3rdAPOut512Threads.txt")
f = open("cooOut512Threads.txt")
lines = f.readlines()
f.close()

Keywords = ["threads","sparsity","compression time taken","solution time taken"]
Case_sensitivity = [0,0,0,0]
Method = [1,0,0,0]
Splitting = [0,1,3,3]

#Keywords = ["threads","sparsity"]
#Case_sensitivity = [0,0]
#Method = [1,0]
#Splitting = [0,3]

#Keywords = ["threads"]
#Case_sensitivity = [0]
#Method = [1]
#Splitting = [0]

table = parse(lines,Keywords,Case_sensitivity,Method,Splitting)