#Module: parse_function.py
#!/bin/usr/
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:33:03 2019

@author: Youssef Aly
"""
import numpy as np

def parse(filename):
    try:
        if ("threads" in filename.lower()) and (".txt" in filename.lower()):
            matrix_size = int(filename.split("Threads")[0].split("Out")[-1],10)
            file = open(filename,"r")
            lines = file.readlines()
            file.close()
        else:
            raise IndexError
            
        try:
            table = np.array([[0,0,0,0,0]])
            threads,old_threads = 0,0
            sparsity,old_sparsity = 0,0
            
            for i,line in enumerate(lines):
                if "number of threads" in line.lower():
                    threads = int(lines[i+1],10)
                if "sparsity" in line.lower():
                    sparsity = int(line.split(" ")[-1],10)
                if "compression time taken" in line.lower():
                    t_comp = int(line.split(" ")[-1],10)
                    table[-1][1] = t_comp
                if "solution time taken" in line.lower():
                    t_sol = int(line.split(" ")[-1],10)
                    table[-1][2] = t_sol
                
                if threads != old_threads:
                    table = np.append(table,[[threads,0,0,0,matrix_size]],0)
                    sparsity = 0;
                    old_sparsity = 0;
                    old_threads = threads
                if sparsity != old_sparsity:
                    table = np.append(table,[[threads,0,0,sparsity,matrix_size]],0)
                    old_sparsity = sparsity
            
            table = np.delete(table,0,0)
            
            for i in range(0,table.shape[0]):
                if table[i][3] == 0:
                    try:
                        sparsity0 = np.append(sparsity0,[table[i]],0)
                    except:
                        sparsity0 = np.array([table[i]])
                if table[i][3] == 90:
                    try:
                        sparsity90 = np.append(sparsity90,[table[i]],0)
                    except:
                        sparsity90 = np.array([table[i]])
                
            
            return np.array([sparsity0,sparsity90])
            #return table
        except:
            return 1
            #print("File is empty")
    except FileNotFoundError:
        return 2
        #print("Error: File not found")
    
    except IndexError:
        return 3
        #print("No data files found")