import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pyplot import figure, show
from matplotlib.ticker import MaxNLocator
        

class bar_plot_pp:
    
    def __init__(self,x_data,y_data,labels,x_min,size,params,alpha=0.2, linewidth=5,color='#007ACC'):
        
        '''
        args : 
        x_data : class
        y_data : percentage
        labels : class array [x_label,y_label]
        shape : x,y range
        params : [nb classes, nb échantillon, legend, title , ytitle]
        
        '''
        
        plt.style.available
        plt.style.use('ggplot')
        
        self.xlabel = labels[0] 
        self.ylabel = labels[1]
        self.x_min = x_min
        
        self.linewidth = linewidth
        self.alpha = alpha
        self.size_x = size[0]
        self.size_y = size[1]
        self.color = color
        self.y_data = y_data
        self.x_data = x_data
        self.label = params[0]
        self.title = params[1] + "\n" + params[0]
        self.ytitle = params[2] 
        self.fig, self.ax = plt.subplots(figsize=(self.size_x,self.size_y))
        self.ax2 =  self.ax.twinx()
        
    def set_global_params(self):
        
        plt.rcParams['font.family'] = 'sans-serif'
        plt.rcParams['font.sans-serif'] = 'Helvetica'
    
        plt.rcParams['axes.edgecolor']='#333F4B'
        plt.rcParams['axes.linewidth']=0.8
        plt.rcParams['xtick.color']='#333F4B'
        plt.rcParams['ytick.color']='#333F4B'
        
        # change the style of the axis spines
        self.ax.spines['top'].set_color('none')
        self.ax.spines['right'].set_color('none')
        self.ax2.spines['top'].set_color('none')
        self.ax2.spines['right'].set_color('none')
        #self.ax.spines['left'].set_smart_bounds(True)
        #self.ax.spines['bottom'].set_smart_bounds(True)
        

    def set_labels(self):
        self.ax.set_xlabel(self.xlabel,fontsize=15, fontweight='black', color = '#333F4B')
        self.ax.set_ylabel(self.ytitle,fontsize=15, fontweight='black', color = '#333F4B')
        #self.ax2.set_xlabel(self.xlabel,fontsize=15, fontweight='black', color = '#333F4B')
        #self.ax2.set_ylabel(self.ytitle,fontsize=15, fontweight='black', color = '#333F4B')
        self.ax.yaxis.set_major_locator(MaxNLocator(integer=True))
        self.ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
        
        #self.ax.set_yticks(self.x_data)
        plt.yticks(self.x_data,self.ylabel)
        # set axis
        # set labels style
    
    def show(self):
        
        #df.plot(kind='barh', legend = False, ax=self.ax)
        plt.hlines(y=self.x_data, xmin=self.x_min, xmax=self.y_data, color=self.color, alpha=self.alpha, label=self.label,linewidth=self.linewidth)
        plt.plot(self.y_data, self.x_data, "o", markersize=5, color=self.color, alpha=0.6)
        
        self.ax.legend(fancybox=True, framealpha=0.7)
        self.ax.set_title(self.title)

    
        self.set_labels()
        self.set_global_params()
        
        