#coding=utf-8

from numpy import *

import inputNorm

if __name__=='__main__':
    # 获取模型参数theta值
    theta=[]
    fileIn=open('theta.txt')
    for line in fileIn:
        theta.append(float(line.strip()))
    fileIn.close()
    theta=transpose(mat(theta))

    # 预测样本
    fileIn=open('predict_input.txt')
    for line in fileIn:
        lineArr=line.strip().split(',')
        for x in xrange(0,len(lineArr)):
            lineArr[x]=float(lineArr[x])

        predict_sample=mat(lineArr)
        predict_sample=inputNorm.predictInputNorm(predict_sample)
        predict_sample=c_[ones([1,1]),predict_sample]

        predict_result=dot(predict_sample,theta)
        print float(predict_result)
    fileIn.close()
