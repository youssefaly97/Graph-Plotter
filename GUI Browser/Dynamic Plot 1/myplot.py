#Module: myplot

import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def bar_autolabel(rects,color,plot,figure):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        label = 0
        if(height >= 0):
            label = plot.annotate(str(format(height,'1.1e'))[0:4]+str(format(height,'1.1e'))[-1],
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',color=color,rotation = 90)
        else:
            label = plot.annotate(str(format(height,'1.1e'))[0:5]+str(format(height,'1.1e'))[-1],
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',color=color)
        
        figure.tight_layout()
        #plt.draw()
        bbox = label.get_window_extent()
        ax = plt.gca()
        bbox_data = bbox.transformed(ax.transData.inverted())
        ax.update_datalim(bbox_data.corners())
        ax.autoscale_view()
        
def plot_autolabel(pointsx,pointsy,color,plot,figure):
    points = np.array((pointsx,pointsy)).T
    for point in points:
        if(point[1] >= 0):
            label = plot.annotate(str(format(point[1],'1.1e'))[0:4]+str(format(point[1],'1.1e'))[-1],
                        xy=(point),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',rotation = 90, color=color)
        else:
            label = plot.annotate(str(format(point[1],'1.1e'))[0:5]+str(format(point[1],'1.1e'))[-1],
                        xy=(point),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom',rotation = 90, color=color)
        
        figure.tight_layout()
        #plt.draw()
        bbox = label.get_window_extent()
        ax = plt.gca()
        bbox_data = bbox.transformed(ax.transData.inverted())
        ax.update_datalim(bbox_data.corners())
        ax.autoscale_view()

#labels: x axis title, y axis title, graph title, series 1 name, .., series n name
#types: 0 bar, 1 plot, 2 scatter
def plot(xdata,ydata,types,colors,labels,plot_labels):
    xticks = np.arange(len(xdata))
    
    try:
        series_count = ydata.shape[0]
    except IndexError: #if only 1 series is to be displayed
        series_count = 1
    
    bar_count = types.count(0)
    
    width = 1/(1+bar_count)
    
    fig, ax = plt.subplots()
    
    bar_index = 0
    for i in range(0,series_count):
        this_plot = 0
        if(types[i] == 0):
            this_plot = ax.bar(xticks + width*(bar_index - ((bar_count-1)/2)),ydata[i],width,label = labels[i+3],color = colors[i])
            if(plot_labels[i] == 1):
                bar_autolabel(this_plot,colors[i],ax,fig)
            bar_index = bar_index + 1
        if(types[i] == 1):
            this_plot = ax.plot(xticks,ydata[i],label = labels[i+3],color = colors[i])
            if(plot_labels[i] == 1):
                plot_autolabel(xticks,ydata[i],colors[i],ax,fig)
        
        #scatter plot
        #if(types[i] == 0): this_plot = ax.bar(x + (width*i - bar_count),ydata[i],width,label = labels[i+4])
        
        try:
            plots = [plots,this_plot]
        except NameError:
            plots = this_plot
    
    ax.set_xlabel(labels[0])
    ax.set_ylabel(labels[1])
    ax.set_title(labels[2])
    ax.set_xticks(xticks)
    ax.set_xticklabels(xdata)    
    
    ax.legend()
    fig.tight_layout()
    plt.show()
    
    
###############################################################################
def plot_old(threads,cyclesEMU,cyclesx86,op,sparsity,size,ps):
    if cyclesEMU[0] < 1.0:
        cyclesEMU = np.delete(cyclesEMU,0)
        threads = np.delete(threads,0)
    if cyclesEMU[-1] < 1.0:
        cyclesEMU = np.delete(cyclesEMU,-1)
        threads = np.delete(threads,-1)
    
    x = np.arange(len(threads))  # the label locations
    width = 0.35  # the width of the bars
    
    fig, ax = plt.subplots()
    rects1 = ax.bar(x - 0*width/2, cyclesEMU, width, label='EMU')
    #rects2 = ax.bar(x + width/2, cyclesx86, width, label='x86')
    
    # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel("Clock Cycles")
    ax.set_xlabel("Number Of Threads")
    #ax.set_title("Sparsity:" + str(sparsity) + ", Matrix Size:" + str(size))# + operation[op])
    ax.set_title("Matrix Size:" + str(size) + operation[op])
    ax.set_xticks(x)
    ax.set_xticklabels(threads)
    
    
    cyclesx86_to_plot = np.full_like(cyclesEMU,cyclesx86[1])
    
    x86_plot = ax.plot(x,cyclesx86_to_plot,label='x86 @ 32 Threads',color="orange")
    x86_label = ax.annotate(str(format(cyclesx86[1],'1.1e')),
                xy=((x[0]+x[-1])/2, cyclesx86[1]),
                xytext=(0, 3),  # 3 points vertical offset
                textcoords="offset points",
                ha='center', va='bottom',color="orange")
    
    #print(x86_plot[0].get_ydata())
    
    ax.legend()
    
    #autolabel(x86_plot)
    autolabel(rects1,ax)
    
    #print(rects1[0].get_height())
    
    fig.tight_layout()
    
    plt.draw()
    bbox = x86_label.get_window_extent()
    
    ax = plt.gca()
    bbox_data = bbox.transformed(ax.transData.inverted())
    ax.update_datalim(bbox_data.corners())
    ax.autoscale_view()
    
    if ps == 1:
        plt.savefig(operation[op].split(' ')[1]+str(size)+'Spar'+str(sparsity)+'.svg',transparent = True)
        plt.savefig(operation[op].split(' ')[1]+str(size)+'Spar'+str(sparsity)+'.png',dpi = 200,transparent = True)
    
    plt.show()