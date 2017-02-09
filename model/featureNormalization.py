from numpy import *

from featureScaling import featureNorm

def featureNormalize(X):
    X_Norm=featureNorm.meanNorm(X)

    return X_Norm
