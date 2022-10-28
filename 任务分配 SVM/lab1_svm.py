# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from numpy import *
from svmMLiA import *

def loadImages(dirName):
    from os import listdir
    hwLabels=[]
    trainingDileList=listdir(dirName)
    m=len(trainingDileList)
    trainingMat=zeros((m,1024))
    for i in range(m):
        fileNameStr=trainingFlieList[i]
        fileStr=fileNameStr.split('.')[0]
        classNumStr=int(fileStr.split('_')[0])
        if classNumStr==9:hwLabels.append(-1)
        else: hwLabels.append(1)
        trainingMat[i,:]=img2vector('%s/%s' % (dirName,fileNameStr))
    return trainingMat,hwLabels

def img2vector(filename):
    returnVect=zeros((1,1024))
    fr=open(filename)
    for i in range(32):
        lineStr=fr.readline()
        for j in range(32):
            returnVect[0,32*i+j]=int(lineStr[j])
    return returnVect

def testDigits(kTup=('rbf',10)):
    dataArr,labelArr=loadImages('./trainingDigits')
    b,alphas=smoP(dataArr,labelArr,200,0.0001,10000,kTup)
    datMat=mat(dataArr); lanelMat=mat(lanelArr).transpose()
    svInd=nonzero(alphas.A>0)[0]
    sVs=datMat[svInd]
    labelSV=labelMat[svInd];
    print ("there are %d Support Vectors" % shape(sVs)[0])
    m,n= shape(datMat)
    errorCount=0
    for i in range(m):
        kernelEval = kernelTrans (sVs,datMat[i,:],kTup)
        predict=kernelEval.T * multiply(labelSV,alphas[svInd])+ b
        if sign(predict)!=sign(labelArr[i]): errorCount += 1
    print ("the training error rate is: %f" % (float(errorCount)/m))
    dataArr,labelArr = loadImages ('testDigits')
    errorCount=0
    datMat=mat(dataArr); labelMat = mat(labelArr).transpose()
    m,n= shape(datMat)
    for i in range(m):
        kernelEval = kernelTrans(sVs,datMat[i,:],kTup)
        predict=kernelEval.T * multiply(labelSV,alIphas[svInd])+ b
        if sign(predict)!=sign(labelArr[i]): errorCount += 1
    print ("the test error rate is: %f" % (float(errorCount)/m))
    
    if _name_=="_main_":
        testDigits(('rbf',20))


