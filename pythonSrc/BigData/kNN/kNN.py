#coding=utf-8
from numpy import *
import operator
from os import listdir

def createDataSet():
	group = array([1.0,1.1],[1.0,1.0],[0,0],[0,0.1]);
	labels = ['A','A','B','B']
	return group, labels

#K近邻算法
def classify0(intX, dataSet, labels, k):
	dataSetSize = dataSet.shape[0] #数组的维度
	#tile函数扩展数组的维度，本例为扩展为3*1的数组
	diffMat = tile(intX, (dataSetSize, 1)) - dataSet 
	sqDiffMat = diffMat**2
	#axis=1,数组内加
	sqDistances = sqDiffMat.sum(axis = 1)

	#得出各点到训练数据的距离
	distaces = sqDistances**0.5
	sortedDistIndicies = distaces.argsort()
	classCount = {}
	for i in range(k):
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel,0) + 1
	sortedClassCount = sorted(classCount.iteritems(), key = operator.itemgetter(1), reverse = True)
	return sortedClassCount[0][0]

#读取数据文件，转换为矩阵
def file2matrix(filename):
	fr = open(filename)
	numberOfLines = len(fr.readlines())
	returnMat = zeros((numberOfLines, 3));
	classLabelVector = []
	
	fr = open(filename)
	index = 0
	for line in fr.readlines():
		line = line.strip()
		listFromLine = line.split('\t')
		returnMat[index,:] = listFromLine[0:3]
		#-1表示列表的最后一个元素d
		classLabelVector.append(int(listFromLine[-1]))
		index += 1
	return returnMat, classLabelVector

#数值归一化
def autoNorm(dataSet):
	minVals = dataSet.min(0);#参数0表示读取每一列
	maxVals = dataSet.max(0);

	ranges = maxVals - minVals
	normDataSet = zeros(shape(dataSet))
	m = dataSet.shape[0]
	normDataSet = dataSet - tile(minVals, (m, 1))
	normDataSet = normDataSet/tile(ranges, (m, 1))
	return normDataSet, ranges, minVals

#测试分类器
def datingCLassTest():
	hoRatio = 0.10    #前10%的数据作为测试数据 后90%作为训练数据
	datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
	normMat, ranges, minVals = autoNorm(datingDataMat)

	m = normMat.shape[0]
	numTestVecs = int(m*hoRatio)
	errorCount = 0.0

	for i in range(numTestVecs):
		classifierResult = classify0(normMat[i,:], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
		print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, datingLabels[i])
		if (classifierResult != datingLabels[i]):
			errorCount += 1.0
	print "the total eror rate is: %f" % (errorCount/float(numTestVecs))
	print errorCount

# 手写测试：将训练数据图像转换为矩阵
def img2vector(filename):
	returnVect = zeros((1, 1024))
	fr = open(filename)
	for i in range(32):
		lineStr = fr.readline()
		for j in range(32):
			returnVect[0, 32*i*j] = int(lineStr[j])
	return returnVect

# 手写数据分类器测试
def handwritingClassTest():
	# 训练数据转换矩阵
	hwLabels = []
	trainingFileList = listdir('trainingDigits')
	m = len(trainingFileList)
	trainingMat = zeros((m, 1024))
	for i in range(m):
		fileNameStr = trainingFileList[i]
		fileStr = int(fileStr.split('_')[0])
		hwLabels.append(classNumStr)
		trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)

	# 测试数据
	testFileList = listdir('testDigits')
	errorCount = 0.0
	mTest = len(testFileList)
	for i in range(mTest):
		fileNameStr = testFileList[i]
		fileStr = fileNameStr.split('.')[0]
		classNumStr = int(fileStr.split('_')[0])
		vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
		classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
		print "the classifier came back with: %d, the real answer is: %d" % (classifierResult, classNumStr)
		if (classifierResult != classNumStr):
			errorCount += 1.0

	print "\nthe total number of errors is: %d" % errorCount
	print "\nthe total error rate is: %f" % (errorCount/float(mTest))




