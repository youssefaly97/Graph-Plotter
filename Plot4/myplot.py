#Module: myplot

import matplotlib
import matplotlib.pyplot as plt
import numpy as np


#operation = [", Compression", ", Solution"]
operation = [", Reading", ", Solution"]

def autolabel(rects,plot):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plot.annotate(str(format(height,'1.1e')),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

def plot(threads,cyclesEMU,cyclesx86,op,sparsity,size,ps):
    if cyclesEMU[0] < 1.0:
        cyclesEMU = np.delete(cyclesEMU,0)
        threads = np.delete(threads,0)
    if cyclesEMU[-1] < 1.0:
        cyclesEMU = np.delete(cyclesEMU,-1)
        threads = np.delete(threads,-1)
    
    x = np.arange(len(threads))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - width/2, cyclesEMU, width, label='EMU')
    rects2 = ax.bar(x + width/2, cyclesx86, width, label='x86')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Clock Cycles")
    ax.set_xlabel("Number Of Threads")
    #ax.set_title("Sparsity:" + str(sparsity) + ", Matrix Size:" + str(size))# + operation[op])
    ax.set_title("Matrix Size:" + str(size) + operation[op])
    ax.set_xticks(x)
    ax.set_xticklabels(threads)
    
    
    cyclesx86_to_plot = np.full_like(cyclesEMU,cyclesx86[1])
    
    #x86_plot = ax.plot(x,cyclesx86_to_plot,label='x86 @ 32 Threads',color="orange")
#    x86_label = ax.annotate(str(format(cyclesx86[1],'1.1e')),
#                xy=((x[0]+x[-1])/2, cyclesx86[1]),
#                xytext=(0, 3),  # 3 points vertical offset
#                textcoords="offset points",
#                ha='center', va='bottom')
    
    #print(x86_plot[0].get_ydata())
    
    ax.legend()
    
    #autolabel(x86_plot)
    autolabel(rects1,ax)
    autolabel(rects2,ax)
    
    #print(rects1[0].get_height())
    
    fig.tight_layout()
    
#    plt.draw()
#    bbox = x86_label.get_window_extent()
#    
#    ax = plt.gca()
#    bbox_data = bbox.transformed(ax.transData.inverted())
#    ax.update_datalim(bbox_data.corners())
#    ax.autoscale_view()
    
    if ps == 1:
        plt.savefig(operation[op].split(' ')[1]+str(size)+'Spar'+str(sparsity)+'.svg',transparent = True)
        plt.savefig(operation[op].split(' ')[1]+str(size)+'Spar'+str(sparsity)+'.png',dpi = 200,transparent = True)
    
    plt.show()