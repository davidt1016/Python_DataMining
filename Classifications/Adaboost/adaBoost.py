from sklearn import tree
from sklearn.ensemble import AdaBoostClassifier
import pandas as pd


#Expansion of Q2 code with AdaBoost Code for better predicition
#Reading in class label data (X and Y), where Y is from testing the subset
def ClassLabel(range1, range2):
	dataset = pd.read_csv('DataSets.csv', header = None)
	XClassLabel =[]
	YClassLabel = []
	for i in range(0, 26000):
		if i>= range1 and i < range2:
			XClassLabel.append([(dataset.values[i,j]) for j in range(23, 24)])
			YClassLabel.append([(dataset.values[i,j]) for j in range(24, 25)])
	return XClassLabel, YClassLabel
#Reading data from CSV files and dividing it into 10 equal subset
def Partitioning(subRange1, subRange2):
	dataset = pd.read_csv('DataSets.csv', header = None)
	testingDataSet= []
	trainingClassLabels = []
	trainingDataSet= []
	for i in range(0,26000):
		#Appending testing data set 
		if i >= subRange1 and i < subRange2:
			testingDataSet.append([(dataset.values[i,j]) for j in range(0, 23)])
		else:
			#Appending training data set 
			trainingDataSet.append([(dataset.values[i,j]) for j in range(0, 23)])
			trainingClassLabels.append([(dataset.values[i,j]) for j in range(23, 24)])		
	#return two training data list and class labels according to each row of training data set
	return testingDataSet, trainingDataSet,trainingClassLabels
#Computing the decision Tree with different subset
def KFold(test, train, trainClass):
	#AdaBoost
	clf = AdaBoostClassifier( n_estimators=50, learning_rate=0.001)
	clf = clf.fit(train, trainClass)
	x = clf.predict(test)
	#writing into file
	file = open("Prediction.txt","a")
	for i in x:
		file.write(str(i))
		file.write("\n")
	file.close()
#computing the True positivie for each fold
def CountTruePositive(actualClass, predictedClass):
	index = 0
	TP = 0
	#Counting and searching for number of True Positives
	while index < len(actualClass):
		if (actualClass[index][0]==1) and (actualClass[index][0]==predictedClass[index][0]):
			TP = TP + 1
		index = index + 1
	return TP
#Counting Number of True Negatives
#computing the True positivie for each fold
def CountTrueNegative(actualClass, predictedClass):
	index = 0
	TN = 0
	#Counting and searching for number of True Positives
	while index < len(actualClass):
		if (actualClass[index][0]==0) and (actualClass[index][0]==predictedClass[index][0]):
			TN = TN + 1
		index = index + 1
	return TN
#Counting Number of False Positive for each fold
def CountFalsePositive(actualClass, predictedClass):
	index = 0
	FP = 0 
	while index < len (actualClass):
				#Actual class is 0 but predicted is 1

		if (actualClass[index][0]==0) and (predictedClass[index][0]==1):
			FP = FP + 1
		index = index + 1
	return FP

#Counting Number of False Negative for each fold
def CountFalseNegative(actualClass, predictedClass):
	index = 0
	FN = 0 
	while index < len (actualClass):
		#Actual class is 1 but predicted is 0
		if (actualClass[index][0]==1) and (predictedClass[index][0]==0):
			FN = FN + 1
		index = index + 1
	return FN
#First Partition
"""
testData , trainData, trainDataClass = Partitioning(0,2600)
KFold(testData, trainData, trainDataClass)

#Second Partition
testData1 , trainData1, trainDataClass1 = Partitioning(2600,5200)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(5200,7800)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(7800,10400)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(10400,13000)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(13000,15600)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(15600,18200)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(18200,20800)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(20800,23400)
KFold(testData1, trainData1, trainDataClass1)

testData1 , trainData1, trainDataClass1 = Partitioning(23400,26000)
KFold(testData1, trainData1, trainDataClass1)
"""
#Computing Accuracy, Recall, Precision Based on Class Label
#Computing for a list of True positives for 10 different folds

#Performance Evaluation Manual Computation


FNList = []
FPList = []
TNList = []
TPList = []
i = 0 
while i <= 23400:
	XClass, YClass = ClassLabel(i,i+2600)
	#Collecting each false negative for each fold
	FN = CountFalseNegative(XClass,YClass)
	FNList.append(FN)
	#Collecting each false positive for each fold
	FP = CountFalsePositive(XClass,YClass)
	FPList.append(FP)
	#Collecting each true negative for each fold
	TN = CountTrueNegative(XClass, YClass)
	TNList.append(TN)
	#Collecting each true positive for each fold
	TP = CountTruePositive(XClass,YClass)
	TPList.append(TP)
	i = i + 2600

deno = 2600
#Compute accuracy, precision, and recall for each fold/parition
index = 0
range1 = 0
#Iterating through each partition result and compute its performance measure
while index < 10:
	print("----------------------Accuracy, Precision, and Recall for ", range1, "to", range1+2600, "Subset-------------------")
	accuracy1 = (TPList[index]+TNList[index])/deno
	precision1 = (TPList[index])/(TPList[index]+FPList[index])
	recall1 = (TPList[index])/ (TPList[index]+ FNList[index])
	print("Accuracy: ", round(accuracy1,3))
	print("Precision: ", round(precision1,3))
	print("Recall: ", round(recall1,3))
	index = index +1
	range1 = range1 + 2600
