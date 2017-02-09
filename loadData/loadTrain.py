#coding=utf-8

from numpy import *

def loadTrainData(filename):
    fileIn=open(filename)
    dataSet=[]
    for line in fileIn:
        lineArr=line.strip().split(',')
        for x in xrange(0,len(lineArr)):
            lineArr[x]=float(lineArr[x])
        dataSet.append(lineArr)

    fileIn.close()

    return mat(dataSet)