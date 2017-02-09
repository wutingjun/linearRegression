#coding=utf-8

from numpy import *
import os

# 对样本特征归一化处理
def predictInputNorm(X):
    # 第一列特征归一化
    fileIn=open(os.path.join(os.path.dirname(__file__),'featureScaling/Gaussian.txt'))
    mu_mutrix=fileIn.readline().split('\t')[0]
    sigma_mutrix=fileIn.readline().split('\t')[0]
    x1=divide(X[:,0]-mat(float(mu_mutrix)),mat(float(sigma_mutrix)))
    fileIn.close()

    # 第二列特征归一化
    fileIn=open(os.path.join(os.path.dirname(__file__),'featureScaling/Gaussian.txt'))
    mu_mutrix=fileIn.readline().split('\t')[1]
    sigma_mutrix=fileIn.readline().split('\t')[1]
    x2=divide(X[:,1]-mat(float(mu_mutrix)),mat(float(sigma_mutrix)))
    fileIn.close()

    X_norm=c_[x1,x2]
    return  X_norm
