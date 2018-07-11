# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: zwp
'''
import numpy as np


import matplotlib.pyplot as plt

def showpic():
    
    
    x_l = np.arange(5,30,3);
    y_l = np.array([0.439,0.424,0.419,0.417,0.418,0.418,0.419,0.423,0.424]);
    print(x_l);
    _, ax = plt.subplots();
    ax.plot(x_l, y_l,'-^',label="a" )
    # ax.plot(x_l, y_l,'-o', label="b")
    plt.xlabel('U-K')
    plt.ylabel('MAE')
    plt.title('Should be growing...')
    plt.xticks(x_l);
    plt.grid(True)
    plt.legend()


    
    plt.show()


def showpic2():
    
    
    x_l = np.arange(5,30,3);
    y_l = np.array([0.439,0.424,0.419,0.417,0.418,0.418,0.419,0.423,0.424]);
    print(x_l);
    _, ax = plt.subplots()
    ax.plot(x_l, y_l,'-^',label="a" )
    # ax.plot(x_l, y_l,'-o', label="b")
    plt.xlabel('U-K')
    plt.ylabel('MAE')
    plt.title('Should be growing...')
    plt.xticks(x_l);
    plt.grid(True)
    plt.legend()


    
    plt.show()




if __name__ == '__main__':
    showpic();
    pass