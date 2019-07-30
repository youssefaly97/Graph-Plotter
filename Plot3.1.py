# -*- coding: utf-8 -*-
"""
Created on Mon Jul 29 02:51:22 2019

@author: Youssef Aly
"""
import matplotlib.pyplot as plt
import numpy as np

threads = [ 4
            ,8
            ,16
            ,32
            ,64
            ,128
            ,256
            ,512
            ,1024
            ,2048
            ,4096
            ,8192
            ,16384]

emu = [ 5399
        ,15818
        ,35421
        ,213504
        ,542048
        ,421647
        ,445562
        ,466336
        ,550463
        ,607531
        ,863764
        ,1145368
        ,1782050]

x86 = [ 4842285
        ,5118435
        ,6408045
        ,4259045
        ,4993345
        ,5206425
        ,4228805
        ,5188155
        ,4952920
        ,6241305
        ,10916990
        ,10965500
        ,11845505]

x = np.arange(len(threads))
fig,ax = plt.subplots()
emu_plot = ax.plot(x,emu,label = "EMU")
x86_plot = ax.plot(x,x86,label = "x86")

ax.set_title("Emu vs. x86 Matrices Generation")
ax.set_ylabel("Clock Cycles")
ax.set_xlabel("Matrix Size")
ax.set_xticks(x)
ax.set_xticklabels(threads)

ax.legend()
fig.tight_layout()
plt.savefig("Emu vs. x86 Matrices Generation.svg", transparent = True)
plt.savefig("Emu vs. x86 Matrices Generation.png", dpi = 200, transparent = True)
plt.show()
