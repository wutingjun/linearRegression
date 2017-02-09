#coding=utf-8

from numpy import *
import computeCost

def gradientDescent(X,y,theta,alpha):
    m=len(y)
    J_history=computeCost.computeCost(X,y,theta)

    while True:
        h=dot(X,theta)
        errors_vector=h-y
        theta_change=alpha*1/float(m)*dot(transpose(X),errors_vector)
        theta=theta-theta_change

        J_now=computeCost.computeCost(X,y,theta)
        #当这一次和上一次损失函数之间的差值小于0.00001,停止循环
        if abs(J_now-J_history)<0.00001:
            break
        J_history=J_now

    return theta