from multiprocessing.sharedctypes import Value
from click import style
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np        
import pandas as pd
import warnings      

class Graphic:
    def __init__(self,data,palette):
        self.data =  data
        self.style = palette
        self.value=[]
        self.labels=[]
        for months,quantity in self.data:
            self.value.append(quantity)
            self.labels.append(months)
        
    def circle(self):
        colors = sns.color_palette(self.style)
        plt.pie(self.value, labels=self.labels,colors = colors, autopct = '%0.0f%%')
        plt.savefig('graph_circle.png')
        
    def bar_horizontal(self):
        #sns.barplot(x=self.labels,y=self.value, color='r',palette =self.style, saturation = 2) 
        #sns.barplot(x=self.value,y=self.labels, color='r', palette =self.style, saturation = 2, linewidth=5)
        colors = sns.color_palette(self.style)
        plt.barh(self.labels,self.value,color=colors)
        plt.xlabel('Quantity')
        plt.ylabel('Months')
        plt.title('Quantity per month')
        plt.savefig("graph_bar.png")

    def bar_vertical(self):
        fig, ax = plt.subplots()
        ax.bar(self.labels, self.value)
        plt.savefig("graph_bar_vertical.png")

    def linear(self):
        fig, ax = plt.subplots()
        ax.plot(self.labels, self.value)
        plt.savefig("graph_linear.png")

data_base=[('JANUARY',200),('FEBRUARY',100),('MARCH',70),('APRIL',175),('MAY',37),('JUNE',23)]
palette = 'pastel'
t1_graphic = Graphic(data_base,'pastel') 
#t1_graphic.circle()  
#t1_graphic.bar_horizontal()
t1_graphic.linear()
#t1_graphic.bar_vertical()
