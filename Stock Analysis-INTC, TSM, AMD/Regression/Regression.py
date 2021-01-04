import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split 
from sklearn import metrics

#reading the data from file
def readTrainingFile(filename):
	training = pd.read_csv(filename+'.csv')
	Y_Train = []
	X_Train = []
	for i in range(0,148):
		Y_Train.append([(training.values[i,j]) for j in range(2,3)])
		X_Train.append([(training.values[i,j]) for j in range(0, 1)])
	return X_Train, Y_Train
#Reading in test file
def readTestingFile(filename):
	testing = pd.read_csv(filename+'.csv')
	X_Test = []
	for i in range(0,105):
		X_Test.append([(testing.values[i,j]) for j in range(0, 1)])
	return X_Test 

#convert list within a list to one list with only data in it
def Data(data):
	resData = []
	index  = 0
	res = 0
	while index < len(data):
		res = data[index][0]
		resData.append(res)
		index = index + 1
	return resData
def WriteFile(filename, data):
	file = open(filename+".txt","a")
	for i in data:
		file.write(str(i))
		file.write("\n")
	file.close()

#Reading file from TSM, AMD, and INTC
X_TSM, Y_TSM = readTrainingFile('TSM_Training')
X_AMD, Y_AMD = readTrainingFile('AMD_Training')
X_INTC, Y_INTC = readTrainingFile('INTC_Training')

#Testing data, since all the testing data are the same for each file, only one file needs to be read in
X_TestData = readTestingFile('TSM_Testing')
#For Plotting Later
X_Transformed = Data(X_TestData)

#Training and splitting with original data (Cross Validation)
X_Train, X_Test, Y_Train, Y_Test = train_test_split(X_TSM, Y_TSM, test_size=0.25, random_state=0)
regTSM = LinearRegression().fit(X_Train, Y_Train)
Y_Pred = regTSM.predict(X_Test)

print("--------------TSM Training with 75%(Training) and 25%(Testing) Split--------------")
print("Coefficient of Determination R^2 of the Prediction:",regTSM.score(X_Test,Y_Test))
#Output the MAE error for reference: average of all absolute errors
print("Mean Absolute Error:", metrics.mean_absolute_error(Y_Test, Y_Pred))

#------------------------Predicting TSM Stocks-----------------------
regTestTSM = LinearRegression().fit(X_Train, Y_Train)
regPredTSM = regTestTSM.predict(X_TestData)
regPredTSM = Data(regPredTSM)
#print("------------------------Predicted TSM Stocks------------------------")
#print(regPredTSM)
#Writing the result into file
WriteFile("TSM", regPredTSM)
#Plotting 
plt.plot(X_TSM, Y_TSM, color='red' ,label ='Actual')
plt.plot(X_Transformed, regPredTSM, color = 'blue', label ='Predicted')
plt.xlabel('Days')
plt.ylabel('Stock Closing Prices')
plt.title('TSM Stock Prices in 2020')
plt.legend(loc ='upper right')
plt.show()

#---------------------------------AMD---------------------------------
X_TrainAMD, X_TestAMD, Y_TrainAMD, Y_TestAMD = train_test_split(X_AMD, Y_AMD, test_size=0.25, random_state=0)
regAMD = LinearRegression().fit(X_TrainAMD, Y_TrainAMD)
Y_PredAMD = regAMD.predict(X_TestAMD)

print("--------------AMD Training with 75%(Training) and 25%(Testing) Split--------------")
print("Coefficient of Determination R^2 of the Prediction:",regAMD.score(X_TestAMD,Y_TestAMD))
#Output the MAE error for reference: average of all absolute errors
print("Mean Absolute Error:", metrics.mean_absolute_error(Y_TestAMD, Y_PredAMD))
#------------------------Predicting TSM Stocks-----------------------
regTestAMD = LinearRegression().fit(X_TrainAMD, Y_TrainAMD)
regPredAMD = regTestAMD.predict(X_TestData)
regPredAMD = Data(regPredAMD)
#print("------------------------Predicted AMD Stocks------------------------")
#print(regPredAMD)
WriteFile("AMD", regPredAMD)
#Plotting 
plt.plot(X_AMD, Y_AMD, color='red' ,label ='Actual')
plt.plot(X_Transformed, regPredAMD, color = 'blue', label ='Predicted')
plt.xlabel('Days')
plt.ylabel('Stock Closing Prices')
plt.title('AMD Stock Prices in 2020')
plt.legend(loc ='upper right')
plt.show()

#---------------------------------INTC---------------------------------
X_TrainINTC, X_TestINTC, Y_TrainINTC, Y_TestINTC = train_test_split(X_INTC, Y_INTC, test_size=0.25, random_state=0)
regINTC = LinearRegression().fit(X_TrainINTC, Y_TrainINTC)
Y_PredINTC = regINTC.predict(X_TestINTC)

print("--------------INTC Training with 75%(Training) and 25%(Testing) Split--------------")
print("Coefficient of Determination R^2 of the Prediction:",regINTC.score(X_TestINTC,Y_TestINTC))
#Output the MAE error for reference: average of all absolute errors
print("Mean Absolute Error:", metrics.mean_absolute_error(Y_TestINTC, Y_PredINTC))
#------------------------Predicting TSM Stocks-----------------------
regTestINTC = LinearRegression().fit(X_TrainINTC, Y_TrainINTC)
regPredINTC = regTestINTC.predict(X_TestData)
regPredINTC = Data(regPredINTC)
#print("------------------------Predicted INTC Stocks------------------------")
#print(regPredINTC)
WriteFile("INTC", regPredINTC)
#Plotting
plt.plot(X_INTC, Y_INTC, color='red' ,label ='Actual')
plt.plot(X_Transformed, regPredINTC, color = 'blue', label ='Predicted')
plt.xlabel('Days')
plt.ylabel('Stock Closing Prices')
plt.title('INTC Stock Prices in 2020')
plt.legend(loc ='upper right')
plt.show()
