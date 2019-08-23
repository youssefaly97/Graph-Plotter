#Module: parser
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
    
    for l,line in range(0,len(filelines)),filelines:
        for i,keyword in range(0,len(keywords)),keywords:
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
                                values[i] = float(filelines[l+method[i]])
                                if splitting[i] == 0 or splitting[i] == 1: splittingValues[i] = values[i] ## only if it's a splitting variable
                            except IndexError: print("File Incomplete")
                            except ValueError: print("Parse Method Error")
                        else:
                            try:
                                values[i] = float(line.split(method[i])[1])
                                if splitting[i] == 0 or splitting[i] == 1: splittingValues[i] = values[i] ## only if it's a splitting variable
                            except IndexError: print("File Incomplete")
                            except ValueError: print("Parse Method Error")
                else:
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
                                values[i] = float(filelines[l+method[i]])
                                if splitting[i] == 0 or splitting[i] == 1: splittingValues[i] = values[i] ## only if it's a splitting variable
                            except IndexError: print("File Incomplete")
                            except ValueError: print("Parse Method Error")
                        else:
                            try:
                                values[i] = float(line.split(method[i])[1])
                                if splitting[i] == 0 or splitting[i] == 1: splittingValues[i] = values[i] ## only if it's a splitting variable
                            except IndexError: print("File Incomplete")
                            except ValueError: print("Parse Method Error")
    return table