#Module: myplot

import matplotlib.pyplot as plt
import numpy as np


operation = [", Compression", ", Solution"]

def plot(threads,cyclesEMU,cyclesx86,op,sparsity,size):
    x = np.arange(len(threads))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, cyclesEMU, width, label='EMU')
    rects2 = ax.bar(x + width/2, cyclesx86, width, label='x86')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Clock Cycles")
    ax.set_xlabel("Number Of Threads")
    ax.set_title("Sparsity:" + str(sparsity) + ", Matrix Size:" + str(size) + operation[op])
    ax.set_xticks(x)
    ax.set_xticklabels(threads)
    ax.legend()
    
    fig.tight_layout()
    
    plt.show()