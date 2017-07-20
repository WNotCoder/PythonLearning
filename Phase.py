import math
import numpy as np
import matplotlib.pyplot as plt
from pylab import *


#极坐标转换为常规坐标
def convToNorm(radi,phase):
    rad = (float(phase) / float(180)) * math.pi
    x = round(radi * math.cos(rad),3)
    y = round(radi * math.sin(rad),3)
    return x,y


#常规坐标转换为极坐标
def convToPolar(x,y):
    if int(x) == 0:
        radi = y
        phase = 0
    elif int(y) == 0:
        radi = x
        phase = 90
    else:
        radi = round(math.sqrt((x**x)+(y**y)),3)
        phase = round((math.atan(float(x)/float(y))*180/math.pi),3)

    return radi,phase

#相量加减法
def addPhasor(arr1,arr2,oprt):
    '''
    :param arr1: 相量1
    :param arr2: 相量2
    :param oprt: 做加法还是做减法
    :return:
    '''
    if oprt == '-':
        x = arr1.x - arr2.x
        y = arr1.y - arr2.y
        arrReslt = Phasor('crs',x,y)
        return arrReslt
    elif oprt == '+':
        x = arr1.x + arr2.x
        y = arr1.y + arr2.y
        arrReslt = Phasor('crs',x,y)
        return arrReslt
    else:
        #raise TypeError #oprt操作符异常
        pass

#相量类
class Phasor(object):

    def __init__(self,type,var1,var2,name):
        '''
        :param var1: 极坐标下相量的模/正交坐标下相量的x轴坐标
        :param var2: 极坐标下相量的相角/正交坐标下相量y轴坐标
        :param type: 相量的表现方式，1：极坐标；2：正交坐标
        :param name: 相量的名字
        '''
        self.name = name
        if type == 'plr':
            #极坐标形式下，输入的两个变量为模和相角
            self.radi = var1
            self.phase = var2
            self.x,self.y = convToNorm(var1,var2)

        elif type == 'crs':
            #正交坐标形式下，输入的为x，y轴坐标
            self.radi,self.phase = convToPolar(var1,var2)
            self.x = var1
            self.y = var2

def drawPhasor(phasorList):

    fig = plt.figure(figsize=(5,5))
    ax = fig.add_subplot(111)

    #绘图的直线集合
    plotList = []

    #坐标范围，默认全为零，遍历向量时，取向量最大最小值作为坐标范围
    axisArea = [0,0,0,0]

    #网上扒的，反正就是这几行执行完以后（0,0）点就成为坐标轴中心了
    ax.spines['top'].set_color('none')
    ax.spines['right'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.spines['bottom'].set_position(('data', 0))
    ax.yaxis.set_ticks_position('left')
    ax.spines['left'].set_position(('data', 0))

    #设置坐标轴刻度
    xmajorLocator = MultipleLocator(20)    #设置x轴主刻度
    xminorLocator   = MultipleLocator(5)    #设置x轴次刻度
    ymajorLocator = MultipleLocator(20)
    yminorLocator   = MultipleLocator(5)
    ax.xaxis.set_major_locator(xmajorLocator)    #执行之前的设置
    ax.xaxis.set_minor_locator(xminorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.xaxis.grid(True, which='major',linestyle=':')    #x轴显示网格线，显示主刻度网格，线型点状
    ax.yaxis.grid(True, which='minor',linestyle=':')    #y轴显示网格线，显示次刻度网格，线型点状

    #遍历所有传入的相量，并且绘图
    for ph in phasorList:
        #找到所有相量中的x，y坐标的最大最小值，并作为坐标的范围
        axisArea[0] = min(ph.x,axisArea[0])
        axisArea[1] = max(ph.x,axisArea[1])
        axisArea[2] = min(ph.y, axisArea[2])
        axisArea[3] = max(ph.y, axisArea[3])

        pX = [0, ph.x]
        pY = [0, ph.y]
        plotList.append(ax.plot(pX,pY,'-',label=ph.name))

    #设置坐标轴范围
    axis(axisArea)
    #设置显示图例
    plt.legend()
    #显示最终绘图结果
    plt.show()


phasorList = []
i = 0
print("相量输入格式：‘名称，坐标类型，坐标值1，坐标值2'，坐标类型（plr：极坐标，crs：正交坐标）")
while True:
    i += 1

    package = input('请输入相量名称或者输入“exit”退出：').split(',')
    phName = package[0]


    if phName != 'exit':
        phType, phVar1, phVar2 = package[1:]
        phasorList.append(Phasor(phType,float(phVar1),float(phVar2),phName))
    else:
        break

drawPhasor(phasorList)



'''
ua = Phasor('plr', 57.7, 0, 'ua')
ub = Phasor('plr',57.7,-120,'ub')
uc = Phasor('plr',57.7,120,'uc')

phasorList = [ua,ub,uc]
drawPhasor(phasorList)
'''

