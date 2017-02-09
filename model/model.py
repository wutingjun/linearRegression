#coding=utf-8

from numpy import *
import os

from loadData import loadTrain
import featureNormalization
import gradientDescent

def get_model(file):
    # 训练数据集
    train_dataSet=loadTrain.loadTrainData(file)

    numSamples,numFeatures=train_dataSet.shape
    #输入特征X=<x1,x2,...,xn>和y值
    X=train_dataSet[:,:numFeatures-1]
    y=train_dataSet[:,numFeatures-1]

    # 训练数据特征归一化，不同的类型的特征归一化的方法应该不同，并返回归一化之后的结果
    X=featureNormalization.featureNormalize(X)

    # 在X左边加一列1是为了表示截距
    X=c_[ones([numSamples,1]),X]

    #本来参数个数numFeatures-1，但因为在X左边加一列，所以特征个数为numFeatures
    theta=zeros([numFeatures,1])
    alpha=0.01

    #用梯度下降求参数
    theta=gradientDescent.gradientDescent(X,y,theta,alpha)

    # 输出模型参数到文件，后面可以直接使用参数
    row,column=theta.shape
    theta_file=os.path.join(os.path.dirname(os.path.dirname(__file__)),'theta.txt')
    fileOut=open(theta_file,'w')
    for i in xrange(0,row):
        write_data=str(theta[i,0])+'\n'
        fileOut.write(write_data)
    fileOut.close()

get_model(os.path.join(os.path.dirname(os.path.dirname(__file__)),'ex1data2.txt'))
