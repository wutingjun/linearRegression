#coding=utf-8
from numpy import *

#损失函数(最小误差平方和)的实现
def computeCost(X,y,theta):
    #训练样本数量
    m=len(y)

    J=0

    predictions=dot(X,theta)
    #在计算点乘上，数组和矩阵是不同的，数组使用*，矩阵使用multiply
    sqrErrors=multiply(predictions-y,predictions-y)

    J=1/float(2*m)*sum(sqrErrors)
    return J