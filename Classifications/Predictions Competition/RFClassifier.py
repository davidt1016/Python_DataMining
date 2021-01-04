from sklearn import tree
import pandas as pd
from sklearn.ensemble import RandomForestClassifier


#Reading data from CSV files and dividing it into 10 equal subset
def Partitioning():
	dataset = pd.read_csv('DataSets.csv', header = None)
	testingDataSet= []
	trainingClassLabels = []
	trainingDataSet= []
	#Reading training data
	for i in range(0,26000):
		#Appending training data set 
		trainingDataSet.append([(dataset.values[i,j]) for j in range(0, 23)])
		trainingClassLabels.append([(dataset.values[i,j]) for j in range(23, 24)])	

	testdataset = pd.read_csv('testData.csv', header = None)
	#reading in test data
	for k in range(0,5000):
		testingDataSet.append([(testdataset.values[k,j]) for j in range(0, 23)])
	#return two training data list and class labels according to each row of training data set as well as test data set
	return testingDataSet, trainingDataSet,trainingClassLabels
#Predicting the output for test class
def Classification(test, train, trainClass):

	#clf = AdaBoostClassifier( n_estimators=150, learning_rate=0.6)
	#Rainforest is proned to overfitting and its decent
	clf = RandomForestClassifier(n_estimators=300)
	
	clf = clf.fit(train, trainClass)
	x = clf.predict(test)
	#writing into file
	file = open("output4.txt","a")
	for i in x:
		file.write(str(i))
		file.write("\n")
	file.close()


testData, trainData, trainLabelClass = Partitioning()
Classification(testData, trainData,trainLabelClass)