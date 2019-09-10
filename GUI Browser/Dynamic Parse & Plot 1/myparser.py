#Module: myparser
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
    #table_dtype = np.empty((len(keywords),2),dtype='U10')
    
    for k,keyword in enumerate(keywords):
        try:
            table_dtype.append((keyword,'f8'))
        except NameError:
            table_dtype = [(keyword,'f8')]
        
    #print(type(table_dtype))
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
    
    #table = np.array(table,dtype=table_dtype)
    #table = np.sort(table,order="sparsity")
    
    if 2 in splitting:
        for i in range(0,len(keywords)):
            if splitting[i] == 2:
                tableSplitterIndex = i
                break
            
        splitValues = np.empty((0,),float)
        for i in range(0,table.shape[1]):
            splitValue = table[0][i][tableSplitterIndex]
            
            if splitValue not in splitValues:
                splitValues = np.append(splitValues,[splitValue],0)
        
        splitValues = np.sort(splitValues)
        
        tempSplitTable = np.zeros((len(splitValues),1,len(keywords)),float)
        tempSplitCheck = np.zeros((len(splitValues),))
        splitTable = np.empty((len(splitValues),0,len(keywords)),float)
        
        for i in range(0,table.shape[1]):
            for j,splitValue in enumerate(splitValues):
                if table[0][i][tableSplitterIndex] == splitValue:
                    if tempSplitCheck[j] == 1:
                        splitTable = np.append(splitTable,tempSplitTable,1)
                        tempSplitCheck = np.zeros((len(splitValues),))
                        tempSplitTable = np.zeros((len(splitValues),1,len(keywords)),float)
                    tempSplitTable[j] = table[0][i]
                    tempSplitCheck[j] = 1
                    #print("Should append:\t" + str(table[0][i]) + "\tto split table at index: " + str(j))
                if np.sum(tempSplitCheck) == len(splitValues):
                    splitTable = np.append(splitTable,tempSplitTable,1)
                    tempSplitCheck = np.zeros((len(splitValues),))
                    tempSplitTable = np.zeros((len(splitValues),1,len(keywords)),float)
        
        if i == (table.shape[1] - 1) and not np.sum(tempSplitCheck) == 0: #reached end of table without appending all values
            splitTable = np.append(splitTable,tempSplitTable,1)
        
        table = splitTable
#1 2 3 4
#1 2 3 4
#0 2 3 0 #done
#0 2 3 0 #not yet, check it tempSplitCheck[j] is already 1 -- done and needs testing with more than 2 sparsities
    return table