# coding=utf-8
# ID3
from math import log
import operator

def createDataSet():
    dataSet = [[1, 1, 'yes'],
               [1, 1, 'yes'],
               [1, 0, 'no'],
               [0, 1, 'no'],
               [0, 1, 'no']]
    labels = ['no surfacing','flippers']
    #change to discrete values
    return dataSet, labels

# 计算数据集的信息熵
def calcShannonEnt(dataSet):
	numEntries = len(dataSet)
	labelCounts = {}

	# 分类项的数量
	for featVec in dataSet:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1

	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		shannonEnt -= prob * log(prob, 2)
	return shannonEnt

# 划分数据集
# axis带划分的特征，0表示第0个特征，1表示第1个特征
# value选择特征的值
def splitDataSet(dataSet, axis, value):
	retDataSet = []
	for featVec in dataSet:
		if featVec[axis] == value:
			reducedFeatVec = featVec[:axis]
			reducedFeatVec.extend(featVec[axis+1:])
			retDataSet.append(reducedFeatVec)
	return retDataSet

# 熵增益计算，选择增益最好的特征，ID3
def chooseBestFeatureToSplit(dataSet):
	numFeatures = len(dataSet[0]) - 1
	baseEntropy = calcShannonEnt(dataSet) # 计算数据集的熵

	bestInfoGain = 0.0; bestFeature = -1
	for i in range(numFeatures):
		featList = [example[i] for example in dataSet]
		# 列表转换为集合
		uniqueVals = set(featList)
		newEntropy = 0.0
		# 计算指定特征分类下的不同值的熵
		for value in uniqueVals:
			subDataSet = splitDataSet(dataSet, i, value)
			prob = len(subDataSet)/float(len(dataSet))
			newEntropy += prob * calcShannonEnt(subDataSet)

		# 熵增益
		infoGain = baseEntropy - newEntropy

		if(infoGain > bestInfoGain):
			bestInfoGain = infoGain
			bestFeature = i

	return bestFeature

# 计算分类标签出现最多的，排序
def majorityCnt(classList):
	classCount = {}
	for vote in classList:
		if vote not in classCount.keys():
			classCount[vote] = 0
		classCount[vote] += 1

	sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	return sortedClassCount[0][0]

# 生成决策树,贪心算法
def createTree(dataSet, labels):
	classList = [example[-1] for example in dataSet]
	if classList.count(classList[0]) == len(classList):
		return classList[0] # 当前类的标签都相等时
	if len(dataSet[0]) == 1:
		return majorityCnt(classList) # 当数据集的特征只有一项时

	# 信息增益变化最大
	bestFeat = chooseBestFeatureToSplit(dataSet)
	bestFeatLabel = labels[bestFeat]

	myTree = {bestFeatLabel:{}}
	del(labels[bestFeat])

	featValues = [example[bestFeat] for example in dataSet]
	uniqueVals = set(featValues)
	for value in uniqueVals:
		subLabels = labels[:]   # 递归算法
		myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value), subLabels)
	return myTree

# 决策树分类
def classify(inputTree, featLabels, testVec):
	firstStr = inputTree.keys()[0]
	secondDict = inputTree[firstStr]
	featIndex = featLabels.index(firstStr) # 属性标签的序号
	key = testVec[featIndex] # 特征标签对应的特征值
	valueOfFeat = secondDict[key] #
	if isinstance(valueOfFeat, dict):
		classLabel = classify(valueOfFeat, featLabels, testVec)
	else:
		classLabel = valueOfFeat
	return classLabel

# 存储决策树，持久化分类器
def storeTree(inputTree, filename):
	import pickle  # 数据的序列化
	fw = open(filename, 'w')
	pickle.dump(inputTree, fw)
	fw.close()

def grabTree(filename):
    import pickle
    fr = open(filename)
    return pickle.load(fr)


		

