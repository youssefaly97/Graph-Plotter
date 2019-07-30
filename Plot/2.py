#!/bin/usr/
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:33:03 2019

@author: Youssef Aly
"""
import os
import sys
import matplotlib as plt
import numpy as np

selfname = sys.argv[0].split('/')[-1]

filelist = os.listdir()
filelist.remove(selfname)

try:
    if ("threads" in filelist[0].lower()) and (".txt" in filelist[0].lower()):
        matrix_size = int(filelist[0].split("Threads")[0].split("Out")[-1],10)
        file = open(filelist[0],"r")
        lines = file.readlines()
        file.close()
    else:
        raise IndexError
        
    try:
        #emu_graph = np.array([[[[0,1],[0,1]],[[0,1],[0,1]]], [[[0,1],[0,1]],[[0,1],[0,1]]]]) #[[compression],[solution]]
        emu_graph = np.array([[0,0,0,0,0]])
        threads,old_threads = 0,0
        sparsity,old_sparsity = 0,0
        
        for i,line in enumerate(lines):
            if "number of threads" in line.lower():
                threads = int(lines[i+1],10)
            if "sparsity" in line.lower():
                sparsity = int(line.split(" ")[-1],10)
                #emu_graph[-1][3] = sparsity
            if "compression time taken" in line.lower():
                t_comp = int(line.split(" ")[-1],10)
                emu_graph[-1][1] = t_comp
            if "solution time taken" in line.lower():
                t_sol = int(line.split(" ")[-1],10)
                emu_graph[-1][2] = t_sol
            
            if threads != old_threads:
                emu_graph = np.append(emu_graph,[[threads,0,0,0,matrix_size]],0)
                sparsity = 0;
                old_sparsity = 0;
                old_threads = threads
            if sparsity != old_sparsity:
                emu_graph = np.append(emu_graph,[[threads,0,0,sparsity,matrix_size]],0)
                old_sparsity = sparsity
        
        emu_graph = np.delete(emu_graph,0,0)
               
               
    except:
        print("File is empty")
except FileNotFoundError:
    print("Error: File not found")

except IndexError:
    print("No data files found")