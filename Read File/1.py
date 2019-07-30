#!/bin/usr/
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 17:33:03 2019

@author: Youssef Aly
"""
import os
import sys

selfname = sys.argv[0].split('/')[-1]

try:
    file = open("cooOut512Threads.txt","r")
except FileNotFoundError:
    print("Error: File not found")
    
lines = file.readlines()

print(lines[2])
    
