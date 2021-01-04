import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
import pandas as pd
#-------------------Q4-----------------
#reading in data from excel for training
def readFile(filename, numofTuples):
	dataset = pd.read_csv(filename+'.csv')
	excelData= []
	for i in range(0,numofTuples):
		excelData.append([(dataset.values[i,j]) for j in range(1, 6)])
	return excelData
#compute sum of square of distances
def ComputeSSD(testingData, centroids, clusterLabels):
	#sum of square distances variables
	SSD = 0
	index  = 0
	jindex = 0
	Diff = 0
	#Computing the SSD
	while index < len(testingData):
		#Getting the corresponding centers for computing SSD
		centers = centroids[clusterLabels[index]]
		#Iterating through each attribute
		while jindex < 5:
			Diff = float(centers[jindex]-testingData[index][jindex])**2
			#Adding up all the sum
			SSD += Diff
			jindex = jindex+1
		jindex = 0
		index = index + 1
	#Returning the final results of Sum of square distances
	return SSD

#Reading in training and testing Data Set
training = readFile('training',4339)
testing = readFile('testing', 500)
#Number of cluster to run initially
numCluster = 10
listSSD = []
result = 0

#Calculating for each number of clusters from 10 to 30
while numCluster <= 30:
#Fitting the data for KMeans
	kmeans = KMeans(n_init = 10, n_clusters = numCluster).fit(training)
	testLabels = kmeans.predict(testing)
	trainingCentroids = kmeans.cluster_centers_
	result = ComputeSSD(testing, trainingCentroids,testLabels )
	listSSD.append(result)
	numCluster += 1

#Output the result
print(listSSD)
print("Minimal Sum of Squared Distances Valus is: ", min(listSSD))
