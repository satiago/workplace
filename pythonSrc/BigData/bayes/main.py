# coding=utf-8

import bayes

listOPosts, listClasses = bayes.loadDataSet()
myVobList = bayes.createVocabList(listOPosts)
trainMat = []
for postinDoc in listOPosts:
	trainMat.append(bayes.setOfWords2Vec(myVobList, postinDoc))

p0v, p1v, pAb = bayes.trainNB0(trainMat, listClasses)