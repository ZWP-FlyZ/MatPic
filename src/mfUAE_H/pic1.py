# -*- coding: utf-8 -*-
'''
Created on 2018年7月5日

@author: zwp
'''
import numpy as np


import matplotlib.pyplot as plt



def show_UK():
    y = [
            [0.604,0.600,0.598,0.596,0.597,0.599,0.599,0.599,0.600,0.600,0.600,0.600],
            [0.537,0.528,0.526,0.525,0.524,0.526,0.526,0.526,0.526,0.526,0.526,0.527],
            [0.465,0.454,0.453,0.452,0.453,0.454,0.455,0.456,0.456,0.458,0.458,0.459],
            [0.437,0.425,0.423,0.424,0.424,0.425,0.426,0.428,0.429,0.430,0.431,0.432],
            [0.423,0.409,0.407,0.409,0.410,0.411,0.413,0.414,0.416,0.417,0.419,0.420]
        ]
    x = np.arange(3,48,4);
    y = np.array(y);
    plt.plot(x,y[0],'-x',label='d=2.5%',linewidth=3);
    plt.plot(x,y[1],'-o',label='d=5%',linewidth=3);
    plt.plot(x,y[2],'-^',label='d=10%',linewidth=3);
    plt.plot(x,y[3],'-v',label='d=15%',linewidth=3);
    plt.plot(x,y[4],'-s',label='d=20%',linewidth=3);
    plt.xlabel('U-K',fontsize=20);
    plt.ylabel('MAE',fontsize=20);
    plt.xticks(x,fontsize=20);
    plt.yticks(fontsize=20);
    plt.grid(True)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=2,
           ncol=3, mode="expand", borderaxespad=0.,fontsize='15')
    
    plt.show()


def show_SK():
    
    y1 =[ 
            [0.587,0.579,0.578,0.576,0.574,0.574,0.573,0.573,0.572,0.573,0.574,0.575],
            [0.521,0.512,0.510,0.509,0.509,0.508,0.509,0.510,0.511,0.511,0.511,0.512]
        ]
    
    y2 =[
            [0.444,0.437,0.437,0.436,0.436,0.436,0.437,0.437],
            [0.409,0.403,0.404,0.404,0.406,0.407,0.407,0.408],
            [0.396,0.391,0.393,0.396,0.399,0.402,0.403,0.404]
        ]
    y1 = np.array(y1);
    y2 = np.array(y2);
    
    x1 = np.arange(5,336,30);
    x2 = np.arange(5,76,10);

    
    plt.figure(1);
    
    
    plt.subplot(121);
    plt.plot(x1,y1[0],'-x',label='d=2.5%',linewidth=3);
    plt.plot(x1,y1[1],'-o',label='d=5%',linewidth=3);
    plt.xticks(x1,fontsize=15);
    plt.yticks(fontsize=20);
    plt.xlabel('S-K',fontsize=20);
    plt.ylabel('MAE',fontsize=20);
    plt.grid(True);
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=2,
           ncol=3, mode="expand", borderaxespad=0.,fontsize='15')
    
    plt.subplot(122);
    plt.plot(x2,y2[0],'-^',label='d=10%',linewidth=3);
    plt.plot(x2,y2[1],'-v',label='d=15%',linewidth=3);
    plt.plot(x2,y2[2],'-s',label='d=20%',linewidth=3);
    plt.xticks(x2,fontsize=15);
    plt.yticks(fontsize=20);
    plt.xlabel('S-K',fontsize=20);
    plt.ylabel('MAE',fontsize=20);
    plt.grid(True);
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=2,
           ncol=3, mode="expand", borderaxespad=0.,fontsize='15')    
    plt.show()



def show_sigma():
    y = [
            [0.580,0.572,0.574,0.575,0.577,0.580,0.582,0.586,0.589,0.593,0.598],
            [0.509,0.508,0.506,0.508,0.509,0.510,0.512,0.514,0.517,0.520,0.525],
            [0.437,0.435,0.433,0.434,0.435,0.436,0.438,0.441,0.444,0.448,0.453],
            [0.403,0.401,0.400,0.401,0.402,0.404,0.406,0.410,0.413,0.418,0.424],
            [0.393,0.390,0.386,0.387,0.387,0.388,0.390,0.393,0.397,0.402,0.408]
        ]
    x = np.arange(0,101,10)/100.0;
    y = np.array(y);
    plt.plot(x,y[0],'-x',label='d=2.5%',linewidth=3);
    plt.plot(x,y[1],'-o',label='d=5%',linewidth=3);
    plt.plot(x,y[2],'-^',label='d=10%',linewidth=3);
    plt.plot(x,y[3],'-v',label='d=15%',linewidth=3);
    plt.plot(x,y[4],'-s',label='d=20%',linewidth=3);
    plt.xlabel('δ',fontsize=20)
    plt.ylabel('MAE',fontsize=20)
    plt.xticks(x,fontsize=20);
    plt.yticks(fontsize=20);
    plt.grid(True)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=2,
           ncol=3, mode="expand", borderaxespad=0.,fontsize='15')
    
    plt.show()




if __name__ == '__main__':
    show_SK();
    pass