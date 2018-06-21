#! /usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
#from sklearn.metrics import r2_score #計算相關係數用，這裡沒有用到


dataX = np.arange(0,100,1) #產出 [0,1,2....99]
#dataX = [ np.radians(x) for x in range(360)]
dataY = []
for y in dataX:
    dataY.append(np.log(y))
#dataY = np.random.randint(5,100, size=100) #產出 100 個 5~100 的隨機整數

def reg(x,y):
    coefficients = np.polyfit(x,y,1) # 利用 polyfit 幫我們算出資料 一階擬合的 a, b 參數
    p = np.poly1d(coefficients) # 做出公式, print 的結果是 coefficients[0] * X + coefficients[1]
    #coefficient_of_dermination = r2_score(y, p(x)) // 計算相關係數用，這裡沒有用到
    return coefficients, p

#(arg1, arg2), text1 = reg(dataX,dataY) 
#arg1, arg2 用來承接 coefficients[0], coefficients[1], text1 承接 p

#trend_line = dataX *arg1 + arg2 #做出趨勢線矩陣

plt.plot(dataX,dataY) #放上資料圖
#plt.plot(trend_line) #放上趨勢線圖
#plt.text(50, 10, text1, fontsize=14) #放上趨勢線公式
plt.show() #出圖